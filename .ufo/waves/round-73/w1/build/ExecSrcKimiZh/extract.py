#!/usr/bin/env python3
"""Extract the rendered text of the VitePress page http://www.kimi.com/code/.../skills.html.

Input: the raw HTML saved by `curl -sL` (arg 1). Output on stdout: page text.
Shaping (documented, so the snapshot's relation to the bytes is checkable):
  * the HTML is the VitePress pre-rendered document, so the text is in the markup
    (no JS execution is needed; `window.__VP_HASH_MAP__` is only asset bookkeeping);
  * <script>/<style>/<nav>/<header>/<footer>/<aside>/<button> subtrees are dropped
    (site chrome and the code-block copy button, whose label otherwise leaks the
    language name into the fence);
  * h1-h4 become `#`-prefixed heading lines; <pre> content is copied verbatim into
    a fenced block; table cells become `|`-separated columns; list items `- `;
  * the zero-width space (U+200B) VitePress renders inside the heading anchor is
    removed; runs of >2 blank lines collapse to one blank line.
Nothing else is rewritten: no translation, no re-wrapping, no token normalisation.
"""
import re
import sys
from html.parser import HTMLParser

DROP = {"script", "style", "nav", "header", "footer", "aside", "button"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
        self.pre = 0

    def handle_starttag(self, tag, attrs):
        if tag in DROP:
            self.skip += 1
            return
        if tag == "pre":
            self.pre += 1
            self.out.append("\n```\n")
        elif self.pre:
            return
        elif tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "tr":
            self.out.append("\n|")
        elif tag in ("td", "th"):
            self.out.append(" ")
        elif tag == "br":
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in DROP:
            self.skip -= 1
        elif tag == "pre":
            self.pre -= 1
            self.out.append("\n```")
        elif self.pre:
            return
        elif tag in ("td", "th"):
            self.out.append(" |")
        elif tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n")

    def handle_data(self, data):
        if self.skip:
            return
        data = data.replace("\u200b", "")
        if self.pre:
            self.out.append(data)
        elif data.strip() or data == " ":
            self.out.append(re.sub(r"\s+", " ", data))


def main():
    raw = open(sys.argv[1], encoding="utf-8").read()
    # VitePress renders the fence language as <span class="lang">markdown</span>
    # outside the <button>; drop it so the fence content is the page code only.
    raw = re.sub(r'<span class="lang">.*?</span>', "", raw, flags=re.S)
    p = Text()
    p.feed(raw)
    txt = "".join(p.out)
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    i = txt.find("\n# ")
    if i >= 0:
        txt = txt[i + 1:]
    sys.stdout.write(txt.strip() + "\n")


if __name__ == "__main__":
    main()
