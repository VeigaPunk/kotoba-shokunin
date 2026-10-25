#!/usr/bin/env python3
"""Derive the rendered text of the S261 page from its committed HTML snapshot.

Deterministic, byte-for-byte reproducible: drop <script>/<style> elements, strip
every remaining tag, unescape HTML entities. No whitespace rewriting, no
normalization. The result is a SHAPE of the page (what a browser renders), not the
page's bytes; the raw forms stay the snapshots of record.

Usage: python3 -B render_text.py [--root <lane-root>] [--write]
"""
import argparse
import hashlib
import html
import os
import re
import sys

SRC = "S261-letta-skills.html"
DST = "S261-letta-skills.rendered.txt"


def render(h):
    body = re.sub(r"(?s)<(script|style)\b.*?</\1>", "", h)
    body = re.sub(r"<[^>]+>", "", body)
    return html.unescape(body)


def main():
    root = os.path.abspath(__file__)
    for _ in range(7):
        root = os.path.dirname(root)
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=root)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    snapdir = os.path.join(args.root, ".ufo", "waves", "round-72", "snapshots")
    with open(os.path.join(snapdir, SRC), "rb") as fh:
        src = fh.read()
    out = render(src.decode("utf-8")).encode("utf-8")
    print("source %s bytes=%d sha256=%s" % (SRC, len(src), hashlib.sha256(src).hexdigest()))
    print("rendered %s bytes=%d sha256=%s" % (DST, len(out), hashlib.sha256(out).hexdigest()))
    if args.write:
        with open(os.path.join(snapdir, DST), "wb") as fh:
            fh.write(out)
        print("wrote %s" % os.path.join(snapdir, DST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
