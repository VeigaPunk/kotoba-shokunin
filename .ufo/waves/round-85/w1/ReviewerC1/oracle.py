#!/usr/bin/env python3
"""Independent oracle for round-85 plan § C1 rules R1-R8.

Built from the plan text only, before reading verifiers/check_description_render.py.
Python stdlib only. Score a world = (skill text, eval fixture text|None, entry text|None,
lane cwd for R5)."""

import argparse
import os
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"


def un_crlf(text):
    return text.replace("\r\n", "\n").replace("\r", "\n")


def parse_description(skill_text):
    """Return the parsed YAML frontmatter description (folded '>' handled).

    The plan says 'parsed description'; the sibling census instrument reads the
    frontmatter description with a folded-scalar join.  Base SKILL.md uses
    `description: >` with 15 indented lines."""
    text = un_crlf(skill_text)
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise SystemExit("ENV: no frontmatter")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise SystemExit("ENV: unterminated frontmatter")
    body = lines[1:end]
    for i, line in enumerate(body):
        m = re.match(r"^description:\s*(.*)$", line)
        if not m:
            continue
        first = m.group(1).strip()
        if first in (">", "|", ">-", "|-", ">+", "|+"):
            block = body[i + 1:]
            parts = []
            for b in block:
                if b.strip() == "":
                    parts.append("")
                elif b[:1] in (" ", "\t"):
                    parts.append(b.strip())
                else:
                    break  # value ends at any column-0 line
            # folded: single newlines -> space, blank line -> newline
            out = []
            for p in parts:
                if p == "":
                    out.append("\n")
                else:
                    if out and out[-1] not in ("\n",):
                        out.append(" ")
                    elif out and out[-1] == "\n" and out[-2:-1] and out[-2] != "\n":
                        pass
                    out.append(p)
            joined = "".join(out)
            joined = re.sub(r" *\n *", "\n", joined).strip()
            return joined
        # plain scalar (possibly quoted)
        v = first
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        return v.strip()
    raise SystemExit("ENV: no description key")


def first_sentence(desc):
    """Text up to and including the first '.' followed by a space or the end."""
    for i, ch in enumerate(desc):
        if ch == "." and (i + 1 == len(desc) or desc[i + 1] == " "):
            return desc[: i + 1]
    return desc  # no terminator: the whole text is the 'sentence' up to the end


def declared_trigger_terms(desc):
    seg = desc
    m = re.search(r"Triggers:(.*?)(Anti-triggers:|$)", desc, re.S)
    if m:
        seg = m.group(1)
    return [t for t in re.findall(r'"([^"]+)"', seg)]


def parse_eval_tsv(fixture_text):
    lines = un_crlf(fixture_text).split("\n")
    rows = [l for l in lines if l.strip() != ""]
    if not rows:
        return None
    header = rows[0].split("\t")
    body = [r.split("\t") for r in rows[1:]]
    return header, body


def r6(desc, fixture_text):
    if fixture_text is None:
        return False, "fixture absent"
    parsed = parse_eval_tsv(fixture_text)
    if not parsed:
        return False, "fixture empty"
    header, body = parsed
    if header != ["label", "query"]:
        return False, "header %r != ['label','query']" % (header,)
    pos = [q for lab, q in body if lab == "should-trigger"]
    neg = [q for lab, q in body if lab == "should-not-trigger"]
    others = [lab for lab, q in body if lab not in ("should-trigger", "should-not-trigger")]
    if others:
        return False, "unknown labels %r" % (others[:3],)
    if not (8 <= len(pos) <= 10):
        return False, "should-trigger rows %d not in 8..10" % len(pos)
    if not (8 <= len(neg) <= 10):
        return False, "should-not-trigger rows %d not in 8..10" % len(neg)
    terms = [t.lower() for t in declared_trigger_terms(desc)]
    indirect = [q for q in pos if not any(t in q.lower() for t in terms)]
    if len(indirect) < 5:
        return False, "indirect positives %d < 5 (terms=%d)" % (len(indirect), len(terms))
    desc_words = set(re.findall(r"[a-z0-9]{4,}", desc.lower()))
    bad = []
    for q in neg:
        words = set(re.findall(r"[a-z0-9]{4,}", q.lower()))
        if not (words & desc_words):
            bad.append(q)
    if bad:
        return False, "negatives sharing no >=4-char word: %r" % (bad[:2],)
    return True, "pos %d neg %d indirect %d" % (len(pos), len(neg), len(indirect))


def r5(desc, skill_path):
    # The rule's instrument as the plan names it, run against a SKILL.md whose
    # frontmatter holds this world's description.
    cmd = [sys.executable, "-B", "verifiers/check_sibling_census.py",
           "corpus/knowledge/sibling-overlap-census-round74.md",
           "--province", "PROVINCE.md", "--skill", skill_path]
    p = subprocess.run(cmd, cwd=LANE, capture_output=True, text=True)
    out = p.stdout
    ok = p.returncode == 0 and "skill description names 10 of 10 non-none lanes" in out
    return ok, "exit %d :: %s" % (p.returncode, " | ".join(out.strip().split("\n")[-3:]))


