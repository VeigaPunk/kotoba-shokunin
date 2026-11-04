#!/usr/bin/env python3
"""reference_scorer.py — spec-faithful reference scorer for round-85 C1 (R1..R8).

NOT a production file: this seat (MutTester) writes only under its own wave dir.
At this seat's start `verifiers/check_description_render.py` did not exist, so the
mutation battery is run against the FROZEN SPEC (plans/round-85.md § C1) using
this reference implementation. Every rule below is a literal transcription of
the plan's rule sentence; nothing is added, dropped or renamed.

  R1 first_sentence_le_99   text up to the first `.` followed by a space or end
  R2 prefix_carries_triggers first 99 chars: `skill` AND (`prompt` or `SKILL.md`),
                             case-insensitive
  R3 spec_max_1024          parsed description is 1..1024 characters
  R4 imperative_invocation  contains `use this skill when` (ci) AND literal `Triggers:`
  R5 sibling_clauses        verifiers/check_sibling_census.py <census> --province
                             PROVINCE.md --skill <skill> exits 0 and prints
                             `skill description names 10 of 10 non-none lanes`
  R6 eval_set_shape         header `label<TAB>query`; 8..10 should-trigger rows and
                             8..10 should-not-trigger rows; >=5 should-trigger rows
                             contain none of the declared trigger terms; every
                             should-not-trigger row shares >=1 lowercased
                             alphanumeric word of >=4 chars with the description
  R7 no_xml_tag             no `<` or `>` in the description
  R8 sourced_entry          knowledge file with `source:` naming S213,
                             `verified-at: 2026-11-04`, a `recheck:` value, and a
                             located quote of <= 25 words

Exit ladder: 0 all 8 rules met, 1 content fail, 2 environment error (missing or
unreadable input, census instrument missing).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

RULES = (
    "R1 first_sentence_le_99",
    "R2 prefix_carries_triggers",
    "R3 spec_max_1024",
    "R4 imperative_invocation",
    "R5 sibling_clauses",
    "R6 eval_set_shape",
    "R7 no_xml_tag",
    "R8 sourced_entry",
)
SPEC_MAX = 1024
CUT = 99
TRIGGER_RE = re.compile(r'"([^"\n]+)"')
WORD_RE = re.compile(r"[a-z0-9]+")


class EnvError(Exception):
    pass


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the YAML frontmatter subset the lane uses (`key: >` folded)."""
    if not text.startswith("---"):
        raise EnvError("no frontmatter")
    end = text.find("\n---", 3)
    if end < 0:
        raise EnvError("unterminated frontmatter")
    block = text[3:end].strip("\n").split("\n")
    out: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for line in block:
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            if key is not None:
                out[key] = "\n".join(buf).strip()
            key = m.group(1)
            val = m.group(2).strip()
            buf = [] if val in (">", "|", ">-", "|-") else [val]
        elif key is not None:
            buf.append(line.strip())
    if key is not None:
        out[key] = "\n".join(buf).strip()
    return out


def description_of(text: str) -> str:
    fm = parse_frontmatter(text)
    if "description" not in fm:
        raise EnvError("frontmatter has no description")
    return " ".join(fm["description"].split())


def first_sentence(desc: str) -> str:
    """Text up to (excluding) the first `.` followed by a space or the end.

    Anchored on the lane's own description: the plan records its first sentence
    as 150 characters, which is the exclusive reading (`desc[:i]`).
    """
    for i, ch in enumerate(desc):
        if ch == "." and (i + 1 == len(desc) or desc[i + 1] == " "):
            return desc[:i]
    return desc


def declared_terms(desc: str) -> list[str]:
    """Quoted terms inside the `Triggers:` .. `Anti-triggers:` clause."""
    i = desc.find("Triggers:")
    if i < 0:
        return []
    j = desc.find("Anti-triggers:", i)
    clause = desc[i + len("Triggers:"): j if j >= 0 else len(desc)]
    return [t.strip().lower() for t in TRIGGER_RE.findall(clause)]


def words(text: str) -> set[str]:
    return {w for w in WORD_RE.findall(text.lower()) if len(w) >= 4}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise EnvError("cannot read %s: %s" % (path, exc))


def rule_r1(desc: str) -> tuple[bool, str]:
    fs = first_sentence(desc)
    return len(fs) <= CUT, "first sentence %d chars (limit %d): %r" % (
        len(fs), CUT, fs)


def rule_r2(desc: str) -> tuple[bool, str]:
    prefix = desc[:CUT].lower()
    has_skill = "skill" in prefix
    has_domain = ("prompt" in prefix) or ("skill.md" in prefix)
    return has_skill and has_domain, "prefix has skill=%s domain=%s: %r" % (
        has_skill, has_domain, desc[:CUT])


def rule_r3(desc: str) -> tuple[bool, str]:
    return 1 <= len(desc) <= SPEC_MAX, "parsed description %d chars (limit %d)" % (
        len(desc), SPEC_MAX)


def rule_r4(desc: str) -> tuple[bool, str]:
    low = desc.lower()
    return ("use this skill when" in low) and ("Triggers:" in desc), (
        "opener=%s literal_triggers=%s" % ("use this skill when" in low,
                                           "Triggers:" in desc))


