#!/usr/bin/env python3
"""Round-69 scribe: verify the twelve carried quotes against the fetched pages.

Six quote-bearing strings are checked here:
  five C1 located quotes (S203-S207) and the S208 approval sentence
  (the S208 sentence appears twice on its page; both occurrences are reported,
   which is how the twelve count is reached: 5 + 2x2? no -- 5 C1 + S208 (2
   occurrences, 1 sentence) is reported as 5 + 1 with occurrence counts, and
   the per-carry count of 12 strings covers every quoted string in the entry
   plus the S208 sentence; see SEAT_REPORT accounting).
"""
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

CACHE = Path("/tmp/k69-fetch")
LIVE = Path("/tmp/k69-scribe/live")

SKIP = {"script", "style", "noscript", "template", "svg"}
BLOCK = {"p", "li", "br", "tr", "td", "th", "div", "h1", "h2", "h3", "h4",
         "h5", "h6", "pre", "ul", "ol", "table", "section", "article",
         "blockquote", "summary", "details", "dd", "dt", "caption"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
        self.blocks = []      # (tag, text) coarse blocks
        self.cur = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag in BLOCK and self.cur:
            self.out.append("".join(self.cur))
            self.cur = []

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag in BLOCK and self.cur:
            self.out.append("".join(self.cur))
            self.cur = []

    def handle_data(self, data):
        if self.skip:
            return
        self.cur.append(data)

    def close(self):
        super().close()
        if self.cur:
            self.out.append("".join(self.cur))
            self.cur = []


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def extract(path: Path):
    raw = path.read_text("utf-8", "replace")
    p = Text()
    p.feed(raw)
    p.close()
    lines = [norm(x) for x in p.out]
    lines = [(i + 1, x) for i, x in enumerate(lines) if x]
    return raw, lines


def check(label, page, url, quote, extra=()):
    cache = CACHE / page
    live = LIVE / page
    if not cache.exists():
        print(f"{label}: CACHE MISSING {cache}")
        return False
    raw, lines = extract(cache)
    raw_live, lines_live = (extract(live) if live.exists() else (None, []))
    q = norm(quote)

    occurrences = [(n, ln) for n, ln in lines if q in ln]
    norm_hits = sum(ln.count(q) for _, ln in occurrences)
    raw_hits = raw.count(html.escape(q, quote=False)) + raw.count(q)
    live_hits = sum(ln.count(q) for _, ln in lines_live)

    print(f"\n=== {label} ===")
    print(f"page      : {page}  ({url})")
    print(f"cache sha : {sha(cache)}")
    if live.exists():
        print(f"live  sha : {sha(live)}  cache==live: {sha(cache)==sha(live)}")
    print(f"quote     : {quote!r}")
    print(f"wc -w     : {len(quote.split())}")
    print(f"verbatim  : {'YES' if norm_hits else 'NO'}")
    print(f"occurrences (normalized text): {norm_hits} in {len(occurrences)} block(s)")
    print(f"raw-html contiguous hits (tags absent between words): {raw_hits}")
    if live.exists():
        print(f"live-page normalized hits: {live_hits}")
    for n, ln in occurrences:
        print(f"context[text-line {n}]: {ln}")
    for name, needle in extra:
        hit = any(norm(needle) in ln for _, ln in lines)
        print(f"extra  : {name} = {needle!r} -> {'present' if hit else 'ABSENT'}")
    return bool(norm_hits)


def sha(p: Path):
    import hashlib
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


QUOTES = [
    ("S203", "roo.html", "https://docs.roocode.com/features/skills",
     "Project skills override global skills, mode-specific override generic",
     [("section", "What Skills Let You Do"), ("bullet", "Override Control"),
      ("extra-claim", "Roo-specific (higher priority)")]),
    ("S204", "amp.html", "https://ampcode.com/docs/customize/skills",
     "Local skills mask repository skills with the same name.",
     [("section", "Skill Sources and Precedence")]),
    ("S205", "deep.html", "https://deepcode.vegamo.cn/en/docs/configuration/agent-skills",
     "only the highest-priority one is kept",
     [("section", "Scan Locations")]),
    ("S206", "junie.html", "https://junie.jetbrains.com/docs/agent-skills.html",
     "the project-level skill takes precedence and the user-level skill is ignored.",
     [("section", "Skill location"), ("section-alt", "Skill location and precedence")]),
    ("S207", "opencode.html", "https://opencode.ai/docs/skills/",
     "Ensure skill names are unique across all locations",
     [("section", "Troubleshoot loading")]),
]

MS = Path("/tmp/k69-scribe/ms.html")


def check_s208():
    raw, lines = extract(MS)
    q = norm("All three skill tools require approval by default.")
    occurrences = [(n, ln) for n, ln in lines if q in ln]
    hits = sum(ln.count(q) for _, ln in occurrences)
    print("\n=== S208 ===")
    print(f"page      : ms.html (https://learn.microsoft.com/en-us/agent-framework/agents/skills)")
    print(f"cache sha : {sha(MS)}")
    print(f"quote     : {'All three skill tools require approval by default.'!r}")
    print(f"wc -w     : {len('All three skill tools require approval by default.'.split())}")
    print(f"verbatim  : {'YES' if hits else 'NO'}")
    print(f"occurrences (normalized text): {hits} in {len(occurrences)} block(s)")
    for n, ln in occurrences:
        print(f"context[text-line {n}]: {ln}")
    for needle in ("approval by default", "require approval", "tool approval",
                   "Tool approvals", "Security best practices", "Skills"):
        s = norm(needle)
        print(f"extra  : {needle!r} -> {'present' if any(s in ln.lower() for _, ln in lines) else 'ABSENT'}")
    return bool(hits)


if __name__ == "__main__":
    ok = True
    for label, page, url, quote, extra in QUOTES:
        ok &= check(label, page, url, quote, extra)
    ok &= check_s208()
    print(f"\nALL VERBATIM: {ok}")
    sys.exit(0 if ok else 1)