def r8(entry_text):
    if entry_text is None:
        return False, "entry absent"
    t = un_crlf(entry_text)
    if not re.search(r"(?m)^source:.*S213", t):
        return False, "no 'source: ... S213'"
    if not re.search(r"(?m)^verified-at:\s*2026-11-04\s*$", t):
        return False, "no verified-at: 2026-11-04"
    if not re.search(r"(?m)^recheck:\s*\S+", t):
        return False, "no recheck value"
    qm = re.search(r'(?m)^\s*[-*]?\s*quote:\s*"?(.*?)"?\s*$', t)
    if not qm:
        return False, "no quote: line"
    quote = qm.group(1).strip().strip('"')
    if len(quote.split()) > 25 or not quote:
        return False, "quote words %d not in 1..25" % len(quote.split())
    if not re.search(r"(?mi)^\s*[-*]?\s*(location|locator|path|line|url|source-url):\s*\S+", t):
        return False, "no located marker"
    return True, "quote %d words" % len(quote.split())


def score(skill_text, fixture_text, entry_text, skill_path=None):
    desc = parse_description(skill_text)
    res = {}
    fs = first_sentence(desc)
    res["R1"] = (len(fs) <= 99, "first_sentence=%d %r" % (len(fs), fs[:60]))
    prefix = desc[:99]
    res["R2"] = (("skill" in prefix.lower()) and
                 any(x in prefix.lower() for x in ("prompt", "skill.md")),
                 "prefix_has_skill=%s prefix=%r" % ("skill" in prefix.lower(), prefix[:40]))
    res["R3"] = (1 <= len(desc) <= 1024, "len=%d" % len(desc))
    res["R4"] = ("use this skill when" in desc.lower() and "Triggers:" in desc,
                 "imperative=%s triggers=%s" % ("use this skill when" in desc.lower(),
                                                "Triggers:" in desc))
    if skill_path:
        res["R5"] = r5(desc, skill_path)
    else:
        res["R5"] = (False, "not runnable (no skill path)")
    res["R6"] = r6(desc, fixture_text)
    res["R7"] = ("<" not in desc and ">" not in desc, "lt=%s gt=%s" % ("<" in desc, ">" in desc))
    res["R8"] = r8(entry_text)
    return desc, res


