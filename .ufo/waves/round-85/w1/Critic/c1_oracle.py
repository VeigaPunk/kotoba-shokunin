#!/usr/bin/env python3
"""Independent C1 oracle for round-85 plan rules R1-R8 (Critic seat).

The frozen production counter (verifiers/check_description_render.py) does not
exist at the freeze commit, so this oracle implements the plan text literally.

Usage:
  python3 -B c1_oracle.py --repo <world>            # score a world tree
  python3 -B c1_oracle.py --repo <world> --json

Exit ladder: 0 iff all 8 rules pass; 1 content fail; 2 environment error.
Prints `description render rules met N of 8` exactly.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

RULE_IDS = [
    "R1 first_sentence_le_99",
    "R2 prefix_carries_triggers",
    "R3 spec_max_1024",
    "R4 imperative_invocation",
    "R5 sibling_clauses",
    "R6 eval_set_shape",
    "R7 no_xml_tag",
    "R8 sourced_entry",
]

EVAL_REL = "verifiers/fixtures/description-eval-round85.tsv"
ENTRY_REL = "corpus/knowledge/description-trigger-discipline-round85.md"
CENSUS_REL = "corpus/knowledge/sibling-overlap-census-round74.md"
QUOTE_MAX_WORDS = 25


def parse_description(text: str) -> str:
    """YAML frontmatter `description` as the loader would read it.

    Handles the inline form and the folded (`>`) / literal (`|`) block forms
    used by this lane. Folded blocks join stripped lines with one space;
    literal blocks join with newlines.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("no YAML frontmatter")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError("unterminated YAML frontmatter")
    fm = lines[1:end]
    for i, line in enumerate(fm):
        m = re.match(r"^description:\s*(.*)$", line)
        if not m:
            continue
        head = m.group(1).strip()
        if head and head not in (">", ">-", "|", "|-"):
            return head
        folded = not head.startswith("|")
        block = []
        for nxt in fm[i + 1:]:
            if nxt.strip() == "":
                block.append("")
                continue
            if not nxt.startswith((" ", "\t")):
                break
            block.append(nxt.strip())
        while block and block[-1] == "":
            block.pop()
        return (" " if folded else "\n").join(block)
    raise ValueError("no description key")


def first_sentence(text: str) -> str:
    for i, ch in enumerate(text):
        if ch == "." and (i + 1 == len(text) or text[i + 1] == " "):
            return text[: i + 1]
    return text


def declared_trigger_terms(desc: str) -> list[str]:
    """Quoted terms inside the `Triggers:` clause (case-folded)."""
    m = re.search(r"Triggers:(.*?)(?:Anti-triggers:|$)", desc, re.DOTALL)
    if not m:
        return []
    return [t.lower() for t in re.findall(r'"([^"]+)"', m.group(1))]


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def r1(desc, repo):
    sent = first_sentence(desc)
    return len(sent) <= 99, "first sentence %d chars: %r" % (len(sent), sent)


def r2(desc, repo):
    prefix = desc[:99]
    low = prefix.lower()
    ok = "skill" in low and ("prompt" in low or "skill.md" in low)
    return ok, "prefix 99 chars: %r" % prefix


def r3(desc, repo):
    return 1 <= len(desc) <= 1024, "description length %d (1..1024)" % len(desc)


def r4(desc, repo):
    ok = "use this skill when" in desc.lower() and "Triggers:" in desc
    return ok, "imperative=%s literal-triggers=%s" % (
        "use this skill when" in desc.lower(), "Triggers:" in desc)


def r5(desc, repo):
    cmd = [sys.executable, "-B", "verifiers/check_sibling_census.py",
           CENSUS_REL, "--province", "PROVINCE.md", "--skill", "SKILL.md"]
    proc = subprocess.run(cmd, cwd=str(repo), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True)
    out = proc.stdout
    needle = "skill description names 10 of 10 non-none lanes"
    ok = proc.returncode == 0 and needle in out
    detail = "exit %d; %s" % (proc.returncode,
                              [ln for ln in out.splitlines()
                               if ln.startswith("skill description")])
    if not ok and proc.stderr:
        detail += "; stderr: " + proc.stderr.strip().splitlines()[0][:160]
    return ok, detail


