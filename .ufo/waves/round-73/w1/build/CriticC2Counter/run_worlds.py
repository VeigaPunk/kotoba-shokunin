#!/usr/bin/env python3
"""Build C2 worlds and walk R1-R3 on each (CriticC2Counter, round 73 wave 1).

R1/R2 are the frozen predicate read literally (eval_c2.py).  R3 is evaluated
by copying the world's SKILL.md into the fleet-shaped sandbox clone of the
base rev and running the tree's own check_sibling_census.py.
"""
import re
import subprocess
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from eval_c2 import base_description, r1, r2, render  # noqa: E402

BUILD = Path(__file__).parent
SANDBOX = Path(open("/tmp/k73w1-CriticC2Counter.path").read().strip()) / "kotoba-shokunin"
NOTE = " Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router \u2014 craft here is audit-side."


def worlds(D):
    out = {}
    out["BASE"] = D
    trig = D[D.index("Triggers:"):]

    # W1: first sentence is a quoted trigger list only.
    first = '"skill file", "prompt craft", "audit this skill", "skill quality" are prompt-craft triggers'
    out["W1_QUOTELIST"] = first + ". " + trig

    # W2: first sentence obeys R1/R2; domain statement moved past offset 99.
    first = 'Skill and prompt craft for "skill file" authors'
    out["W2_DOMAIN_EVICTED"] = first + ". Audits " + D[D.index("SKILL.md"):]

    # W3: the cheapest punctuation world -- base + 3 inserted characters; the
    # old 150-char sentence continues after the inserted period.
    out["W3_PUNCT_MIN"] = D.replace("and rewrites SKILL.md", 'and rewrites. SKILL.md "SKILL.md"', 1)
    # W3b: the same punctuation trick, trimmed under the byte cap by deleting
    # 24 chars of domain text.
    out["W3B_PUNCT_TRIMMED"] = out["W3_PUNCT_MIN"].replace(
        " for trigger fidelity and decision density", " for trigger fidelity", 1)

    # W4: one quoted trigger repeated until the window is stuffed.
    out["W4_STUFFED"] = '"skill file" ' * 6 + 'skill prompt. ' + trig

    # W5: the Triggers list shortened to one string, which R2 then uses.
    out["W5_TRIGGERS_SHRUNK"] = (
        'Skill and prompt craft for "skill file" authors. Audits ' + D[D.index("SKILL.md"):]
    ).replace(D[D.index("Triggers:"):D.index("Anti-triggers:")], 'Triggers: "skill file". ', 1)

    # W6: no uppercase sentence boundary anywhere -> R1 falls back to the
    # first 99 characters (length 99, so it always passes).
    w6 = D.replace("rewrites SKILL.md /", 'rewrites "SKILL.md" /', 1)
    w6 = w6.replace("density. Triggers:", "density; Triggers:")
    w6 = w6.replace('"skill quality". Anti-triggers:', '"skill quality"; Anti-triggers:')
    w6 = w6.replace("tree. Sibling boundary:", "tree; sibling boundary:")
    w6 = w6.replace("method. NOT kotodama", "method; not kotodama")
    w6 = w6.replace("name. Note:", "name; note:")
    assert not re.search(r"[.:] (?=[A-Z])", w6)
    out["W6_FALLBACK_VACUOUS"] = w6

    # W7: the quoted trigger sits after the first sentence -- R2's 99-char
    # window sees it, the truncator's first-sentence render does not.
    out["W7_TRIGGER_AFTER_FS"] = ('Prompt and skill craft \u2014 audits, writes, and rewrites SKILL.md. '
                                  + trig)

    # W8: first sentence exactly 99 chars (terminal period at offset 99, i.e.
    # outside the truncator's slice(0,99)); Note clause removed to stay <=1024.
    f8 = ('Skill and prompt craft for "skill file" authors who audit and rewrite skill files'
          ' with care and craft for routing')[:99]
    assert len(f8) == 99 and "." not in f8
    out["W8_BOUND_99"] = f8 + ". Audits " + D[D.index("SKILL.md"):].replace(NOTE, "", 1)

    # W9: R2 alone is free -- add only the quote pair, leave the sentence.
    out["W9_QUOTE_ONLY"] = D.replace("rewrites SKILL.md", 'rewrites "SKILL.md"', 1)

    # Shortcut controls, rebuilt so the whole 99-char window is controlled.
    f1 = "Skill and prompt craft for audit and rewrite work done with care and craft for daily use"
    while len(f1) < 99:
        f1 += " now" if len(f1) + 4 <= 99 else "x"
    assert len(f1) == 99 and '"' not in f1, (len(f1), f1)
    out["S1_NOQUOTE"] = f1 + ". " + trig
    # S1a: a quote-free FIRST SENTENCE of 59 chars, with a trigger quote at
    # offset ~70 -- the addendum's control wording does not exclude this.
    out["S1A_QUOTE_AFTER_FS"] = "Skill and prompt craft for audit and rewrite work done well. " + trig
    out["S6_COLON"] = 'Skill and prompt craft: audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts "skill file". ' + D[D.index("Anti-triggers:"):]
    out["S2_UNDER40"] = "Skill and prompt craft. " + trig
    f3 = 'Skill and prompt craft for "random phrase" authors who audit and rewrite skill files daily'
    out["S3_NOTINLIST"] = f3 + ". " + trig
    out["S4_CUT99"] = 'Skill and prompt craft for "skill file" authors.'
    out["S5_OVER1024"] = D + " filler" * 5
    return out


