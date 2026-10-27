#!/usr/bin/env python3
"""R02RevAudit-script.py -- independent recompute of the C1 self-audit numbers.

Seat R02RevAudit, kotoba round 77 w1. This script shares no code with
verifiers/check_desc_craft.py (that counter hand-rolls the block-scalar
render; this script parses the frontmatter with yaml.safe_load, PyYAML) and
re-derives every audit field the C1 entry draft states.

Usage: python3 -B R02RevAudit-script.py [path/to/SKILL.md]
Exit 0 when every recomputed value equals the entry's stated value, else 1.
"""
import hashlib
import re
import sys

import yaml

CLAIMED = {
    "clip_len": 1022,
    "stripped_len": 1021,
    "first_sentence_incl_period": 151,
    "first_sentence_excl_period": 150,
    "quoted_trigger_phrases": 8,
    "quoted_span_chars_bare": 108,
    "sentence_count": 7,
    "fm_block_line_range": (4, 18),
    "anti_trigger_categories": 3,
}

def anti_categories(desc: str):
    m = re.search(r"Anti-triggers: (.*?)\. ", desc, re.S)
    if not m:
        return []
    clause = m.group(1)
    cats, depth, cur = [], 0, []
    for ch in clause:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            cats.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur:
        cats.append("".join(cur).strip())
    return cats

def main(path: str) -> int:
    raw = open(path, encoding="utf-8").read()
    print(f"file: {path}")
    print(f"sha256: {hashlib.sha256(raw.encode()).hexdigest()}")
    print(f"bytes: {len(raw.encode())}  chars: {len(raw)}")

    lines = raw.split("\n")
    assert lines[0] == "---", "SKILL.md does not open with '---'"
    close_at = lines.index("---", 1)  # 0-based index of closing delimiter
    # Keep the source line break immediately before closing '---': YAML clip
    # chomping retains this terminal line break in the scalar value.
    fm_text = "\n".join(lines[1:close_at]) + "\n"
    doc = yaml.safe_load(fm_text)
    desc = doc["description"]
    assert isinstance(desc, str), "description is not a plain string render"

    desc_key_at = next(i for i, l in enumerate(lines, 1) if l.startswith("description:"))
    block = (desc_key_at + 1, close_at)  # 1-based inclusive content lines
    block_n = block[1] - block[0] + 1

    clip_len = len(desc)
    stripped_len = len(desc.strip())
    collapsed_len = len(re.sub(r"\s+", " ", desc).strip())
    idx = desc.find(". ")
    first_incl = idx + 1 if idx >= 0 else clip_len
    first_excl = idx if idx >= 0 else clip_len

    quotes = re.findall(r'"([^"]+)"', desc)
    span_bare = sum(len(q) for q in quotes)
    span_marked = sum(len(q) + 2 for q in quotes)
    parts = re.split(r"(?<=\.) ", desc)
    sentences = [p.strip() for p in parts if p.strip()]
    boundaries = [
        (m.start(), desc[max(0, m.start() - 18):m.start()].replace("\n", "\\n"),
         desc[m.start():m.start() + 20].replace("\n", "\\n"))
        for m in re.finditer(r"\. ", desc)
    ]
    cats = anti_categories(desc)

    # Independent physical-line fold check: all content lines have the same
    # two-space indentation and no blank lines, so joining their contents with
    # spaces and the clip-preserving final newline must reproduce YAML's value.
    body_lines = lines[desc_key_at:close_at]
    naive_render = " ".join(l[2:] for l in body_lines) + "\n"
    fold_agrees = naive_render == desc

    print("\n== measured (yaml.safe_load, clip-preserving) ==")
    print(f"description key line (1-based):        {desc_key_at}")
    print(f"frontmatter block line range:          {block[0]}-{block[1]}  ({block_n} physical lines)")
    print(f"clip render length:                    {clip_len}")
    print(f"stripped render length:                {stripped_len}")
    print(f"whitespace-collapsed length:           {collapsed_len}")
    print(f"first sentence incl period:            {first_incl}")
    print(f"first sentence excl period:            {first_excl}")
    print(f"quoted trigger phrases:                {len(quotes)}")
    print(f"quoted span (chars inside quotes):     {span_bare}")
    print(f"quoted span (incl the quote marks):    {span_marked}")
    print(f"sentence count ('. ' segments):        {len(sentences)}")
    print(f"anti-trigger categories:               {len(cats)}")
    print(f"headroom under 1024 (clip):            {1024 - clip_len}")
    print(f"trivial fold == yaml.safe_load fold:   {fold_agrees}")
    print("\n== quoted phrases (len, phrase) ==")
    for q in quotes:
        print(f"  {len(q):>3}  \"{q}\"")
    print("\n== sentences (len, first 60 chars) ==")
    for s in sentences:
        print(f"  {len(s):>4}  {s[:60].replace(chr(10), ' ')}...")
    print("\n== '. ' boundaries (offset, before, after) ==")
    for off, before, after in boundaries:
        print(f"  @{off:>4}  ...{before}|{after}...")
    print("\n== anti-trigger categories ==")
    for c in cats:
        print(f"  - {c}")

    recomputed = {
        "clip_len": clip_len,
        "stripped_len": stripped_len,
        "first_sentence_incl_period": first_incl,
        "first_sentence_excl_period": first_excl,
        "quoted_trigger_phrases": len(quotes),
        "quoted_span_chars_bare": span_bare,
        "sentence_count": len(sentences),
        "fm_block_line_range": block,
        "anti_trigger_categories": len(cats),
    }
    print("\n== claimed (entry draft) vs recomputed ==")
    ok = fold_agrees
    for k, want in CLAIMED.items():
        got = recomputed[k]
        match = got == want
        ok &= match
        print(f"  {'PASS' if match else 'FAIL'}  {k}: entry={want} recomputed={got}")
    print(f"\nALL-MATCH: {ok}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1
                  else "/home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md"))
