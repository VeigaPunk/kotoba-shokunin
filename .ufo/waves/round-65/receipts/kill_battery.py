# Round-65 C1 kill battery — run against a git-archive EXTRACTION of the measured rev,
# never the live lane tree (the harness writes the candidate file in place).
# Usage: git archive <rev> | tar -x -C /tmp/tree && cd /tmp/tree && python3 kill_battery.py

#!/usr/bin/env python3
"""Round-65 C1 kill battery: every named lane must die by its pin arm on the
candidate bytes; semantics-preserving equivalents must survive; the four
new-arm mutants must survive the pkg7-equivalent control world (candidate
minus the four round-65-new arms)."""
import subprocess, sys
from pathlib import Path

TREE = Path('/tmp/r65work/tree')
CAND = TREE / 'check_scoped_rules_v32.py'
BASE = CAND.read_text()

SPAN_BLOCK = '''    span_missing = sorted({
        word
        for span in BACKTICK_RE.findall(cell)
        for word in span.split()
        if len(word) >= 4 and word.lower() not in STOPWORDS
        and word.lower() not in content_words(raw_line)
        and not supported(word.lower(), page_words(raw_page))})'''

MUTANTS = {
    # lane: (old, new) -- one exact-string replacement
    "SM1-span-empty": (SPAN_BLOCK, "    span_missing = []"),
    "SM2-floor2": ("len(word) >= 4", "len(word) >= 2"),
    "SM3-no-stopword": ("word.lower() not in STOPWORDS", "True"),
    "SM4-no-page-check": ("and not supported(word.lower(), page_words(raw_page))", ""),
    "SM5-no-line-check": ("and word.lower() not in content_words(raw_line)", ""),
    "SM6-always-fires": ("if span_missing:", "if True:"),
    "M7-floor3": ("len(word) >= 4", "len(word) >= 3"),
    "M8-floor5": ("len(word) >= 4", "len(word) >= 5"),
    "M9-stopword-no-lower": ("word.lower() not in STOPWORDS", "word not in STOPWORDS"),
    "M10-line-no-lower": ("word.lower() not in content_words(raw_line)", "word not in content_words(raw_line)"),
    "M12-line-page-words": ("content_words(raw_line)", "page_words(raw_line)"),
    "M17-exact-page": ("supported(word.lower(), page_words(raw_page))", "word.lower() in page_words(raw_page)"),
    "M14-wrapper-no-page": ('raw_page = page_text if page_text is not None else "\\n".join(lines)', 'raw_page = "\\n".join(lines)'),
    "SPAN_FIRST": ("for span in BACKTICK_RE.findall(cell)", "for span in BACKTICK_RE.findall(cell)[:1]"),
    "SPAN_LAST": ("for span in BACKTICK_RE.findall(cell)", "for span in BACKTICK_RE.findall(cell)[-1:]"),
    "M20-page-content-words": ("page_words(raw_page)", "content_words(raw_page)"),
    "M11-page-no-lower": ('t = CITE_RE.sub(" ", text)\n    return {w for w in CONTENT_RE.findall(t.lower()) if w not in STOPWORDS}',
                          't = CITE_RE.sub(" ", text)\n    return {w for w in CONTENT_RE.findall(t) if w not in STOPWORDS}'),
}
KILLED_BY = {
    "SM1-span-empty": "a backticked span whose words occur in neither",
    "SM2-floor2": "a backticked span word shorter than four characters",
    "SM3-no-stopword": "a backticked span made only of stopwords",
    "SM4-no-page-check": None,  # attribution: first killer is the M17 arm, then eligible-world lines
    "SM5-no-line-check": "a backticked span word present in the cited line is",
    "SM6-always-fires": None,  # attribution: pre-existing A2 cell arm (R64-M9 rule)
    "M7-floor3": "a three-character span word is not rejected",
    "M8-floor5": "a fabricated four-character span word is rejected",
    "M9-stopword-no-lower": "a capitalised stopword-only span is not rejected",
    "M10-line-no-lower": "a capitalised span word present in the cited line is",
    "M12-line-page-words": "a span word present in the cited line only inside",
    "M17-exact-page": "a span word supported by a four-character prefix",
    "M14-wrapper-no-page": "a span word present in the cited line only inside",
    "SPAN_FIRST": "a fabricated second backticked span is rejected",
    "SPAN_LAST": "a fabricated first backticked span is rejected",
    "M20-page-content-words": "a span word whose only page occurrence is inside",
    "M11-page-no-lower": "a capitalised span word present on the page only as an",
}
SURVIVE = ["M19-sorted-list", "M22-L-guard"]

