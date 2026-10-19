#!/usr/bin/env python3
"""Self-checking cmark oracle + instrument diff for the round-37 C3 shapes.

For every shape in ``shapes/`` this prints one row per planted box line:
my spec reading (shapes.json expect), cmark 0.31.2 ground truth, and the live
verdict of ``verify_skill_checklist.extract_boxes`` at the revision under test.

The cmark arm is self-checking: each ``<code_block>`` node's text is matched
against the source lines its sourcepos claims (indentation and block-quote
prefixes stripped), so a cmark sourcepos quirk is reported as UNEXPLAINED
instead of silently becoming ground truth.

The instrument file's sha256 is printed before and after the run; a difference
means a concurrent editor, and the measurement is reported as such.

Usage: python3 oracle.py [--repo ROOT] [--json OUT]
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import spec_rules  # noqa: E402

PROBE_RE = re.compile(r"-\s+\[([ xX])\]\s?(.*)$")
NS = "{http://commonmark.org/xml/1.0}"


def strip_indent(line: str, n: int) -> str:
    col = 0
    i = 0
    while i < len(line) and col < n:
        if line[i] == " ":
            col += 1
        elif line[i] == "\t":
            col += spec_rules.TAB - (col % spec_rules.TAB)
        else:
            break
        i += 1
    return line[i:] if col >= n else line


def cmark_code_lines(lines: list[str]) -> tuple[set[int], list[dict]]:
    xml = subprocess.run(["cmark", "-t", "xml", "--sourcepos"],
                         input="\n".join(lines) + "\n", capture_output=True,
                         text=True, check=True).stdout
    root = ET.fromstring(re.sub(r"^<!DOCTYPE[^>]*>\n", "", xml))
    content: set[int] = set()
    notes: list[dict] = []
    for node in root.iter(NS + "code_block"):
        a, b = node.attrib["sourcepos"].split("-")
        start = int(a.split(":")[0])
        end = int(b.split(":")[0])
        want = (node.text or "").split("\n")[:-1]
        for lo, hi in [(start + 1, end - 1), (start + 1, end),
                       (start, end - 1), (start, end)]:
            cand = lines[lo - 1:hi]
            if len(cand) != len(want):
                continue
            for variant in range(3):
                if variant == 1:
                    cand2 = [spec_rules.strip_quote(x) for x in cand]
                elif variant == 2:
                    cand2 = [spec_rules.strip_quote(x) for x in cand]
                    cand2 = [x[1:] if x.startswith(" ") else x for x in cand2]
                else:
                    cand2 = cand
                for indent in range(0, 7):
                    if [strip_indent(x, indent) for x in cand2] == want:
                        content.update(range(lo, hi + 1))
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            notes.append({"span": node.attrib["sourcepos"],
                          "node_text": (node.text or "")[:60],
                          "note": "UNEXPLAINED cmark span"})
    return content, notes


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(HERE.parents[2]))
    ap.add_argument("--json", default=str(HERE / "matrix.json"))
    args = ap.parse_args()
    repo = pathlib.Path(args.repo).resolve()
    target = repo / "verifiers" / "verify_skill_checklist.py"
    before = sha(target)
    sys.path.insert(0, str(repo / "verifiers"))
    import verify_skill_checklist as vsc
    assert sha(pathlib.Path(vsc.__file__)) == before
    manifest = json.loads((HERE / "shapes.json").read_text())
    rows, bad = [], 0
    for entry in manifest:
        lines = pathlib.Path(entry["path"]).read_text().split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        cmark_lines, cnotes = cmark_code_lines(lines)
        spec_lines, snotes = spec_rules.code_lines(lines)
        boxes, near = vsc.extract_boxes(list(lines))
        live = {b["line"] for b in boxes}
        for i, line in enumerate(lines, 1):
            m = PROBE_RE.search(line)
            if not m:
                continue
            text = m.group(2).strip()
            exp = next((v for k, v in entry["expect"].items()
                        if text.startswith(k)), "?")
            oracle = "illustration" if i in cmark_lines else "live"
            mine = "illustration" if i in spec_lines else "live"
            inst = "live" if i in live else "illustration"
            verdict = "ok" if (oracle == inst == mine == exp) else "MISMATCH"
            bad += verdict != "ok"
            rows.append({"shape": entry["shape"], "line": i, "text": text,
                         "expect": exp, "spec": mine, "cmark": oracle,
                         "instrument": inst, "verdict": verdict,
                         "cites": entry["cite"]})
        for n in cnotes + snotes:
            rows.append({"shape": entry["shape"], "line": n.get("line", 0),
                         "text": "note", "expect": "-", "spec": "-",
                         "cmark": "-", "instrument": "-",
                         "verdict": "note: " + n["note"], "cites": ""})
        if near:
            rows.append({"shape": entry["shape"], "line": near[0]["line"],
                         "text": "near-miss: " + near[0]["text"],
                         "expect": "-", "spec": "-", "cmark": "-",
                         "instrument": "-",
                         "verdict": "near-miss kind=%s" % near[0].get("kind"),
                         "cites": ""})
    width = max(len(r["shape"]) for r in rows)
    for r in rows:
        print("%-*s L%-3d %-34s spec=%-12s cmark=%-12s instrument=%-12s %s"
              % (width, r["shape"], r["line"], r["text"][:34], r["spec"],
                 r["cmark"], r["instrument"], r["verdict"]))
    probes = [r for r in rows if r["verdict"] in ("ok", "MISMATCH")]
    print("\nprobe lines=%d  mismatches=%d  (instrument vs cmark)"
          % (len(probes), bad))
    for r in [x for x in rows if x["verdict"] == "MISMATCH"]:
        tag = "instrument-only" if r["cmark"] == r["spec"] else "MY READING"
        print("  %s: %s L%d %s (instrument=%s, cmark=%s)"
              % (tag, r["shape"], r["line"], r["text"], r["instrument"],
                 r["cmark"]))
    print("\nshapes=%d  spec-vs-cmark disagreements=%d  unexplained cmark spans=%d"
          % (len(manifest), len([r for r in probes if r["spec"] != r["cmark"]]),
             len([r for r in rows if "UNEXPLAINED" in r["verdict"]])))
    after = sha(target)
    print("instrument sha256 before/after run: %s / %s  %s"
          % (before[:12], after[:12], "STABLE" if before == after else "MOVED"))
    pathlib.Path(args.json).write_text(
        json.dumps({"instrument_sha256": before, "rows": rows}, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())