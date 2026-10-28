#!/usr/bin/env python3
"""Kb80S11GateQuotes — verification of the S232+ rejection/queued row quotes
against the pages this seat fetched itself (2026-10-27, curl 8.23.0).

Bodies: /fast/scratch/hyaku/kotoba-r80/Kb80S11GateQuotes/<slug>.html|.md
(the same bytes copied as Kb80S11GateQuotes-<slug>.* into round-80/build/).

HTML view: script/style removed, tags -> one space (with a raw-offset map),
entities decoded; then every whitespace run collapsed, empty lines dropped.
Plain markdown: whitespace collapsed only. Every reported raw offset is a byte
offset into the fetched body; line numbers are 1-based raw lines.
"""
import hashlib
import json
import re
import sys
from html import unescape

SCRATCH = "/fast/scratch/hyaku/kotoba-r80/Kb80S11GateQuotes"
ROWS = [
    ("S232", "cline", "https://docs.cline.bot/customization/skills", "html",
     "Metadata Always (at startup) ~100 tokens per skill name and description from YAML frontmatter",
     "ef602792f4d2074678eadcd39f1d506d604dbed4bbee69df05865792e6c57fdc"),
    ("S233", "windsurf", "https://docs.windsurf.com/windsurf/cascade/skills", "html",
     "name : Unique identifier for the skill (displayed in UI and used for @-mentions) description : Brief explanation shown to the model",
     "a7e33f3a12363a33fd96e26e6a26e1d1f412dfc1c2a18d2715eb64f22f7cb85b"),
    ("S234", "langchain", "https://docs.langchain.com/oss/python/deepagents/skills", "html",
     "They are unrelated to the spec\u2019s allowed-tools field, which pre-approves tools rather than adding them",
     "dfaa7d2bd9a1fabf245bdc9e4b2a61a4ea2bf002a9de497cbae3d945c5ad6b52"),
    ("S235", "issue", "https://github.com/anthropics/claude-code/issues/18737", "html",
     "The allowed-tools frontmatter field in SKILL.md is only supported when using Claude Code CLI directly.",
     "7774040f99f84da2b9f26ab7dc0c78973388c84e9e11eabf041a51e2b8c15688"),
    ("S236", "agentsdk", "https://code.claude.com/docs/en/agent-sdk/skills.md", "md",
     "In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's allowed-tools frontmatter or with the allowedTools option",
     "ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2"),
    ("S236b", "agentsdk", "https://code.claude.com/docs/en/agent-sdk/skills.md", "md",
     "The list pre-approves the named tools rather than restricting the others.",
     "ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2"),
]


def build_view(raw, kind):
    """(collapsed text, per-char raw index) for the declared view."""
    if kind == "md":
        chars = list(raw)
        idx = list(range(len(raw)))
    else:
        chars, idx = [], []
        i, n = 0, len(raw)
        while i < n:
            if raw.startswith("<!--", i):
                j = raw.find("-->", i)
                i = n if j < 0 else j + 3
                continue
            if raw[i] == "<":
                m = re.match(r"(?is)<(script|style)\b.*?</\1\s*>", raw[i:])
                if m:
                    i += m.end()
                    continue
                j = raw.find(">", i)
                if j < 0:
                    break
                chars.append(" ")
                idx.append(i)
                i = j + 1
                continue
            chars.append(raw[i])
            idx.append(i)
            i += 1
    text = unescape("".join(chars))
    # collapse whitespace; map each kept char to the raw index of its source
    out_c, out_i = [], []
    n = len(text)
    p = 0
    while p < n:
        if text[p].isspace():
            q = p
            while q < n and text[q].isspace():
                q += 1
            if out_c:
                out_c.append(" ")
                out_i.append(idx[min(p, len(idx) - 1)])
            p = q
            continue
        out_c.append(text[p])
        out_i.append(idx[min(p, len(idx) - 1)])
        p += 1
    return "".join(out_c), out_i


def raw_line(raw, off):
    return raw.count("\n", 0, off) + 1


def main():
    out = []
    for rid, slug, url, kind, quote, s05_sha in ROWS:
        path = f"{SCRATCH}/{slug}.{kind}"
        data = open(path, "rb").read()
        raw = data.decode("utf-8", "replace")
        sha = hashlib.sha256(data).hexdigest()
        view, vmap = build_view(raw, kind)
        q = " ".join(quote.split())
        count = view.count(q)
        pos = view.find(q)
        rec = dict(id=rid, slug=slug, url=url, bytes=len(data), sha256=sha,
                   s05_sha=s05_sha, sha_matches_s05=(sha == s05_sha),
                   quote=quote, words=len(q.split()),
                   has_allowed_tools=("allowed-tools" in q),
                   view_occurrences=count,
                   raw_allowed_tools_hits=len(re.findall(r"(?i)allowed[-_ ]tools", raw)))
        if pos >= 0:
            start_raw = vmap[pos]
            end_raw = vmap[min(pos + len(q) - 1, len(vmap) - 1)]
            rec.update(view_char_index=pos, raw_start_char=start_raw,
                       raw_start_byte=len(raw[:start_raw].encode("utf-8")),
                       raw_start_line=raw_line(raw, start_raw),
                       raw_end_char=end_raw,
                       raw_end_byte=len(raw[:end_raw].encode("utf-8")),
                       raw_end_line=raw_line(raw, end_raw))
        out.append(rec)
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
