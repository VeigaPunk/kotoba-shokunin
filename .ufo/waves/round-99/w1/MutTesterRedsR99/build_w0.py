#!/usr/bin/env python3
"""Build the scratch green-base control W0 in a scratch clone (not the lane).

Honest route the C2 counter admits: 8 coverage-map rows, round-81.md:8 hash
quoting, an equal-mode baseline re-record, appended GOVERNANCE_CORRECTIONS rows
with one appended LOG.md notice (all tokens double-quoted so they are not
subjects), and one INSTRUMENT_PINS admission.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

D = Path(sys.argv[1]).resolve()

# ---- 1. coverage-map rows for the eight unindexed spot-check lessons ---------
readme = D / "corpus/README.md"
lines = readme.read_text(encoding="utf-8").splitlines()
idx = next(i for i, l in enumerate(lines) if l.startswith("| Round-98 lesson |"))
rows = []
for n in range(91, 99):
    rows.append(
        "| Round-%d verifier spot-check (indexed round 99) | "
        "`lessons/round-%d-verifier-spotcheck.md` | the non-author closure of "
        "round %d, written by the hyaku closure and never edited here; indexed "
        "at round 99 so the coverage map denotes every tracked corpus file |"
        % (n, n, n))
lines[idx + 1:idx + 1] = rows
readme.write_text("\n".join(lines) + "\n", encoding="utf-8")

# ---- 2. round-81.md:8 hash quoting (the absent test-world commit) -----------
r81 = D / "corpus/lessons/round-81.md"
text = r81.read_text(encoding="utf-8")
old = "a real commit `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`"
new = "a real `commit 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`"
assert text.count(old) == 1, "round-81 anchor"
r81.write_text(text.replace(old, new), encoding="utf-8")

# ---- 3. governance corrections ---------------------------------------------
# (subject file, subject line, stale token, corrected token)
DEAD = [
    ("LOG.md", 2881, ".ufo/waves/round-82/receipts/before-tip-battery-win-dot.txt", "../.ufo/waves"),
    ("LOG.md", 2947, ".ufo/waves/round-82/receipts/before-tip-battery-win-dot.txt", "../.ufo/waves"),
    ("LOG.md", 2958, ".ufo/reports/round-82/kotoba.md", "../.ufo/reports/round-82/kotoba.md"),
    ("LOG.md", 3353, ".ufo/watchdog.log", "../.ufo/watchdog.log"),
    ("LOG.md", 3360, ".ufo/reports/round-84/kama.md", "../.ufo/reports/round-84/kama.md"),
    ("LOG.md", 3512, ".ufo/l0-questions.md", "../.ufo/l0-questions.md"),
    ("LOG.md", 3561, ".ufo/watchdog.log", "../.ufo/watchdog.log"),
    ("SCORECARD.md", 186, ".ufo/reports/round-82/kotoba.md", "../.ufo/reports/round-82/kotoba.md"),
    ("SCORECARD.md", 204, ".ufo/reports/round-83/kotoba.md", "../.ufo/reports/round-83/kotoba.md"),
    ("SCORECARD.md", 222, ".ufo/reports/round-84/kotoba.md", "../.ufo/reports/round-84/kotoba.md"),
    ("SCORECARD.md", 527, ".ufo/wapes", "../.ufo/waves"),
    ("SCORECARD.md", 529, "corpus/lessons/round-80-verifier-spotcheck.md:30,37",
     "corpus/lessons/round-80-verifier-spotcheck.md"),
    ("SCORECARD.md", 531, ".ufo/reports/round-81/kotoba.md", "../.ufo/reports/round-81/kotoba.md"),
    ("SCORECARD.md", 538, "verifiers/check_description_render.py",
     "verifiers/check_description_thresholds.py"),
    ("SCORECARD.md", 646, ".ufo/reports/round-84/kama.md", "../.ufo/reports/round-84/kama.md"),
]

log = D / "LOG.md"
log_lines = log.read_text(encoding="utf-8").splitlines()
notice_no = len(log_lines) + 1
parts = []
for sfile, sline, stale, corrected in DEAD:
    parts.append('%s:%d token "%s" -> "%s"' % (sfile, sline, stale, corrected))
notice = ("- **Round-99 C2 correction notice (scratch control; append-only).** "
          "Superseded citations corrected by this appended notice: "
          + "; ".join(parts) + ".")
assert "\n" not in notice
with log.open("a", encoding="utf-8") as fh:
    fh.write(notice + "\n")
digest = hashlib.sha256(notice.encode("utf-8")).hexdigest()

chk = D / "verifiers/verify_skill_checklist.py"
ctext = chk.read_text(encoding="utf-8")
assert ctext.count('"SCORECARD.md", 158, ".ufo/reports/round-60/kotoba.md",') == 1
ctext = ctext.replace('"SCORECARD.md", 158, ".ufo/reports/round-60/kotoba.md",',
                      '"SCORECARD.md", 161, ".ufo/reports/round-60/kotoba.md",')
block_rows = []
for sfile, sline, stale, corrected in DEAD:
    block_rows.append('    (%d,\n     "%s",\n     "%s", %d, "%s",\n     "%s"),'
                      % (notice_no, digest, sfile, sline, stale, corrected))
anchor = ")\nEMPTY_SCALARS = frozenset("
assert ctext.count(anchor) == 1
ctext = ctext.replace(anchor, "\n".join(block_rows) + "\n" + anchor)
assert ctext.count("GOVERNANCE_CORRECTIONS_HORIZON = 2723\n") == 1
ctext = ctext.replace("GOVERNANCE_CORRECTIONS_HORIZON = 2723\n",
                      "GOVERNANCE_CORRECTIONS_HORIZON = %d\n" % notice_no)
chk.write_text(ctext, encoding="utf-8")

# ---- 4. baseline equal-mode re-record --------------------------------------
proc = subprocess.run([sys.executable, "-B", "verifiers/verify_corpus_integrity.py",
                       "--no-baseline", "--json"], cwd=str(D),
                      capture_output=True, text=True)
# rc 1 is expected outside the fleet-shaped sandbox: report_dead resolves only
# through the fleet-root hop.  The three equal counts do not depend on it.
obs = json.loads(proc.stdout)
flat = obs["observed"]["corpus"]
base_path = D / "verifiers/corpus-baseline.json"
baseline = json.loads(base_path.read_text(encoding="utf-8"))
for cid, row in baseline["checks"].items():
    if row.get("mode") == "equal":
        key = cid.split(".")[-1]
        row["expect"] = flat[key]
baseline["as_of"] = "2026-11-06"
baseline["measured_against"]["head"] = "scratch-w0"
baseline["measured_against"]["note"] = (
    "Scratch green-base control (MutTesterRedsR99): equal-mode re-record only; "
    "zero expectations unchanged.")
base_path.write_text(json.dumps(baseline, indent=1, ensure_ascii=False) + "\n",
                     encoding="utf-8")

# ---- 5. INSTRUMENT_PINS admission -----------------------------------------
blob = subprocess.run(["git", "-C", str(D), "hash-object",
                       "verifiers/verify_skill_checklist.py"],
                      capture_output=True, text=True).stdout.strip()
bat = D / "verifiers/check_tip_battery.py"
btext = bat.read_text(encoding="utf-8")
pin_anchor = '    "verifiers/verify_skill_checklist.py": (\n'
assert btext.count(pin_anchor) == 1
btext = btext.replace(pin_anchor, pin_anchor + '        "%s",\n' % blob)
bat.write_text(btext, encoding="utf-8")

print("notice line", notice_no, "digest", digest)
print("checklist blob", blob)
print("baseline expects", {k: v["expect"] for k, v in baseline["checks"].items() if v.get("mode") == "equal"})
print("observed", {k: flat[k] for k in flat if not isinstance(flat[k], (list, dict))})
