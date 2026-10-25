#!/usr/bin/env python3
"""Anchor check: which heading chain encloses each carried quote?

Catches the S201 defect class (quote verbatim but filed under the wrong section)
without depending on any lane script.
"""
import html
import re
from html.parser import HTMLParser
from pathlib import Path

SKIP = {"script", "style", "noscript", "template", "svg"}
BLOCK = {"p", "li", "br", "tr", "td", "th", "div", "h1", "h2", "h3", "h4",
         "h5", "h6", "pre", "ul", "ol", "table", "section", "article",
         "blockquote", "summary", "details", "dd", "dt", "caption"}
HRE = re.compile(r"h([1-6])")


class Doc(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.stack = []          # [(level, text)]
        self.heading = None      # [level, text] currently open
        self.cur = []
        self.blocks = []         # (line, text, heading-chain-string)

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if HRE.fullmatch(tag):
            self._flush()
            self.heading = [int(tag[1]), ""]
        elif tag in BLOCK:
            self._flush()

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if HRE.fullmatch(tag) and self.heading:
            lv, txt = self.heading
            txt = re.sub(r"\s+", " ", txt).strip()
            while self.stack and self.stack[-1][0] >= lv:
                self.stack.pop()
            self.stack.append((lv, txt))
            self.blocks.append((len(self.blocks) + 1, txt, " > ".join(t for _, t in self.stack)))
            self.heading = None
        elif tag in BLOCK:
            self._flush()

    def handle_data(self, data):
        if self.skip:
            return
        if self.heading is not None:
            self.heading[1] += data
        self.cur.append(data)

    def _flush(self):
        txt = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        self.cur = []
        if txt:
            chain = " > ".join(t for _, t in self.stack) or "(no heading yet)"
            self.blocks.append((len(self.blocks) + 1, txt, chain))


def load(p):
    d = Doc()
    d.feed(Path(p).read_text("utf-8", "replace"))
    d.close()
    d._flush()
    return d.blocks


CASES = [
    ("S203", "/tmp/k69-fetch/roo.html", "Project skills override global skills, mode-specific override generic", "What Skills Let You Do"),
    ("S204", "/tmp/k69-fetch/amp.html", "Local skills mask repository skills with the same name.", "Skill Sources and Precedence"),
    ("S205", "/tmp/k69-fetch/deep.html", "only the highest-priority one is kept", "Scan Locations"),
    ("S206", "/tmp/k69-fetch/junie.html", "the project-level skill takes precedence and the user-level skill is ignored.", "Skill location"),
    ("S207", "/tmp/k69-fetch/opencode.html", "Ensure skill names are unique across all locations", "Troubleshoot loading"),
    ("S208", "/tmp/k69-scribe/ms.html", "All three skill tools require approval by default.", "Tool approval"),
    ("S201", "/tmp/k69-scribe/ms.html", "Agent Skills should be treated like any third-party code you bring into your project.", "Security best practices"),
]

for label, page, quote, claimed in CASES:
    q = re.sub(r"\s+", " ", quote).strip()
    blocks = load(page)
    hits = [b for b in blocks if q in b[1]]
    print(f"\n{label}  page={Path(page).name}  claimed-anchor={claimed!r}")
    if not hits:
        print("  NOT FOUND on page")
        continue
    for line, text, chain in hits:
        claimed_ok = claimed.lower() in chain.lower()
        print(f"  block {line}: chain = {chain!r}")
        print(f"    claimed anchor present in chain: {claimed_ok}")
        print(f"    block text: {text}")
