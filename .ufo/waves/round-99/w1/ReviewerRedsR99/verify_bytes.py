#!/usr/bin/env python3
"""ReviewerRedsR99: byte-level checks of the ExecRedsR99 candidate in $D."""
import hashlib, json, re, subprocess, sys
from pathlib import Path

D = Path("/fast/scratch/hyaku/kotoba-r99/ReviewerRedsR99/repo")
BASE = "b53e209603e7c480cd975ea543e415b66f695438"
HEAD = subprocess.run(["git", "-C", str(D), "rev-parse", "HEAD"],
                      capture_output=True, text=True).stdout.strip()

def show(rev, path):
    p = subprocess.run(["git", "-C", str(D), "show", f"{rev}:{path}"],
                       capture_output=True)
    return p.stdout

PINS_RE = re.compile(rb"^INSTRUMENT_PINS = \{\n.*?^\}\n", re.M | re.S)
CORR_RE = re.compile(rb"^GOVERNANCE_CORRECTIONS = \(\n.*?^\)\n", re.M | re.S)
HORIZON_RE = re.compile(rb"^GOVERNANCE_CORRECTIONS_HORIZON = \d+\n", re.M)

fails = []
# 1. checklist data-only
a, b = show(BASE, "verifiers/verify_skill_checklist.py"), show(HEAD, "verifiers/verify_skill_checklist.py")
for x, who in ((a, "base"), (b, "HEAD")):
    if len(CORR_RE.findall(x)) != 1 or len(HORIZON_RE.findall(x)) != 1:
        fails.append(f"checklist {who}: corr/horizon not found exactly once")
sa = HORIZON_RE.sub(b"", CORR_RE.sub(b"", a))
sb = HORIZON_RE.sub(b"", CORR_RE.sub(b"", b))
print("checklist data-only strip equal:", sa == sb)
if sa != sb:
    fails.append("checklist bytes differ outside corrections data")
# block shapes at HEAD
hblock = CORR_RE.search(b).group(0).decode()
print("horizon at HEAD:", HORIZON_RE.search(b).group(0).decode().strip())
print("correction rows at HEAD:", hblock.count("(3") + hblock.count("(27") + hblock.count("(26") + hblock.count("(35"))

# 2. battery pins-only
a, b = show(BASE, "verifiers/check_tip_battery.py"), show(HEAD, "verifiers/check_tip_battery.py")
for x, who in ((a, "base"), (b, "HEAD")):
    if len(PINS_RE.findall(x)) != 1:
        fails.append(f"battery {who}: INSTRUMENT_PINS not found exactly once")
pa, pb = PINS_RE.sub(b"", a), PINS_RE.sub(b"", b)
print("battery pins-only strip equal:", pa == pb)
if pa != pb:
    fails.append("battery bytes differ outside INSTRUMENT_PINS")
pins = PINS_RE.search(b).group(0).decode()
m = re.search(r'"verifiers/verify_skill_checklist\.py": \(([^)]*)\)', pins, re.S)
pin_list = re.findall(r'"([0-9a-f]{40})"', m.group(1))
print("checklist pins:", pin_list)

# 3. pin == blob sha of HEAD checklist
blob = subprocess.run(["git", "-C", str(D), "rev-parse", f"{HEAD}:verifiers/verify_skill_checklist.py"],
                      capture_output=True, text=True).stdout.strip()
print("HEAD checklist blob:", blob, "pinned:", blob in pin_list)
if blob not in pin_list:
    fails.append("new checklist blob not pinned")

# 4. LOG.md notice lines sha256 vs rows
log = show(HEAD, "LOG.md").decode().splitlines()
print("LOG.md lines at HEAD:", len(log))
rows = re.findall(r'\((\d+),\s*\n\s*"([0-9a-f]{64})",\s*\n\s*"(LOG\.md|SCORECARD\.md)", (\d+), "([^"]+)",\s*\n\s*"([^"]+)"\)', hblock)
print("parsed rows:", len(rows))
for line_no, digest, sfile, sline, stale, corrected in rows:
    line_no = int(line_no)
    if line_no > len(log):
        fails.append(f"row {line_no}: past LOG end")
        continue
    text = log[line_no - 1]
    got = hashlib.sha256(text.encode()).hexdigest()
    ok = got == digest and stale in text and corrected in text
    if not ok:
        fails.append(f"row {line_no}: sha={'ok' if got==digest else 'MISMATCH'} stale={'on' if stale in text else 'OFF'} corrected={'on' if corrected in text else 'OFF'}")
print("notice rows verified:", len(rows), "failures:", [f for f in fails if "row" in f] or "none")

# 5. round-81 diff strictly line 8, hash identical
a = show(BASE, "corpus/lessons/round-81.md").decode().splitlines()
b = show(HEAD, "corpus/lessons/round-81.md").decode().splitlines()
if len(a) != len(b):
    fails.append("round-81: line count changed")
diffs = [(i + 1, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
for ln, x, y in diffs:
    print(f"round-81 diff at line {ln}:")
    print("  old:", x[:160])
    print("  new:", y[:160])
same_except_quotes = all(
    x.replace("`8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`", '"8b1cc1b00a9322cd8e231d87e015e1d75d20adc1"') == y
    for _, x, y in diffs)
print("round-81 changes confined to backtick->double-quote of the hash:", same_except_quotes, "(changed lines:", [ln for ln, _, _ in diffs], ")")
if not (len(diffs) == 1 and diffs[0][0] == 8 and same_except_quotes):
    fails.append("round-81: change not confined to line 8 hash quoting")

# 6. baseline JSON shape
bl = json.loads(show(HEAD, "verifiers/corpus-baseline.json"))
checks = bl["checks"]
print("baseline equal expects:", {k: v["expect"] for k, v in checks.items() if v["mode"] == "equal"})
print("baseline zero modes unchanged:",
      {k: v["expect"] for k, v in checks.items() if v["mode"] == "zero"} ==
      {k: v["expect"] for k, v in json.loads(show(BASE, "verifiers/corpus-baseline.json"))["checks"].items() if v["mode"] == "zero"})

# 7. patch scope: only the six owned paths
name_only = subprocess.run(["git", "-C", str(D), "diff", "--name-only", BASE, HEAD],
                           capture_output=True, text=True).stdout.split()
expected = {"LOG.md", "corpus/README.md", "corpus/lessons/round-81.md",
            "verifiers/check_tip_battery.py", "verifiers/corpus-baseline.json",
            "verifiers/verify_skill_checklist.py"}
print("changed files:", sorted(name_only))
if set(name_only) != expected:
    fails.append(f"patch scope mismatch: {sorted(set(name_only) ^ expected)}")

print("RESULT:", "ALL-BYTE-CHECKS-PASS" if not fails else f"FAILURES: {fails}")
sys.exit(0 if not fails else 1)