def r6(desc, repo):
    path = repo / EVAL_REL
    if not path.is_file():
        return False, "missing %s" % EVAL_REL
    raw = path.read_text()
    lines = raw.splitlines()
    if not lines or lines[0] != "label\tquery":
        return False, "header is not exactly 'label<TAB>query': %r" % (
            lines[0] if lines else "")
    pos, neg, malformed = [], [], []
    for line in lines[1:]:
        if not line.strip():
            continue
        cells = line.split("\t")
        if len(cells) != 2:
            malformed.append(line)
            continue
        if cells[0] == "should-trigger":
            pos.append(cells[1])
        elif cells[0] == "should-not-trigger":
            neg.append(cells[1])
        else:
            malformed.append(line)
    terms = declared_trigger_terms(desc)
    indirect = [q for q in pos
                if not any(t in q.lower() for t in terms)]
    desc_words = {w for w in words(desc) if len(w) >= 4}
    near_miss = [q for q in neg if desc_words & set(words(q))]
    problems = []
    if malformed:
        problems.append("%d malformed row(s)" % len(malformed))
    if not 8 <= len(pos) <= 10:
        problems.append("should-trigger rows %d not in 8..10" % len(pos))
    if not 8 <= len(neg) <= 10:
        problems.append("should-not-trigger rows %d not in 8..10" % len(neg))
    if len(indirect) < 5:
        problems.append("indirect positives %d < 5 (terms=%s)" % (
            len(indirect), terms))
    if len(near_miss) != len(neg):
        problems.append("near-miss negatives %d of %d" % (
            len(near_miss), len(neg)))
    detail = ("pos %d (indirect %d), neg %d (near-miss %d), terms %d"
              % (len(pos), len(indirect), len(neg), len(near_miss), len(terms)))
    if problems:
        detail += "; " + "; ".join(problems)
    return not problems, detail


def r7(desc, repo):
    ok = "<" not in desc and ">" not in desc
    return ok, "xml-angle=%s" % (not ok)


def r8(desc, repo):
    path = repo / ENTRY_REL
    if not path.is_file():
        return False, "missing %s" % ENTRY_REL
    text = path.read_text()
    fields = {}
    quote = None
    for line in text.splitlines():
        m = re.match(r"^(source|verified-at|recheck|quote|locator):\s*(.*)$", line)
        if m:
            fields.setdefault(m.group(1), m.group(2).strip())
            if m.group(1) == "quote":
                quote = m.group(2).strip()
    problems = []
    if "S213" not in fields.get("source", ""):
        problems.append("source does not name S213")
    if "2026-11-04" not in fields.get("verified-at", ""):
        problems.append("verified-at is not 2026-11-04")
    if not fields.get("recheck"):
        problems.append("recheck missing")
    if not fields.get("locator"):
        problems.append("quote locator missing")
    if quote is None:
        problems.append("quote missing")
    elif not 1 <= len(quote.split()) <= QUOTE_MAX_WORDS:
        problems.append("quote %d words > %d" % (len(quote.split()),
                                                 QUOTE_MAX_WORDS))
    return not problems, "; ".join(problems) or "entry fields complete"


RULES = [r1, r2, r3, r4, r5, r6, r7, r8]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    skill = repo / "SKILL.md"
    try:
        desc = parse_description(skill.read_text())
    except (OSError, ValueError) as exc:
        print("ERROR %s: %s" % (skill, exc), file=sys.stderr)
        return 2
    results = []
    for rid, fn in zip(RULE_IDS, RULES):
        try:
            ok, detail = fn(desc, repo)
        except Exception as exc:  # oracle defect, not a world verdict
            print("ERROR %s: %s" % (rid, exc), file=sys.stderr)
            return 2
        results.append({"rule": rid, "pass": bool(ok), "detail": detail})
    met = sum(1 for r in results if r["pass"])
    if args.json:
        print(json.dumps({"met": met, "of": 8, "description_length": len(desc),
                          "rules": results}, indent=1))
    else:
        for r in results:
            print("%s %s  %s" % ("PASS" if r["pass"] else "FAIL", r["rule"],
                                 r["detail"]))
        print("description render rules met %d of 8" % met)
    return 0 if met == 8 else 1


if __name__ == "__main__":
    sys.exit(main())
