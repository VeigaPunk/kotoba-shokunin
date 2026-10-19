#!/usr/bin/env python3
"""Independent re-derivation of the container battery pins V6b must add to
FENCE_SHAPES (round-38 C3, seat V5).

Three shapes, one per residual class V6 named at r37 (S07 four-column fence in
a list item, S08 nested item, S07b outdented closer).  Every pin below is
derived from cmark 0.31.2 structure alone by ``verify_battery_cmark.cmark_arms``
(no spec implementation in the loop): ``content`` = the code_block's content
lines, ``boxes`` = planted probe lines outside every code_block, ``unclosed``
= None because each block's content ends before its span's last line.

Run: python3 pins_for_battery.py [--emit]   (--emit prints the FENCE_SHAPES
entries ready to paste; the default prints the derivation + the live check
against the candidate instrument named on the command line).
"""
import argparse
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_battery_cmark as vbc  # noqa: E402

SHAPES = [
    ("fence-in-list-item-four-columns",
     "0.31.2 §4.5 rule 1 read inside the container + §5.2 (item content col 2)",
     ["- item", "    ```", "    - [ ] decoy-in-list-fence", "    ```",
      "- [ ] live-after-item"]),
    ("fence-in-nested-item",
     "0.31.2 §4.5 rule 1 inside the nested container + §5.2 (nested col 4)",
     ["- outer", "  - inner", "    ```", "    - [ ] decoy-in-nested-fence",
      "    ```", "- [ ] live-after-nested"]),
    ("outdented-closer-ends-item",
     "0.31.2 §4.5 rule 5 (the block ends with its container) + §5.2",
     ["- item", "  ```", "  - [ ] decoy-in-item-fence", "```",
      "- [ ] decoy-in-doc-fence", "```", "- [ ] live-after"]),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=None,
                    help="candidate instrument's repo root (live check)")
    ap.add_argument("--emit", action="store_true")
    args = ap.parse_args()
    entries = []
    for sid, cite, lines in SHAPES:
        cm = vbc.cmark_arms(lines)
        entries.append({"id": sid, "spec": cite, "lines": lines,
                        "content": cm["fenced"], "boxes": cm["boxes"],
                        "unclosed": cm["unclosed"]})
        print("%s\n  content=%s boxes=%s unclosed=%s\n  cmark_all=%s "
              "(indented-code arm)" % (sid, cm["fenced"], cm["boxes"],
                                       cm["unclosed"], cm["all"]))
    if args.emit:
        for e in entries:
            print('\n    {"id": "%s",\n     "spec": "%s",\n     "lines": %r,'
                  '\n     "content": %s, "boxes": %s, "unclosed": %s},'
                  % (e["id"], e["spec"], e["lines"], e["content"],
                     e["boxes"], e["unclosed"]))
    if args.repo:
        repo = pathlib.Path(args.repo).resolve()
        sys.path.insert(0, str(repo / "verifiers"))
        import verify_skill_checklist as vsc
        bad = 0
        for e in entries:
            content, blocks, unclosed = vsc.fenced_regions(list(e["lines"]))
            boxes, near = vsc.extract_boxes(list(e["lines"]))
            got = sorted(b["line"] for b in boxes)
            ok = (sorted(content) == e["content"] and got == e["boxes"]
                  and unclosed == e["unclosed"])
            bad += not ok
            print("%s candidate[%s] content=%s boxes=%s unclosed=%s "
                  "(want %s/%s/%s)" % ("PASS" if ok else "FAIL", e["id"],
                                       sorted(content), got, unclosed,
                                       e["content"], e["boxes"],
                                       e["unclosed"]))
        print("\ncandidate failing=%d over %d container shapes" % (bad,
                                                                  len(entries)))
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
