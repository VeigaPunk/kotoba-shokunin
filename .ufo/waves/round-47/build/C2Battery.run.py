#!/usr/bin/env python3
"""Run one candidate C2 predicate over C2Battery.json (stdlib only).

A candidate is f(row) -> bool; True means "this description carries an XML tag".
It sees only id, category, value and yaml. label, alt_label, ambiguity and reason
are withheld, so a candidate cannot read its own answer.

  python3 -B C2Battery.run.py --predicate builtin:xml-strict
  python3 -B C2Battery.run.py --predicate CANDIDATE.py[:function] [--json] [--rows]
  python3 -B C2Battery.run.py --list-predicates
  python3 -B C2Battery.run.py --self-test

Exit: 0  every decisive row (s003_ambiguous=false) agrees with its label
      1  a decisive row disagrees, or --self-test fails
      2  environment error: battery unreadable or malformed, predicate unloadable,
         predicate raised, or predicate returned a non-bool
Ambiguous rows are reported as agree-with-label and agree-with-alt; they never gate.
"""
import argparse
import html
import importlib.util
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
BATTERY = HERE / "C2Battery.json"
REQUIRED_FIELDS = ("id", "category", "label", "s003_ambiguous", "alt_label",
                   "ambiguity", "reason", "yaml", "value")
REQUIRED_CATEGORIES = {
    "plain-tag", "closing-selfclosing", "attribute", "namespaced", "backtick-code-span",
    "comparator-spaced", "x-lt-y", "lt-equal", "arrow", "lt-digit", "autolink",
    "comment-doctype-pi-cdata", "entity-encoded", "unicode-lookalike", "yaml-folded-split",
    "yaml-block-literal", "yaml-quoted", "real-world", "control",
}


class EnvError(Exception):
    """Exit-2 condition: the battery or a candidate cannot be evaluated."""


# XML 1.0 5th ed. reference grammar. STag [40], ETag [42], EmptyElemTag [44];
# NameStartChar [4], NameChar [4a], Name [5], Attribute [41], AttValue [10], Eq [25],
# S [3] = one or more of #x20 #x9 #xD #xA; Reference [67] restricted to the forms used here.
NAME_START = (r":A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF"
              r"\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD"
              r"\U00010000-\U000EFFFF")
NAME_CHAR = NAME_START + r"\-.0-9\u00B7\u0300-\u036F\u203F-\u2040"
NAME = "[" + NAME_START + "][" + NAME_CHAR + "]*"
SP = r"[ \t\r\n]"
REF = "&(?:" + NAME + r"|#[0-9]+|#x[0-9A-Fa-f]+);"
ATTVAL = "(?:\"(?:[^<&\"]|" + REF + ")*\"|'(?:[^<&']|" + REF + ")*')"
ATTR = SP + "+" + NAME + SP + "*=" + SP + "*" + ATTVAL
XML_TAG = re.compile("<" + NAME + "(?:" + ATTR + ")*" + SP + "*/?>" + "|</" + NAME + SP + "*>")


def xml_tag(text):
    """Reference predicate: the text contains an STag, ETag or EmptyElemTag."""
    return XML_TAG.search(text) is not None


# Built-in candidates. Each reads only the view passed by run(); the first one
# reproduces the BASE check (grep -c '<skills>' over the frontmatter source).
BUILTIN = {
    "base-grep-skills": lambda r: "<skills>" in r["yaml"],
    "naive-angle": lambda r: re.search(r"<[^>]*>", r["value"]) is not None,
    "tag-shaped-lenient": lambda r: re.search(r"</?[A-Za-z_:][^<>]*>", r["value"]) is not None,
    "markup-any": lambda r: xml_tag(r["value"]) or re.search(r"<[!?]", r["value"]) is not None,
    "xml-strict": lambda r: xml_tag(r["value"]),
    "xml-strict-nfkc": lambda r: xml_tag(unicodedata.normalize("NFKC", r["value"])),
    "xml-strict-unescaped": lambda r: xml_tag(html.unescape(r["value"])),
    # Anthropic quick_validate.py (fetched 2026-10-21): any '<' or '>' is rejected. Stricter than S003.
    "anthropic-quick-validate": lambda r: "<" in r["value"].strip() or ">" in r["value"].strip(),
    # Counterexample candidate: strip backtick and quoted spans before the grammar check.
    "span-stripped-xml": lambda r: xml_tag(re.sub(r"`[^`\n]*`|\"[^\"\n]*\"|'[^'\n]*'", " ", r["value"])),
}