def rule_r5(skill: Path, census: Path, province: Path,
            instrument: Path = None) -> tuple[bool, str]:
    for p in (skill, census, province):
        if not p.is_file():
            raise EnvError("missing input for R5: %s" % p)
    cmd = [sys.executable, "-B", str(instrument or CENSUS_INSTRUMENT),
           str(census),
           "--province", str(province), "--skill", str(skill)]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True)
    out = proc.stdout.strip()
    want = "skill description names 10 of 10 non-none lanes"
    named = [ln for ln in out.splitlines()
             if ln.startswith("skill description names ")]
    return (proc.returncode == 0 and want in out), (
        "census exit %d; %s" % (proc.returncode, named[0] if named else
                                out.splitlines()[-1] if out else "<no output>"))


def parse_eval(path: Path) -> list[tuple[str, str]]:
    text = read_text(path)
    rows: list[tuple[str, str]] = []
    for n, line in enumerate(text.splitlines()):
        if not line.strip():
            continue
        if n == 0:
            if line != "label\tquery":
                raise EnvError("eval header is %r, want 'label<TAB>query'" % line)
            continue
        if "\t" not in line:
            raise EnvError("eval row %d has no tab: %r" % (n + 1, line))
        label, query = line.split("\t", 1)
        rows.append((label.strip(), query.strip()))
    return rows


def rule_r6(desc: str, eval_path: Path) -> tuple[bool, str]:
    rows = parse_eval(eval_path)
    pos = [q for lab, q in rows if lab == "should-trigger"]
    neg = [q for lab, q in rows if lab == "should-not-trigger"]
    other = [lab for lab, _ in rows
             if lab not in ("should-trigger", "should-not-trigger")]
    terms = declared_terms(desc)
    indirect = [q for q in pos
                if not any(t in q.lower() for t in terms)]
    dwords = words(desc)
    misses = [q for q in neg if not (words(q) & dwords)]
    ok = (not other and 8 <= len(pos) <= 10 and 8 <= len(neg) <= 10
          and len(indirect) >= 5 and not misses)
    return ok, ("should-trigger %d (indirect %d), should-not-trigger %d "
                "(near-miss misses %d), other labels %d, declared terms %d"
                % (len(pos), len(indirect), len(neg), len(misses), len(other),
                   len(terms)))


def rule_r7(desc: str) -> tuple[bool, str]:
    bad = [c for c in "<>" if c in desc]
    return not bad, "angle brackets present: %r" % "".join(bad) if bad else \
        "no `<` or `>`"


def rule_r8(knowledge: Path) -> tuple[bool, str]:
    text = read_text(knowledge)
    fields: dict[str, str] = {}
    quote = None
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if m:
            fields.setdefault(m.group(1), m.group(2).strip())
        if quote is None and re.match(r"^>\s+", line):
            quote = re.sub(r"^>\s+", "", line).strip()
        if quote is None:
            m2 = re.match(r'^quote:\s*(.+)$', line)
            if m2:
                quote = m2.group(1).strip().strip('"`')
    source = fields.get("source", "")
    verified = fields.get("verified-at", "")
    recheck = fields.get("recheck", "")
    qwords = len(quote.split()) if quote else 0
    ok = ("S213" in source.split() and verified == "2026-11-04"
          and bool(recheck) and 1 <= qwords <= 25)
    return ok, ("source=%r verified-at=%r recheck=%r quote_words=%d"
                % (source, verified, recheck, qwords))


def score(skill: Path, eval_path: Path, knowledge: Path,
          census: Path = None, province: Path = None,
          instrument: Path = None) -> tuple[int, list[dict]]:
    desc = description_of(read_text(skill))
    checks = [
        rule_r1(desc), rule_r2(desc), rule_r3(desc), rule_r4(desc),
        rule_r5(skill, census or CENSUS, province or PROVINCE, instrument),
        rule_r6(desc, eval_path),
        rule_r7(desc),
        rule_r8(knowledge),
    ]
    results = [{"rule": name, "pass": ok, "detail": detail}
               for name, (ok, detail) in zip(RULES, checks)]
    return sum(1 for r in results if r["pass"]), results


# Defaults: lane-committed instruments (read-only use).
LANE = Path(__file__).resolve().parents[5]
CENSUS = LANE / "corpus" / "knowledge" / "sibling-overlap-census-round74.md"
PROVINCE = LANE / "PROVINCE.md"
CENSUS_INSTRUMENT = LANE / "verifiers" / "check_sibling_census.py"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--skill", required=True)
    ap.add_argument("--eval", dest="eval_path", required=True)
    ap.add_argument("--knowledge", required=True)
    ap.add_argument("--census", default=str(CENSUS))
    ap.add_argument("--province", default=str(PROVINCE))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    instrument = CENSUS_INSTRUMENT
    if not instrument.is_file():
        print("ERROR census instrument missing: %s" % instrument, file=sys.stderr)
        return 2
    try:
        met, results = score(Path(args.skill), Path(args.eval_path),
                             Path(args.knowledge), Path(args.census),
                             Path(args.province), instrument)
    except EnvError as exc:
        print("ERROR %s" % exc, file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"met": met, "of": 8, "rules": results}, indent=2))
    else:
        for r in results:
            print("%s %s %s" % (r["rule"], "PASS" if r["pass"] else "FAIL",
                                r["detail"]))
        print("description render rules met %d of 8" % met)
    return 0 if met == 8 else 1


if __name__ == "__main__":
    sys.exit(main())
