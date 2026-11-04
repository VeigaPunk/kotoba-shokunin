#!/usr/bin/env python3
"""Mirror checker: R6 (eval_set_shape) for the round-85 C1 trigger eval candidate.

Applies the R6 conditions from plans/round-85.md section C1 to a candidate TSV:
  - header line is exactly `label<TAB>query`
  - 8-10 should-trigger rows and 8-10 should-not-trigger rows
  - >= 5 should-trigger rows contain none of the description's declared
    trigger terms (indirect positives)
  - every should-not-trigger row shares >= 1 lowercased alphanumeric token
    of >= 4 characters with the parsed description (near-miss negatives)

The candidate description bytes are read verbatim from
candidate-description.txt (extracted from the freeze commit's plan § C1).
Stdlib only. Exit ladder: 0 pass, 1 content fail, 2 environment error.
"""
import argparse
import re
import sys
from pathlib import Path

MIN_POS, MAX_POS, MIN_NEG, MAX_NEG = 8, 10, 8, 10
MIN_INDIRECT, MIN_TOKEN = 5, 4


def parse_args():
    here = Path(__file__).resolve().parent
    p = argparse.ArgumentParser(description="R6 eval_set_shape mirror checker")
    p.add_argument("--tsv", type=Path, default=here / "description-eval-round85.tsv")
    p.add_argument("--description", type=Path, default=here / "candidate-description.txt")
    return p.parse_args()


def tokens(text):
    return {t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) >= MIN_TOKEN}


def trigger_terms(description):
    m = re.search(r"Triggers:(.*?)Anti-triggers:", description, re.S)
    if not m:
        sys.exit("description carries no Triggers: clause")
    return re.findall(r'"([^"]+)"', m.group(1))


def main():
    args = parse_args()
    try:
        description = args.description.read_text(encoding="utf-8").rstrip("\n")
        lines = args.tsv.read_text(encoding="utf-8").split("\n")
    except OSError as exc:
        print(f"environment error: {exc}")
        return 2
    failures = []
    if lines and lines[-1] == "":
        lines.pop()  # tolerate the final newline
    if not lines or lines[0] != "label\tquery":
        failures.append(f"header is {lines[0]!r}, want 'label<TAB>query'")
    rows = []
    for n, line in enumerate(lines[1:], start=2):
        parts = line.split("\t")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            failures.append(f"line {n}: want label<TAB>query, both fields non-empty, got {line!r}")
            continue
        rows.append((n, parts[0], parts[1]))
    pos = [r for r in rows if r[1] == "should-trigger"]
    neg = [r for r in rows if r[1] == "should-not-trigger"]
    bad_labels = sorted({r[1] for r in rows} - {"should-trigger", "should-not-trigger"})
    if bad_labels:
        failures.append(f"unknown labels: {', '.join(bad_labels)}")
    if not MIN_POS <= len(pos) <= MAX_POS:
        failures.append(f"should-trigger rows = {len(pos)}, want {MIN_POS}-{MAX_POS}")
    if not MIN_NEG <= len(neg) <= MAX_NEG:
        failures.append(f"should-not-trigger rows = {len(neg)}, want {MIN_NEG}-{MAX_NEG}")
    terms = trigger_terms(description)
    indirect = [r for r in pos if not any(t.lower() in r[2].lower() for t in terms)]
    print(f"rows: should-trigger={len(pos)} should-not-trigger={len(neg)}")
    print(f"declared trigger terms ({len(terms)}): {', '.join(terms)}")
    print(f"indirect positives (none of the declared terms): {len(indirect)} (need >= {MIN_INDIRECT})")
    for n, _, query in pos:
        hits = sorted(t for t in terms if t.lower() in query.lower())
        tag = "indirect" if not hits else "direct: " + ", ".join(hits)
        print(f"  line {n}: {tag}")
    if len(indirect) < MIN_INDIRECT:
        failures.append(f"indirect positives = {len(indirect)}, want >= {MIN_INDIRECT}")
    desc_tokens = tokens(description)
    near = 0
    for n, _, query in neg:
        shared = sorted(tokens(query) & desc_tokens)
        if shared:
            near += 1
            print(f"  line {n}: shared token(s): {', '.join(shared)}")
        else:
            print(f"  line {n}: NO shared token >= {MIN_TOKEN} chars")
            failures.append(f"line {n}: negative row shares no token >= {MIN_TOKEN} chars with the description")
    print(f"near-miss negatives (share a token >= {MIN_TOKEN} chars): {near}/{len(neg)}")
    if failures:
        print("FAIL R6 eval_set_shape")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("OK R6 eval_set_shape: header exact, row counts in range, indirect floor met, all negatives near-miss")
    return 0


if __name__ == "__main__":
    sys.exit(main())