def run(src: str, label: str):
    CAND.write_text(src)
    try:
        p = subprocess.run([sys.executable, "-B", "check_scoped_rules_v32.py", "--self-test"],
                           cwd=TREE, capture_output=True, text=True, timeout=180)
    finally:
        CAND.write_text(BASE)
    out = p.stdout + p.stderr
    fails = [l for l in out.splitlines() if "FAIL" in l or "failure(s)" in l]
    count = [l for l in out.splitlines() if "failure(s) over" in l]
    print(f"== {label}: exit={p.returncode}  {count[-1] if count else 'NO COUNT'}")
    for l in fails[:4]:
        print(f"   {l[:150]}")
    return p.returncode, out

ok = True
print("# candidate baseline")
rc, _ = run(BASE, "baseline")
assert rc == 0

print("\n# kill set (each must exit 1, attributed to its arm)")
for lane, (old, new) in MUTANTS.items():
    assert BASE.count(old) == 1, (lane, BASE.count(old))
    rc, out = run(BASE.replace(old, new), lane)
    want = KILLED_BY[lane]
    if rc != 1:
        print(f"   !! {lane} SURVIVED (exit {rc})"); ok = False; continue
    if want and want not in out:
        print(f"   !! {lane} killed but NOT by its arm label ({want!r})"); ok = False

print("\n# equivalents (must exit 0 on the candidate)")
rc, _ = run(BASE.replace("span_missing = sorted({", "span_missing = list({"), "M19-sorted-list")
if rc != 0: print("   !! M19 died"); ok = False
rc, _ = run(BASE.replace("if L is None or L < 1 or L > len(lines):", "if L is None or L > len(lines):"), "M22-L-guard")
if rc != 0: print("   !! M22 died"); ok = False

print("\n# control world: pkg7-equivalent (candidate minus the 4 round-65-new arms)")
marker = '        check("A2 G7: a fabricated first backticked span is rejected'
tail_marker = '        check("A2 G9: an `and`-joined purpose clause off the cited line is rejected",'
head, rest = BASE.split(marker, 1)
_, tail = rest.split(tail_marker, 1)
CTRL = head + tail_marker + tail
rc, _ = run(CTRL, "pkg7-control")
NEW_ARM_LABELS = ["a fabricated first backticked span", "a fabricated second backticked span",
                  "a span word whose only page occurrence", "a capitalised span word present on the page only"]
# load-bearing pins: must SURVIVE the pkg7 control world (killed only by the new arms)
for lane in ["SPAN_FIRST", "SPAN_LAST", "M20-page-content-words"]:
    old, new = MUTANTS[lane]
    if CTRL.count(old) != 1:
        print(f"   !! control world lacks unique target for {lane}"); ok = False; continue
    rc, out = run(CTRL.replace(old, new), f"control+{lane}")
    if rc != 0:
        print(f"   !! {lane} died in the control world -- the new arm is not the load-bearing pin"); ok = False
# M11: pinned by pre-existing main-world collateral in EVERY world (MutW2M7M22 F7);
# the new M11 arm is a named witness, never the first kill.  Control expectation:
# killed there with NO new-arm label among the FAILs.
old, new = MUTANTS["M11-page-no-lower"]
rc, out = run(CTRL.replace(old, new), "control+M11-page-no-lower")
if rc == 0:
    print("   !! M11 survived the control world -- F7 attribution broken"); ok = False
elif any(lbl in out for lbl in NEW_ARM_LABELS):
    print("   !! M11 control-world kill carries a new-arm label -- attribution broken"); ok = False

print("\nRESULT:", "ALL OK" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)