# Grammar units: (text, expected xml_tag result). Exercise the reference itself.
UNITS = [
    ("<a:b>", True), ("<skills/>", True), ("<skills />", True), ("<skills>", True),
    ("</skills>", True), ("<skills\t>", True), ("<a b='c'>", True), ('<a b="c&amp;">', True),
    ("<\u6280\u80fd>", True), ("<caf\u00e9>", True), ("<\U0001F642>", True),
    ("a < b", False), ("<3", False), ("x<y", False), ("</ a>", False), ("<>", False),
    ("</>", False), ("<skills / >", False), ("<-x>", False), ("<1a>", False),
    ("<a b=c>", False), ("&lt;a&gt;", False), ("<https://x.y>", False),
]


def load_battery(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise EnvError(f"cannot read battery {path}: {exc}") from exc
    rows = data.get("rows") if isinstance(data, dict) else None
    if not isinstance(rows, list) or not rows:
        raise EnvError(f"battery {path} has no rows")
    for row in rows:
        missing = [f for f in REQUIRED_FIELDS if f not in row]
        if missing:
            raise EnvError(f"row {row.get('id', '?')} lacks {missing}")
    return rows


def load_predicate(spec):
    if spec.startswith("builtin:"):
        name = spec.split(":", 1)[1]
        if name not in BUILTIN:
            raise EnvError(f"unknown builtin {name!r}; see --list-predicates")
        return BUILTIN[name]
    path, sep, fn_name = spec.rpartition(":")
    if not (sep and fn_name.isidentifier() and path.endswith(".py")):
        path, fn_name = spec, "predicate"
    if not Path(path).is_file():
        raise EnvError(f"no predicate file {path}")
    mod_spec = importlib.util.spec_from_file_location("c2_candidate", path)
    module = importlib.util.module_from_spec(mod_spec)
    try:
        mod_spec.loader.exec_module(module)
    except Exception as exc:
        raise EnvError(f"importing {path} failed: {exc!r}") from exc
    fn = getattr(module, fn_name, None)
    if not callable(fn):
        raise EnvError(f"{path} has no callable {fn_name!r}")
    return fn


def run(rows, predicate):
    results = []
    for row in rows:
        view = {k: row[k] for k in ("id", "category", "value", "yaml")}
        try:
            got = predicate(view)
        except Exception as exc:
            raise EnvError(f"predicate raised on {row['id']}: {exc!r}") from exc
        if not isinstance(got, bool):
            raise EnvError(f"predicate returned {type(got).__name__} on {row['id']}; expected bool")
        results.append((row, got))
    return results


def is_tag(row):
    return row["label"] == "tag"


def summarize(results):
    decisive = [(r, g) for r, g in results if not r["s003_ambiguous"]]
    ambiguous = [(r, g) for r, g in results if r["s003_ambiguous"]]
    fp = [r["id"] for r, g in decisive if g and not is_tag(r)]
    fn = [r["id"] for r, g in decisive if is_tag(r) and not g]
    return {
        "rows": len(results),
        "decisive": {"n": len(decisive), "agree": len(decisive) - len(fp) - len(fn),
                     "fp": fp, "fn": fn},
        "ambiguous": {"n": len(ambiguous),
                      "agree_label": sum(g == is_tag(r) for r, g in ambiguous),
                      "agree_alt": sum(g == (r["alt_label"] == "tag") for r, g in ambiguous)},
    }


def self_test(rows):
    failures, count = [], 0

    def check(cond, msg):
        nonlocal count
        count += 1
        if not cond:
            failures.append(msg)

    check(len(rows) >= 40, f"rows >= 40 (got {len(rows)})")
    ids = [r["id"] for r in rows]
    check(len(set(ids)) == len(ids), "ids are unique")
    missing = REQUIRED_CATEGORIES - {r["category"] for r in rows}
    check(not missing, f"required categories present (missing {sorted(missing)})")
    for r in rows:
        rid = r["id"]
        check(r["label"] in ("tag", "not-tag"), f"{rid}: label is tag or not-tag")
        check(isinstance(r["s003_ambiguous"], bool), f"{rid}: s003_ambiguous is bool")
        if r["s003_ambiguous"]:
            check(bool(r["ambiguity"]) and r["alt_label"] == ("not-tag" if is_tag(r) else "tag"),
                  f"{rid}: ambiguous row has ambiguity text and the opposite alt_label")
        else:
            check(r["alt_label"] is None and r["ambiguity"] is None,
                  f"{rid}: decisive row carries no alt_label or ambiguity")
        check(bool(str(r["reason"]).strip()), f"{rid}: reason is non-empty")
        check(isinstance(r["value"], str) and isinstance(r["yaml"], str),
              f"{rid}: value and yaml are strings")
        check(xml_tag(r["value"]) == is_tag(r),
              f"{rid}: reference grammar agrees with label (strict reading)")
    for text, want in UNITS:
        check(xml_tag(text) == want, f"grammar unit {text!r} -> {want}")
    print(f"self-test: {len(failures)} failure(s) over {count} assertions")
    for msg in failures:
        print(f"  FAIL {msg}")
    return 0 if not failures else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--predicate", help="builtin:<name> or FILE.py[:function]")
    ap.add_argument("--battery", default=str(BATTERY), help="default: C2Battery.json beside this file")
    ap.add_argument("--json", action="store_true", help="emit the summary as JSON")
    ap.add_argument("--rows", action="store_true", help="print every row's prediction")
    ap.add_argument("--list-predicates", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    try:
        if args.list_predicates:
            print("\n".join("builtin:" + name for name in BUILTIN))
            return 0
        rows = load_battery(args.battery)
        if args.self_test:
            return self_test(rows)
        if not args.predicate:
            raise EnvError("--predicate is required (or --self-test / --list-predicates)")
        results = run(rows, load_predicate(args.predicate))
    except EnvError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    summary = summarize(results)
    dec, amb = summary["decisive"], summary["ambiguous"]
    ok = not dec["fp"] and not dec["fn"]
    summary.update(battery=str(args.battery), predicate=args.predicate,
                   verdict="PASS" if ok else "FAIL")
    if args.json:
        summary["per_row"] = [{"id": r["id"], "label": r["label"], "alt_label": r["alt_label"],
                               "s003_ambiguous": r["s003_ambiguous"], "predicted_tag": g}
                              for r, g in results]
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if ok else 1
    print(f"battery   {Path(args.battery).name}  rows={summary['rows']}  "
          f"decisive={dec['n']}  s003_ambiguous={amb['n']}")
    print(f"predicate {args.predicate}")
    print(f"decisive  agree={dec['agree']}/{dec['n']}  fp={dec['fp']}  fn={dec['fn']}")
    print(f"ambiguous agree_with_label={amb['agree_label']}/{amb['n']}  "
          f"agree_with_alt={amb['agree_alt']}/{amb['n']}  (reported, not gated)")
    for r, g in results:
        if args.rows or (not r["s003_ambiguous"] and g != is_tag(r)):
            flag = "AMB " if r["s003_ambiguous"] else "    "
            label = "MISS" if (not r["s003_ambiguous"] and g != is_tag(r)) else "    "
            print(f"  {label} {flag}{r['id']:4} label={r['label']:8} predicted="
                  f"{'tag' if g else 'not-tag':8} {r['category']}")
    print(f"verdict   {summary['verdict']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