def report(name, res):
    n = sum(1 for v in res.values() if v[0])
    print("== %s : %d of 8" % (name, n))
    for k in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]:
        ok, why = res[k]
        print("  %s %s :: %s" % (k, "GREEN" if ok else "RED  ", why))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scratch", required=True)
    args = ap.parse_args()
    S = args.scratch

    def git_show(rev_path):
        p = subprocess.run(["git", "show", rev_path], cwd=LANE, capture_output=True, text=True)
        return p.stdout if p.returncode == 0 else None

    base = "1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b"
    base_skill = git_show(base + ":SKILL.md")
    base_desc = parse_description(base_skill)
    print("base parsed description len", len(base_desc), "first_sentence", len(first_sentence(base_desc)))

    # Production paths state at HEAD (working tree == base for SKILL.md)
    prod_fixture = os.path.join(LANE, "verifiers/fixtures/description-eval-round85.tsv")
    prod_entry = os.path.join(LANE, "corpus/knowledge/description-trigger-discipline-round85.md")
    prod_fixture_text = open(prod_fixture, encoding="utf-8").read() if os.path.exists(prod_fixture) else None
    prod_entry_text = open(prod_entry, encoding="utf-8").read() if os.path.exists(prod_entry) else None
    print("production fixture present:", prod_fixture_text is not None)
    print("production entry present:", prod_entry_text is not None)

    # --- build a scratch SKILL.md per description world, preserving frontmatter shape
    def skill_with_desc(desc):
        return "---\nname: kotoba-shokunin\ndescription: >\n" + \
               "\n".join("  " + w for w in desc.split(" ")) + "\n---\n\nbody\n"

    def write_world(name, text):
        p = os.path.join(S, name + ".SKILL.md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(text)
        return p

    # valid fixture (claim-ready) and valid entry for the counterfactual tree
    trig = declared_trigger_terms(base_desc)  # base shares the same trigger list
    pos = ["Can you look over the instruction block I ship with my agent?",
           "Our frontmatter metadata is confusing the loader, please help.",
           "I wrote a decision table for an assistant; is it too dense?",
           "The routing paragraph for my tool is fuzzy — rewrite it.",
           "How should I describe a workflow so an assistant picks it up?",
           "My library of agent instructions has overlapping scopes, fix it.",
           "Turn this rough note into a crisp operating instruction.",
           "Does my assistant know when to activate this capability?",
           "Rewrite my tool description so the model chooses it correctly."]
    # Claim-ready negatives: topic-adjacent but out of province; each shares at
    # least one >=4-char word with the candidate description (R6 near-miss).
    neg = ["How do I prompt Claude to write marketing copy?",
           "Audit our team's prompt library for grammatical errors.",
           "Recommend a prompt template for a cooking assistant.",
           "Rewrite this SQL query to use a window function.",
           "What is a good description for an API endpoint?",
           "Should we audit our team's on-call rotation?",
           "How do I trigger a rebuild of the docs site?",
           "Explain the runtime error from this compiler.",
           "Is a method call on a null object an error?"]
    valid_fixture = "label\tquery\n" + \
        "\n".join("should-trigger\t" + q for q in pos) + "\n" + \
        "\n".join("should-not-trigger\t" + q for q in neg) + "\n"
    valid_entry = (
        "# description trigger discipline (round 85)\n\n"
        "source: S213\n"
        "verified-at: 2026-11-04\n"
        "recheck: 2027-02-04\n"
        "location: S213 § 3 (skill description guidance), row S213 in corpus/SOURCES.md\n"
        'quote: "Keep the description short, front-load the trigger words, and state when the skill should not run."\n')

    # check the valid fixture against the base desc trigger terms (sanity)
    print("trigger terms from base:", trig)

    base_skill_scratch = write_world("base", base_skill)

    candidate = (open(os.path.join(LANE, "plans/round-85.md"), encoding="utf-8")
                 .read().split("\n")[76])
    print("candidate raw line len", len(candidate))
    cand_skill = write_world("candidate", skill_with_desc(candidate))

    naive = base_desc[:99]
    naive_skill = write_world("naive99", skill_with_desc(naive))

    lanes = ["kagi", "kake", "kasegi", "kengaku", "kumitate", "chousa", "kama",
             "tameshi", "tsukuroi", "kotodama"]
    dump = ('Triggers: "skill file", "SKILL.md", "prompt craft", "write a skill", "skill quality". '
            + " ".join(lanes))
    dump_skill = write_world("tokendump", skill_with_desc(dump))

    # W5: 9 identical should-trigger rows, same valid negatives
    dup_pos = [pos[0]] * 9
    dup_fixture = "label\tquery\n" + "".join("should-trigger\t%s\n" % q for q in dup_pos) + \
        "".join("should-not-trigger\t%s\n" % q for q in neg)
    # W6: obviously irrelevant negatives, each keeping one generic >=4-char word
    irr_neg = ["Write a haiku about autumn leaves.",
               "What skill level is needed to play chess well?",
               "Write a summary of how a bill becomes a law in Canada.",
               "Which prompt was used to train this language model?",
               "How do I write a cover letter for a nursing job?",
               "What is the skill ceiling for competitive Tetris?",
               "Write a short story about a lighthouse keeper.",
               "Explain how a skill tree works in role-playing games.",
               "Prompt the user for their date of birth in a form."]
    irr_fixture = "label\tquery\n" + "".join("should-trigger\t%s\n" % q for q in pos) + \
        "".join("should-not-trigger\t%s\n" % q for q in irr_neg)

    # W7: candidate whose first 'sentence' is short only because of "e.g."
    eg_desc = candidate.replace(
        "Use this skill when auditing or rewriting a skill file or prompt.",
        "Use this skill when auditing e.g. skill files or prompts whose activation boundaries and listing descriptions require careful restructuring for more reliable discovery.")
    eg_skill = write_world("eg", skill_with_desc(eg_desc))

    worlds = [
        ("W0 base bytes @1c8f37e", base_skill, base_skill_scratch),
        ("W1 naive 99-char cut", skill_with_desc(naive), naive_skill),
        ("W2 token dump", skill_with_desc(dump), dump_skill),
        ("W-candidate (plan payload)", skill_with_desc(candidate), cand_skill),
        ("W5 eval: 9 identical should-trigger rows", skill_with_desc(candidate), cand_skill),
        ("W6 eval: irrelevant negatives w/ generic word", skill_with_desc(candidate), cand_skill),
        ("W7 description: 'e.g.' short first sentence", skill_with_desc(eg_desc), eg_skill),
    ]

    print("\n########## TABLE A: actual tree now (R6/R8 = production files as they are) ##########")
    for name, skill_text, skill_path in worlds:
        fx = {"W5": dup_fixture, "W6": irr_fixture}.get(name.split()[0], prod_fixture_text)
        _, res = score(skill_text, fx, prod_entry_text, skill_path)
        report(name, res)

    print("\n########## TABLE B: counterfactual claim-ready tree (valid fixture + valid R8 entry) ##########")
    for name, skill_text, skill_path in worlds:
        fx = {"W5": dup_fixture, "W6": irr_fixture}.get(name.split()[0], valid_fixture)
        _, res = score(skill_text, fx, valid_entry, skill_path)
        report(name, res)


    # Save world files for later counter-vs-oracle comparison
    with open(os.path.join(S, "worlds.json"), "w", encoding="utf-8") as fh:
        import json
        json.dump({n: {"skill": sp} for n, _, sp in worlds}, fh, indent=1)
    print("\nworld files in", S)


if __name__ == "__main__":
    main()