def skill_md(D):
    wrapped = textwrap.fill(D, width=84, initial_indent="  ", subsequent_indent="  ",
                            break_on_hyphens=False, break_long_words=False)
    return "---\nname: kotoba-shokunin\ndescription: >\n%s\n---\n\nbody\n" % wrapped


def gate(D):
    (SANDBOX / "SKILL.md").write_text(skill_md(D))
    p = subprocess.run(
        ["python3", "-B", "verifiers/check_sibling_census.py",
         "corpus/knowledge/sibling-overlap-census-round49.md",
         "--province", "PROVINCE.md", "--skill", "SKILL.md"],
        cwd=SANDBOX, capture_output=True, text=True)
    tail = [l for l in p.stdout.splitlines() if l.startswith(("skill description", "rows"))]
    return p.returncode, tail


def main():
    D = base_description()
    print("base D len", len(D))
    results = {}
    for name, W in worlds(D).items():
        b, fs, ok1 = r1(W)
        words, quotes, hits, ok2 = r2(W)
        rc, tail = gate(W)
        ok3 = rc == 0 and len(W) <= 1024
        r = render(W)
        (BUILD / "worlds").mkdir(exist_ok=True)
        (BUILD / "worlds" / (name + ".description.txt")).write_text(W + "\n")
        results[name] = (sum([ok1, ok2, ok3]), len(W))
        print("== %-20s N=%d len=%d R1=%s fslen=%s R2=%s R3=%s" %
              (name, sum([ok1, ok2, ok3]), len(W), ok1, len(fs), ok2, ok3))
        print("   fs     : %r" % fs)
        print("   render : %r" % r)
        print("   gate   : exit=%d %s" % (rc, " | ".join(tail)))
    print()
    print("3-of-3 worlds:", [k for k, v in results.items() if v[0] == 3])
    # frontmatter line delta for the cheapest 3/3 world
    (SANDBOX / "SKILL.md").write_text(skill_md(worlds(D)["W3_PUNCT_MIN"]))
    fm = (SANDBOX / "SKILL.md").read_text().split("\n---", 1)[0].count("\n") + 1
    base_fm = 19
    print("W3 frontmatter lines: %d (base %d, delta %+d) -> body citations shift %+d"
          % (fm, base_fm, fm - base_fm, base_fm - fm))
    subprocess.run(["git", "-C", str(SANDBOX), "checkout", "-q", "--", "SKILL.md"])


if __name__ == "__main__":
    main()
