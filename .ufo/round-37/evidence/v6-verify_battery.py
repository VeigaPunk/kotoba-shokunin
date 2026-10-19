#!/usr/bin/env python3
"""Verify the instrument's OWN planted fence battery (``FENCE_SHAPES``) against
cmark 0.31.2 and against the live instrument, field by field.

The battery pins literals (``content``, ``boxes``, ``unclosed``) that the
self-test then trusts.  A pinned literal is a claim about CommonMark: this
script re-derives it from cmark and from the live ``extract_boxes``, so a
self-consistent-but-wrong pin cannot hide behind the self-test.

``content`` is compared against *fenced* code content only: a cmark code_block
whose first line is indented four columns or more is an indented code block
(§4.4), which ``fenced_regions`` does not claim to cover -- the box layer owns
that class in the landed instrument (``is_indented_code_marker``).

Usage: python3 verify_battery.py [--repo ROOT]
"""
import argparse
import pathlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import oracle  # noqa: E402
import spec_rules  # noqa: E402

NS = "{http://commonmark.org/xml/1.0}"


def cmark_code_spans(lines: list[str]) -> list[tuple[int, int, bool]]:
    """(start line, end line, is_fenced) for every cmark code block."""
    xml = subprocess.run(["cmark", "-t", "xml", "--sourcepos"],
                         input="\n".join(lines) + "\n", capture_output=True,
                         text=True, check=True).stdout
    root = ET.fromstring(re.sub(r"^<!DOCTYPE[^>]*>\n", "", xml))
    out = []
    for node in root.iter(NS + "code_block"):
        a, b = node.attrib["sourcepos"].split("-")
        start = int(a.split(":")[0])
        end = int(b.split(":")[0])
        first = spec_rules.strip_quote(lines[start - 1])
        cols, body = spec_rules.columns(first)
        fenced = cols <= 3 and bool(spec_rules.FENCE_RE.match(body))
        out.append((start, end, fenced))
    return out


def cmark_fenced_content(lines: list[str]) -> set[int]:
    """Fenced-block content lines only, excluding indented code blocks (§4.4)
    and excluding the closing fence line (an unclosed block has no closer, so
    its last line is content)."""
    content: set[int] = set()
    for start, end, fenced in cmark_code_spans(lines):
        if not fenced:
            continue
        last = spec_rules.strip_quote(lines[end - 1])
        cols, body = spec_rules.columns(last)
        closer = cols <= 3 and bool(spec_rules.FENCE_RE.match(body))
        content.update(range(start + 1, end if closer else end + 1))
    return content


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(HERE.parents[2]))
    args = ap.parse_args()
    repo = pathlib.Path(args.repo).resolve()
    before = oracle.sha(repo / "verifiers" / "verify_skill_checklist.py")
    sys.path.insert(0, str(repo / "verifiers"))
    import verify_skill_checklist as vsc
    shapes = getattr(vsc, "FENCE_SHAPES", None)
    if shapes is None:
        print("instrument has no FENCE_SHAPES battery; nothing to verify")
        return 2
    bad = 0
    for sh in shapes:
        lines = list(sh["lines"])
        cmark_fenced = cmark_fenced_content(lines)
        cmark_all, _ = oracle.cmark_code_lines(lines)
        spec_content, snotes = spec_rules.code_lines(lines)
        spec_fenced = {i for i in spec_content
                       if i not in cmark_all or i in cmark_fenced}
        boxes, _ = vsc.extract_boxes(list(lines))
        live = sorted(b["line"] for b in boxes)
        pinned_content = sorted(sh["content"])
        pinned_boxes = sorted(sh["boxes"])
        pinned_unclosed = sh["unclosed"]
        ob = sorted(x for x in live if x not in cmark_fenced)
        unclosed_cmark = next((n["line"] for n in snotes if "unclosed" in n["note"]),
                              None)
        checks = {
            "content==cmark_fenced": sorted(cmark_fenced) == pinned_content,
            "content==spec_fenced": sorted(spec_fenced) == pinned_content,
            "boxes==cmark_live": pinned_boxes == ob,
            "unclosed==spec_rules": pinned_unclosed == unclosed_cmark,
            "instrument==pinned_boxes": live == pinned_boxes,
        }
        status = "PASS" if all(checks.values()) else "FAIL"
        if status == "PASS":
            note = "cmark indented-code lines here: %s" % (
                sorted(cmark_all - cmark_fenced) or "none")
            print("PASS %-40s %s" % (sh["id"], note))
        else:
            bad += 1
            print("FAIL %-40s %s" % (sh["id"],
                                     {k: v for k, v in checks.items() if not v}))
            print("      lines=%r" % (lines,))
            print("      pinned content=%s cmark_fenced=%s spec_fenced=%s"
                  % (pinned_content, sorted(cmark_fenced), sorted(spec_fenced)))
            print("      pinned boxes=%s instrument=%s cmark-live=%s"
                  % (pinned_boxes, live, ob))
    print("\nbattery shapes=%d  failing=%d  (fields: content/boxes/unclosed, "
          "cmark+spec_rules+instrument)" % (len(shapes), bad))
    after = oracle.sha(repo / "verifiers" / "verify_skill_checklist.py")
    print("instrument sha256 before/after run: %s / %s  %s"
          % (before[:12], after[:12], "STABLE" if before == after else "MOVED"))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())