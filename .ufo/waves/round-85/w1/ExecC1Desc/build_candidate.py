"""ExecC1Desc: build candidate-SKILL.md and prove parsed == candidate.

Reads the frozen candidate text from plans/round-85.md section C1 (the fenced
block after the "Candidate payload" marker), rewrites ONLY the frontmatter
description block of SKILL.md as a YAML folded scalar, preserving the file's
CRLF line endings byte-for-byte, and proves equality through
check_sibling_census.description_of() loaded via importlib.
Writes: candidate-SKILL.md + proof JSON into the wave seat dir.
"""
import importlib.util
import json
import re
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
PLAN = LANE + "/plans/round-85.md"
SKILL = LANE + "/SKILL.md"
CENSUS_VERIFIER = LANE + "/verifiers/check_sibling_census.py"
OUT_DIR = LANE + "/.ufo/waves/round-85/w1/ExecC1Desc"
OUT = OUT_DIR + "/candidate-SKILL.md"
PROOF = OUT_DIR + "/proof-parsed-equality.json"
FOLD_WIDTH = 72
INDENT = "  "

# --- 1. extract the frozen candidate text from the plan ---------------------
plan = open(PLAN, encoding="utf-8", newline="").read()
marker = plan.index("Candidate payload")
fence = plan.index("```", marker)
line_start = plan.index("\n", fence) + 1
fence_close = plan.index("\n```", line_start)
candidate = plan[line_start:fence_close]
assert "\r" not in candidate, "candidate line carries CR"
assert len(candidate) == 876, "plan says 876 parsed chars, got %d" % len(candidate)
assert "\n" not in candidate

# --- 2. read base SKILL.md as bytes-preserving text ------------------------
with open(SKILL, encoding="utf-8", newline="") as fh:
    base = fh.read()
assert base.count("\n") == base.count("\r\n"), "base is not uniformly CRLF"
EOL = "\r\n"
lines = base.split(EOL)            # every terminated line is CRLF
assert lines[0] == "---" and lines[1].startswith("name:")
close = lines.index("---", 1)      # frontmatter terminator (line 19, index 18)
desc_start = 2
assert lines[desc_start].startswith("description:")
assert lines[desc_start] == "description: >", "base description is not a folded block"
assert all(not ln.endswith("\r") for ln in lines), "stray CR after split"


def fold(text, width, indent):
    """Fold at spaces only; never break a word."""
    out, cur = [], ""
    for word in text.split(" "):
        assert word != "", "empty word (double space) in candidate"
        if not cur:
            cur = word
        elif len(indent) + len(cur) + 1 + len(word) <= width:
            cur += " " + word
        else:
            out.append(indent + cur)
            cur = word
    if cur:
        out.append(indent + cur)
    return out


folded = fold(candidate, FOLD_WIDTH, INDENT)
for ln in folded:
    assert ln[:2] == INDENT and ln.rstrip() == ln, "bad folded line"
    assert len(ln) <= FOLD_WIDTH

new_lines = lines[:desc_start] + ["description: >"] + folded + lines[close:]
# the body after the frontmatter must be byte-identical
base_tail = EOL.join(lines[close:])
cand_tail = EOL.join(new_lines[len(new_lines) - (len(lines) - close):])
assert base_tail == cand_tail, "body drifted"
candidate_text = EOL.join(new_lines)
assert candidate_text.endswith(EOL) == base.endswith(EOL)

with open(OUT, "w", encoding="utf-8", newline="") as fh:
    fh.write(candidate_text)

# --- 3. parse through the sibling census's own description_of --------------
spec = importlib.util.spec_from_file_location("check_sibling_census", CENSUS_VERIFIER)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
with open(OUT, encoding="utf-8", newline="") as fh:
    cand_read = fh.read()
parsed = mod.description_of(cand_read)

m = re.search(r".*?\.(?= |$)", parsed, re.S)
first_sentence = m.group(0) if m else parsed
low99 = parsed[:99].lower()
evidence = {
    "parsed_equals_candidate": parsed == candidate,
    "len_parsed": len(parsed),
    "len_candidate": len(candidate),
    "first_sentence_len": len(first_sentence),
    "first_sentence_le_99": len(first_sentence) <= 99,
    "repr_parsed_99": repr(parsed[:99]),
    "folded_line_count": len(folded),
    "folded_max_width": max(len(ln) for ln in folded),
    "candidate_file_uses_crlf": candidate_text.count("\n") == candidate_text.count("\r\n"),
    "body_bytes_identical": base_tail == cand_tail,
    "hand_rule_probes": {
        "R2_skill_in_first99": "skill" in low99,
        "R2_prompt_or_skillmd_in_first99": ("prompt" in low99 or "skill.md" in low99),
        "R4_use_this_skill_when": "use this skill when" in parsed.lower(),
        "R4_literal_triggers": "Triggers:" in parsed,
        "anti_triggers_present": "Anti-triggers" in parsed,
        "R7_no_angle_brackets": ("<" not in parsed and ">" not in parsed),
    },
}
with open(PROOF, "w", encoding="utf-8") as fh:
    json.dump(evidence, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print(json.dumps(evidence, indent=2, ensure_ascii=False))
ok = (
    evidence["parsed_equals_candidate"]
    and evidence["first_sentence_le_99"]
    and evidence["candidate_file_uses_crlf"]
    and evidence["body_bytes_identical"]
    and all(evidence["hand_rule_probes"].values())
)
print("BUILD-OK" if ok else "BUILD-FAIL")
sys.exit(0 if ok else 1)
