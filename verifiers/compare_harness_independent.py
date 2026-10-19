#!/usr/bin/env python3
"""compare_harness_independent.py — C1 agreement driver (round 37, seat P4).

Builds the N/28 agreement report for the harness claim set.  It runs the LIVE
observation instrument (``verifiers/verify_harness_claims.py --json``) and the
source-blind independent re-derivation instrument
(``verifiers/verify_harness_independent.py --json``), joins the two outputs on
check id, and reports how many of the pinned checks the independent
re-derivation reproduces.

Source-blindness (round 37 C1 rule): this driver embeds NO expected value, no
check-id list and no baseline; it only transports both instruments' own
outputs, so the agreement verdict is a measured join rather than a restatement.
Nothing in this file was copied from ``verify_harness_claims.py``, the harness
rows of ``verifiers/baseline.json``, or corpus docs quoting them.

Interface contract for the independent instrument — ``--json`` prints ONE JSON
object to stdout in one of these shapes::

    {"results": [{"check": <id>, "expected": <value>, ...}, ...]}
    {"checks":  [{"id": <id>, "re_derived": <value>, ...}, ...]}
    {<dotted.check.id>: <value>, ...}                  (flat expected map)

Per-record id keys: ``check`` | ``id`` | ``name``.  Per-record value keys, in
priority order: ``expected`` | ``expected_value`` | ``re_derived`` | ``value`` |
``observed``.  Any other shape — e.g. observations nested by subject rather
than keyed by check id — is a loud error here (exit 2), never a silent pass.

Comparison semantics (two columns, both always computed):

* **strict** — type-tagged value equality (``1`` != ``True``, ``7`` != ``7.0``,
  list order significant, dict key order insignificant).
* **protocol** — the mode-aware agreement predicate frozen by the round-37 C1
  adjudication protocol, read from the live payload's own ``mode`` field:
  ``equal`` -> strict equality; ``zero`` -> both readings empty
  (0 / [] / false / {} / null); ``positive`` -> both numeric and the
  independent reading is not below the observed one (inequality direction).
  An unknown mode is never smoothed: it is named as un-adjudicated and fails.

The headline agreement is the protocol column.  Rows where strict disagrees but
the protocol predicate agrees are ADJUDICATED: recorded by name in the report
and never counted as a failure.  ``--strict-headline`` makes the strict column
decisive instead (red-team mode).

Exit: 0 every check agrees and both instruments are green; 1 protocol
disagreement(s) or un-adjudicated rows; 2 unreadable / unparseable /
non-joinable inputs; 3 joined but an instrument reported failure.  Read-only
apart from the paths given on the command line.  Deterministic output.
"""

import argparse
import json
import re
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_LIVE = "verifiers/verify_harness_claims.py"
DEFAULT_INDEPENDENT = "verifiers/verify_harness_independent.py"
RUN_TIMEOUT_S = 300

ID_KEYS = ("check", "id", "name")
IND_VALUE_KEYS = ("expected", "expected_value", "re_derived", "value", "observed")
DOTTED_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z0-9_]+)+$")
KNOWN_MODES = ("equal", "zero", "positive")


class CompareError(Exception):
    """Unreadable, unparseable or non-joinable input."""


# --------------------------------------------------------------------------
# value canonicalisation: strict, type-tagged, container-order aware
# --------------------------------------------------------------------------
def canon(value):
    if isinstance(value, bool):
        return ("bool", value)
    if isinstance(value, int):
        return ("int", value)
    if isinstance(value, float):
        return ("float", repr(value))
    if value is None:
        return ("null", "")
    if isinstance(value, str):
        return ("str", value)
    if isinstance(value, (list, tuple)):
        return ("list", tuple(canon(v) for v in value))
    if isinstance(value, dict):
        return ("dict", tuple(sorted((str(k), canon(v)) for k, v in value.items())))
    return ("other", repr(value))


def is_empty(value):
    """The protocol's emptiness predicate: 0 / [] / false / {} / null / ''."""
    if value is None or value is False:
        return True
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value == 0
    if isinstance(value, (str, list, tuple, dict)):
        return len(value) == 0
    return False


def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def predicate_agree(mode, live_value, ind_value):
    """None when the mode itself is un-adjudicated (loud, never a silent pass)."""
    if mode == "equal":
        return canon(live_value) == canon(ind_value)
    if mode == "zero":
        return is_empty(live_value) and is_empty(ind_value)
    if mode == "positive":
        if not (is_number(live_value) and is_number(ind_value)):
            return None
        return ind_value >= live_value
    return None


def show(value, limit=72):
    text = json.dumps(value, sort_keys=True) if isinstance(value, (list, dict)) else repr(value)
    if len(text) > limit:
        text = text[: limit - 1] + "\u2026"
    return text


# --------------------------------------------------------------------------
# payload parsing
# --------------------------------------------------------------------------
def extract_json(text):
    """The last balanced top-level JSON object embedded in ``text``, or None."""
    text = text.strip()
    try:
        return json.loads(text)
    except ValueError:
        pass
    depth = 0
    in_str = False
    esc = False
    start = None
    found = None
    for i, ch in enumerate(text):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            if depth:
                in_str = True
        elif ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}" and depth:
            depth -= 1
            if depth == 0 and start is not None:
                try:
                    found = json.loads(text[start : i + 1])
                except ValueError:
                    pass
                start = None
    return found


def _record_list(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("results", "rows", "checks"):
            if isinstance(payload.get(key), list):
                return payload[key]
    return None


def _dotted_map(value):
    if isinstance(value, dict) and value and all(isinstance(k, str) and DOTTED_ID.match(k) for k in value):
        return dict(value)
    return None


def _record_id(record, where):
    for key in ID_KEYS:
        if isinstance(record.get(key), str):
            return record[key]
    raise CompareError(f"{where}: record has no check id (keys {ID_KEYS}): {show(record)}")


def parse_independent(payload, statuses=None):
    """payload -> {check id: re-derived value}.  Loud on any other shape.

    ``statuses``, when given, is filled with each record's own status field
    (``status`` | ``state``) so an UNLANDED derivation can never launder into
    agreement unnoticed.
    """
    records = _record_list(payload)
    if records is not None:
        out = {}
        for i, record in enumerate(records):
            if not isinstance(record, dict):
                raise CompareError(f"independent: record {i} is not an object: {show(record)}")
            cid = _record_id(record, "independent")
            key = next((k for k in IND_VALUE_KEYS if k in record), None)
            if key is None:
                raise CompareError(
                    f"independent: record {cid} carries no value (keys {IND_VALUE_KEYS}): {show(record)}"
                )
            out[cid] = record[key]
            if statuses is not None:
                status = record.get("status", record.get("state"))
                if isinstance(status, str):
                    statuses[cid] = status
        return out
    if isinstance(payload, dict):
        for key in ("checks", "expected", "re_derived", "observations"):
            nested = _dotted_map(payload.get(key))
            if nested is not None:
                return nested
        nested = _dotted_map(payload)
        if nested is not None:
            return nested
        raise CompareError(
            "independent: payload is not keyed by check id (expected a results/rows/checks "
            "list, a flat {'<dotted.check.id>': value, ...} map, or a nested checks/expected "
            f"map); top-level keys: {show(list(payload))}"
        )
    raise CompareError(f"independent: payload is not a JSON object: {show(payload)}")


def parse_live(payload):
    """payload -> ({id: observed}, {id: verdict}, {id: mode})."""
    records = _record_list(payload)
    if records is None:
        raise CompareError(f"live: payload is not a results list: {show(payload)[:200]}")
    observed, verdicts, modes = {}, {}, {}
    for i, record in enumerate(records):
        if not isinstance(record, dict):
            raise CompareError(f"live: record {i} is not an object: {show(record)}")
        cid = _record_id(record, "live")
        if "observed" not in record:
            raise CompareError(f"live: record {cid} carries no observed value: {show(record)}")
        observed[cid] = record["observed"]
        if isinstance(record.get("verdict"), str):
            verdicts[cid] = record["verdict"]
        if isinstance(record.get("mode"), str):
            modes[cid] = record["mode"]
    return observed, verdicts, modes


# --------------------------------------------------------------------------
# run + join
# --------------------------------------------------------------------------
def run_cmd(argv, cwd):
    proc = subprocess.run(
        argv, cwd=str(cwd), capture_output=True, text=True, timeout=RUN_TIMEOUT_S
    )
    return proc.returncode, proc.stdout, proc.stderr


def load_payload(text, where):
    payload = extract_json(text)
    if payload is None:
        raise CompareError(f"{where}: no JSON object in output ({len(text)} bytes captured)")
    return payload


def compare(live, independent, modes, use_predicates=True):
    """Two columns: strict value equality and the mode-aware protocol predicate."""
    uncovered = sorted(set(live) - set(independent))
    unknown = sorted(set(independent) - set(live))
    rows = []
    for cid in sorted(live):
        if cid not in independent:
            continue
        live_value, ind_value = live[cid], independent[cid]
        mode = modes.get(cid, "equal" if not modes else "unknown")
        strict = canon(live_value) == canon(ind_value)
        protocol = predicate_agree(mode, live_value, ind_value) if use_predicates else strict
        rows.append(
            {
                "check": cid,
                "mode": mode,
                "live": live_value,
                "ind": ind_value,
                "strict": strict,
                "protocol": protocol,
            }
        )
    return {
        "rows": rows,
        "uncovered": uncovered,
        "unknown": unknown,
        "agree": [r for r in rows if (r["protocol"] if use_predicates else r["strict"]) is True],
        "disagree": [r for r in rows if (r["protocol"] if use_predicates else r["strict"]) is False],
        "strict_disagree": [r for r in rows if not r["strict"]],
        "adjudicated": [r for r in rows if not r["strict"] and r["protocol"] is True],
        "unadjudicated": [r for r in rows if r["protocol"] is None],
        "provisional": [],  # filled by the caller from the independent statuses
        "strict_agree_n": sum(1 for r in rows if r["strict"]),
    }


def annotate_statuses(res, statuses):
    """Mark agreements that rest on a non-derived independent reading as provisional.

    The instrument's own status channel (`DERIVED` / `UNLANDED` / …) is the only
    place a "could not derive it" is distinguishable from "derived emptiness",
    so without this an unlanded row could pass the `zero` emptiness predicate.
    """
    for row in res["rows"]:
        status = statuses.get(row["check"], "")
        row["ind_status"] = status
        if status and status.upper() not in ("DERIVED", "OK") and row["protocol"] is True:
            res["provisional"].append(row)
    return res


def decide_exit(res, live_n, expect_n, live_exit, ind_exit, verdicts, strict_headline=False):
    if expect_n and live_n != expect_n:
        return 2, f"live check set has {live_n} checks, expected {expect_n}"
    if res["uncovered"]:
        return 2, "uncovered checks (in live, missing from independent): " + ", ".join(res["uncovered"])
    if res["unknown"]:
        return 2, "unknown checks (in independent, absent from live): " + ", ".join(res["unknown"])
    if res["unadjudicated"]:
        return 1, "un-adjudicated mode(s): " + ", ".join(
            f"{r['check']} (mode={r['mode']})" for r in res["unadjudicated"]
        )
    decisive = res["strict_disagree"] if strict_headline else res["disagree"]
    if decisive:
        return 1, "disagreements: " + ", ".join(
            f"{r['check']} (mode={r['mode']}: expected {show(r['ind'])}, observed {show(r['live'])})"
            for r in decisive
        )
    if res["provisional"]:
        return 1, "agreement resting on unlanded derivations: " + ", ".join(
            f"{r['check']} (status={r.get('ind_status', '?')})" for r in res["provisional"]
        )
    failed = sorted(cid for cid, v in verdicts.items() if v != "PASS")
    if live_exit != 0 or ind_exit != 0 or failed:
        bits = []
        if live_exit != 0:
            bits.append(f"live exit {live_exit}")
        if ind_exit != 0:
            bits.append(f"independent exit {ind_exit}")
        if failed:
            bits.append("live non-PASS: " + ", ".join(failed))
        return 3, "all checks agree but " + "; ".join(bits)
    return 0, "all checks agree, both instruments green"


# --------------------------------------------------------------------------
# rendering
# --------------------------------------------------------------------------
def headline(meta):
    """(label, n) for the decisive column: strict when strict-headline or predicates off."""
    res = meta["result"]
    if meta.get("strict_headline"):
        return "strict value", res["strict_agree_n"]
    if not meta.get("use_predicates", True):
        return "strict value (mode predicates off)", res["strict_agree_n"]
    return "mode-aware protocol", len(res["agree"])


def summary_lines(meta):
    res = meta["result"]
    total = len(meta["live"]) + len(res["uncovered"])
    label, headline_n = headline(meta)
    return [
        f"agreement: {headline_n}/{total} ({label} headline)",
        f"columns: protocol {len(res['agree'])}/{total}; strict {res['strict_agree_n']}/{total}; "
        f"adjudicated rows: {len(res['adjudicated'])}; un-adjudicated modes: {len(res['unadjudicated'])}",
        f"disagree: {len(res['disagree'])}; uncovered: {len(res['uncovered'])}; unknown: {len(res['unknown'])}; "
        f"provisional (unlanded-based agreement): {len(res['provisional'])}",
        f"live: {meta['live_cmd']} -> exit {meta['live_exit']}, {len(meta['live'])} checks, "
        f"{sum(1 for v in meta['verdicts'].values() if v == 'PASS')} PASS",
        f"independent: {meta['ind_cmd']} -> exit {meta['ind_exit']}, {len(meta['independent'])} checks",
        f"secondary (independent expected vs live expected): {meta['secondary_agree']}/{total}",
        f"verdict: exit {meta['exit']} \u2014 {meta['reason']}",
    ]


HEADER = """# harness-independent agreement report — round 37 (C1, seat P4)

Driver: `verifiers/compare_harness_independent.py` (embeds no expected value; joins both
instruments' outputs only). Source-blindness rule honoured while building it: no harness
source, no `baseline.json` harness rows and no doc quoting them were read.

Agreement predicate follows the round-37 C1 adjudication protocol §2 (frozen surface):
`equal` -> value equality; `zero` -> both readings empty; `positive` -> numeric direction.
Strict value equality is reported alongside; rows where it fails but the predicate holds
are adjudicated and named, never smoothed.
"""


def render_markdown(meta):
    res = meta["result"]
    total = len(meta["live"]) + len(res["uncovered"])
    out = [HEADER]
    if meta.get("head"):
        out.append(f"- HEAD scanned: `{meta['head']}`")
    if meta.get("stamp"):
        out.append(f"- stamp: {meta['stamp']}")
    label, headline_n = headline(meta)
    out += [
        f"- live command: `{meta['live_cmd']}` (exit {meta['live_exit']})",
        f"- independent command: `{meta['ind_cmd']}` (exit {meta['ind_exit']})",
        f"- **agreement: {headline_n}/{total}** ({label} headline) — protocol {len(res['agree'])}/{total}, "
        f"strict {res['strict_agree_n']}/{total} — {meta['reason']}",
        "",
        "| # | check | mode | live observed | independent expected | ind status | protocol | strict |",
        "|---|-------|------|---------------|----------------------|------------|----------|--------|",
    ]
    for i, row in enumerate(res["rows"], 1):
        protocol = "n/a" if row["protocol"] is None else ("yes" if row["protocol"] else "NO")
        out.append(
            f"| {i} | `{row['check']}` | {row['mode']} | `{show(row['live'])}` | "
            f"`{show(row['ind'])}` | {row.get('ind_status') or '-'} | {protocol} | "
            f"{'yes' if row['strict'] else 'no'} |"
        )
    for cid in res["uncovered"]:
        out.append(f"| + | `{cid}` | ? | `{show(meta['live'][cid])}` | _(uncovered)_ | - | ERROR | ERROR |")
    for cid in res["unknown"]:
        out.append(f"| + | `{cid}` | ? | _(absent)_ | `{show(meta['independent'][cid])}` | - | ERROR | ERROR |")
    out += ["", "## Provisional rows (agreement resting on unlanded derivations — named, not counted)", ""]
    if res["provisional"]:
        for row in res["provisional"]:
            out.append(
                f"- `{row['check']}` (status={row.get('ind_status')}): live observed `{show(row['live'])}` vs "
                f"independent expected `{show(row['ind'])}`"
            )
    else:
        out.append("- none")
    out += ["", "## Adjudicated rows (strict unequal, protocol agreed — recorded, not smoothed)", ""]
    if res["adjudicated"]:
        for row in res["adjudicated"]:
            out.append(
                f"- `{row['check']}` (mode={row['mode']}): live observed `{show(row['live'])}` vs "
                f"independent expected `{show(row['ind'])}`"
            )
    else:
        out.append("- none")
    out += ["", "## Disagreements (named)", ""]
    if res["disagree"]:
        for row in res["disagree"]:
            out.append(
                f"- `{row['check']}` (mode={row['mode']}): live observed `{show(row['live'])}` != "
                f"independent expected `{show(row['ind'])}`"
            )
    else:
        out.append("- none")
    if res["unadjudicated"]:
        out += ["", "Un-adjudicated modes: " + ", ".join(f"`{r['check']}` ({r['mode']})" for r in res["unadjudicated"])]
    if res["uncovered"]:
        out += ["", "Uncovered (in live, missing from independent): " + ", ".join(f"`{c}`" for c in res["uncovered"])]
    if res["unknown"]:
        out += ["", "Unknown (in independent, absent from live): " + ", ".join(f"`{c}`" for c in res["unknown"])]
    failed = sorted(c for c, v in meta["verdicts"].items() if v != "PASS")
    out += [
        "",
        "## Instrument states quoted (both instruments' own outputs)",
        "",
        f"- live verdicts: {sum(1 for v in meta['verdicts'].values() if v == 'PASS')} PASS, "
        f"{len(failed)} non-PASS" + (f" ({', '.join('`' + c + '`' for c in failed)})" if failed else ""),
        f"- secondary join (independent expected vs live expected): {meta['secondary_agree']}/{total}",
        f"- driver exit: {meta['exit']} — {meta['reason']}",
        "",
    ]
    return "\n".join(out)


def render_json(meta):
    res = meta["result"]
    total = len(meta["live"]) + len(res["uncovered"])
    label, headline_n = headline(meta)
    return {
        "head": meta.get("head"),
        "headline": {"column": label, "n": headline_n, "total": total},
        "live": {
            "cmd": meta["live_cmd"],
            "exit": meta["live_exit"],
            "n": len(meta["live"]),
            "verdicts": meta["verdicts"],
            "modes": meta["modes"],
        },
        "independent": {"cmd": meta["ind_cmd"], "exit": meta["ind_exit"], "n": len(meta["independent"])},
        "agreement": {
            "n_agree_protocol": len(res["agree"]),
            "n_agree_strict": res["strict_agree_n"],
            "n_adjudicated": len(res["adjudicated"]),
            "n_disagree": len(res["disagree"]),
            "n_unadjudicated": len(res["unadjudicated"]),
            "n_provisional": len(res["provisional"]),
            "n_uncovered": len(res["uncovered"]),
            "n_unknown": len(res["unknown"]),
            "total": total,
        },
        "disagreements": [
            {"check": r["check"], "mode": r["mode"], "live_observed": r["live"], "independent_expected": r["ind"]}
            for r in res["disagree"]
        ],
        "provisional_rows": [
            {
                "check": r["check"],
                "mode": r["mode"],
                "ind_status": r.get("ind_status", ""),
                "live_observed": r["live"],
                "independent_expected": r["ind"],
            }
            for r in res["provisional"]
        ],
        "adjudicated_rows": [
            {"check": r["check"], "mode": r["mode"], "live_observed": r["live"], "independent_expected": r["ind"]}
            for r in res["adjudicated"]
        ],
        "uncovered": res["uncovered"],
        "unknown": res["unknown"],
        "secondary_agree": meta["secondary_agree"],
        "exit": meta["exit"],
        "reason": meta["reason"],
    }


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------
def self_test(quiet=False):
    failures = []
    count = 0

    def check(label, cond):
        nonlocal count
        count += 1
        ok = bool(cond)
        if not ok:
            failures.append(label)
        if not quiet:
            print(("ok " if ok else "NOT OK ") + f"{count} - {label}")
        return ok

    # canon: strict, type-tagged
    check("canon: bool is not int", canon(True) != canon(1))
    check("canon: int is not float", canon(7) != canon(7.0))
    check("canon: dict key order insignificant", canon({"a": 1, "b": 2}) == canon({"b": 2, "a": 1}))
    check("canon: list order significant", canon([1, 2]) != canon([2, 1]))
    check("canon: nested types kept distinct", canon({"x": [1, True]}) != canon({"x": [1, 1]}))

    # emptiness predicate
    check("empty: zero/[]/false/{}/null all empty", all(is_empty(v) for v in (0, 0.0, [], False, {}, None, "")))
    check("empty: 1 and 'x' not empty", not is_empty(1) and not is_empty("x"))
    check("empty: empty list != nonempty list", is_empty([]) and not is_empty([1]))

    # mode predicates
    check("predicate equal: value equality", predicate_agree("equal", 1, 1) and not predicate_agree("equal", 1, 2))
    check("predicate zero: [] vs 0 agrees", predicate_agree("zero", [], 0) is True)
    check("predicate zero: 0 vs 1 disagrees", predicate_agree("zero", 0, 1) is False)
    check("predicate positive: ind >= obs agrees", predicate_agree("positive", 7, 8) is True)
    check("predicate positive: ind < obs disagrees", predicate_agree("positive", 7, 6) is False)
    check("predicate positive: non-numeric is un-adjudicated", predicate_agree("positive", "7", 7) is None)
    check("predicate unknown mode is un-adjudicated", predicate_agree("at_least", 1, 1) is None)

    # extract_json
    check("extract_json: whole text", extract_json('{"a": 1}') == {"a": 1})
    check("extract_json: noisy stdout", extract_json('log line\n{"a": 1}\nmore') == {"a": 1})
    check("extract_json: last balanced object", extract_json('{"a": 1} tail {"b": 2}') == {"b": 2})
    check("extract_json: braces inside strings", extract_json('x {"a": "}{"} y') == {"a": "}{"})
    check("extract_json: none when absent", extract_json("no json here") is None)

    # independent payload shapes
    ind_records = {"results": [{"check": "a.b", "expected": 1}, {"check": "a.c", "expected": "x"}]}
    check("independent: results list", parse_independent(ind_records) == {"a.b": 1, "a.c": "x"})
    ind_id = {"checks": [{"id": "a.b", "re_derived": 2}, {"name": "a.c", "value": "y"}]}
    check("independent: checks list, id aliases", parse_independent(ind_id) == {"a.b": 2, "a.c": "y"})
    check("independent: flat dotted map", parse_independent({"a.b": 3, "a.c": True}) == {"a.b": 3, "a.c": True})
    check(
        "independent: rows list with value key",
        parse_independent({"rows": [{"check": "a.b", "value": 1}, {"check": "a.c", "value": "x"}]})
        == {"a.b": 1, "a.c": "x"},
    )
    check(
        "independent: nested dotted checks map beside meta keys",
        parse_independent({"checks": {"a.b": 1, "a.c": []}, "landed": 2, "unlanded": []}) == {"a.b": 1, "a.c": []},
    )
    check(
        "independent: rows preferred over a sibling checks map",
        parse_independent({"checks": {"a.b": 99}, "rows": [{"check": "a.b", "value": 1}]}) == {"a.b": 1},
    )
    check(
        "independent: nested expected map",
        parse_independent({"expected": {"a.b": 4}}) == {"a.b": 4},
    )
    check(
        "independent: observed fallback key",
        parse_independent({"results": [{"check": "a.b", "observed": 9}]}) == {"a.b": 9},
    )
    try:
        parse_independent({"omp": {"x": 1}, "opencode": {"y": 2}})
        check("independent: nested-by-subject shape rejected", False)
    except CompareError:
        check("independent: nested-by-subject shape rejected", True)
    try:
        parse_independent({"results": [{"check": "a.b"}]})
        check("independent: value-less record rejected", False)
    except CompareError:
        check("independent: value-less record rejected", True)

    # live payload shapes
    live_payload = {
        "observed": {"omp": {}},
        "results": [{"check": "a.b", "observed": 1, "verdict": "PASS", "mode": "equal"}],
    }
    live_map, verdicts, modes = parse_live(live_payload)
    check("live: results list parsed", live_map == {"a.b": 1} and verdicts == {"a.b": "PASS"} and modes == {"a.b": "equal"})
    check("live: bare list accepted", parse_live([{"id": "a.b", "observed": 5}])[0] == {"a.b": 5})
    try:
        parse_live({"observed": {}})
        check("live: shape without results rejected", False)
    except CompareError:
        check("live: shape without results rejected", True)
    try:
        parse_live({"results": [{"check": "a.b", "expected": 1}]})
        check("live: record without observed rejected", False)
    except CompareError:
        check("live: record without observed rejected", True)

    # compare + exit codes
    lv = {"a.b": 1, "a.c": "x", "a.d": [1, 2]}
    iv = {"a.b": 1, "a.c": "x", "a.d": [1, 2]}
    modes_equal = {"a.b": "equal", "a.c": "equal", "a.d": "equal"}
    verdicts_ok = {"a.b": "PASS", "a.c": "PASS", "a.d": "PASS"}
    res = compare(lv, iv, modes_equal)
    code, _ = decide_exit(res, len(lv), 3, 0, 0, verdicts_ok)
    check("compare: all agree -> exit 0", not res["disagree"] and code == 0)
    res2 = compare(lv, {"a.b": 1, "a.c": "y", "a.d": [1, 2]}, modes_equal)
    code2, reason2 = decide_exit(res2, 3, 3, 0, 0, verdicts_ok)
    check("compare: mismatch -> exit 1 naming the check", code2 == 1 and "a.c" in reason2)
    res3 = compare(lv, {"a.b": 1, "a.c": "x"}, modes_equal)
    code3, reason3 = decide_exit(res3, 3, 3, 0, 0, {})
    check("compare: uncovered -> exit 2 naming the check", code3 == 2 and "a.d" in reason3)
    res4 = compare(lv, {"a.b": 1, "a.c": "x", "a.d": [1, 2], "a.e": 1}, modes_equal)
    code4, reason4 = decide_exit(res4, 3, 3, 0, 0, {})
    check("compare: unknown -> exit 2 naming the check", code4 == 2 and "a.e" in reason4)
    code5, reason5 = decide_exit(compare(lv, iv, modes_equal), 3, 3, 0, 0, {"a.b": "DRIFT"})
    check("compare: non-PASS verdict -> exit 3 named", code5 == 3 and "a.b" in reason5)
    code6, reason6 = decide_exit(compare(lv, iv, modes_equal), 2, 3, 0, 0, {})
    check("compare: count shortfall -> exit 2 named", code6 == 2 and "expected 3" in reason6)

    # mode-aware rows: adjudicated / strict-headline / un-adjudicated
    lv_zero = {"a.b": [], "a.c": 0}
    iv_zero = {"a.b": 0, "a.c": 0}
    modes_zero = {"a.b": "zero", "a.c": "zero"}
    res_z = compare(lv_zero, iv_zero, modes_zero)
    check(
        "mode zero: [] vs 0 adjudicated, protocol agrees",
        len(res_z["adjudicated"]) == 1 and len(res_z["disagree"]) == 0 and not res_z["rows"][0]["strict"],
    )
    code_z, _ = decide_exit(res_z, 2, 2, 0, 0, {"a.b": "PASS", "a.c": "PASS"})
    check("mode zero: adjudicated row does not fail the run", code_z == 0)
    code_zs, _ = decide_exit(res_z, 2, 2, 0, 0, {"a.b": "PASS", "a.c": "PASS"}, strict_headline=True)
    check("strict-headline: adjudicated row fails", code_zs == 1)
    res_u = compare({"a.b": 1}, {"a.b": 1}, {"a.b": "at_least"})
    code_u, reason_u = decide_exit(res_u, 1, 1, 0, 0, {"a.b": "PASS"})
    check("un-adjudicated mode -> exit 1 named", code_u == 1 and "a.b" in reason_u and "at_least" in reason_u)
    res_p = compare({"a.b": 7}, {"a.b": 8}, {"a.b": "positive"})
    check("mode positive: direction preserved agrees", len(res_p["disagree"]) == 0 and len(res_p["adjudicated"]) == 1)
    check("no-mode-predicates falls back to strict", compare(lv, iv, {}, use_predicates=False)["strict_agree_n"] == 3)

    # statuses + provisional rows (an unlanded derivation must never launder into agreement)
    st = {}
    vals = parse_independent(
        {"rows": [{"check": "a.b", "value": 0, "status": "UNLANDED"}, {"check": "a.c", "value": 1, "status": "DERIVED"}]},
        st,
    )
    check(
        "status capture: rows carry their own status",
        vals == {"a.b": 0, "a.c": 1} and st == {"a.b": "UNLANDED", "a.c": "DERIVED"},
    )
    res_pr = annotate_statuses(compare({"a.b": [], "a.c": 1}, vals, {"a.b": "zero", "a.c": "equal"}), st)
    code_pr, reason_pr = decide_exit(res_pr, 2, 2, 0, 0, {"a.b": "PASS", "a.c": "PASS"})
    check(
        "provisional: unlanded-based agreement fails named",
        code_pr == 1 and "a.b" in reason_pr and "UNLANDED" in reason_pr,
    )
    res_pr2 = annotate_statuses(compare({"a.b": 5, "a.c": 1}, vals, {"a.b": "zero", "a.c": "equal"}), st)
    check(
        "provisional: a disagreeing unlanded row is a disagreement, not provisional",
        not res_pr2["provisional"] and len(res_pr2["disagree"]) == 1,
    )
    # headline column selection: the printed count must follow the decisive column
    meta_h = {"result": res_z, "strict_headline": False, "use_predicates": True}
    check("headline: default is protocol", headline(meta_h) == ("mode-aware protocol", 2))
    meta_s = {"result": res_z, "strict_headline": True, "use_predicates": True}
    check("headline: strict-headline switches label and count", headline(meta_s) == ("strict value", 1))
    meta_n = {"result": res_z, "strict_headline": False, "use_predicates": False}
    check("headline: predicates off reports strict", headline(meta_n) == ("strict value (mode predicates off)", 1))
    res_pr3 = annotate_statuses(compare({"a.b": 0, "a.c": 1}, vals, {"a.b": "zero", "a.c": "equal"}), st)
    check(
        "provisional: only the unlanded row is provisional; the derived row stays ordinary",
        [r["check"] for r in res_pr3["provisional"]] == ["a.b"] and not res_pr3["disagree"],
    )

    # end-to-end CLI against stub instruments in a throwaway temp tree
    stub_live = (
        "import json;print(json.dumps({'results':["
        "{'check':'a.b','observed':1,'verdict':'PASS','mode':'equal'},"
        "{'check':'a.c','observed':'x','verdict':'PASS','mode':'equal'}]}))"
    )
    stub_ind_ok = (
        "import json;print(json.dumps({'results':["
        "{'check':'a.b','expected':1},{'check':'a.c','expected':'x'}]}))"
    )
    stub_ind_bad = (
        "import json;print(json.dumps({'results':["
        "{'check':'a.b','expected':1},{'check':'a.c','expected':'y'}]}))"
    )
    stub_live_red = (
        "import json,sys;print(json.dumps({'results':["
        "{'check':'a.b','observed':1,'verdict':'DRIFT','mode':'equal'},"
        "{'check':'a.c','observed':'x','verdict':'PASS','mode':'equal'}]}));sys.exit(1)"
    )
    with tempfile.TemporaryDirectory(prefix="cmp-ind-selftest-") as tmp:
        tmp_path = Path(tmp)
        for name, body in (
            ("live.py", stub_live),
            ("ind_ok.py", stub_ind_ok),
            ("ind_bad.py", stub_ind_bad),
            ("live_red.py", stub_live_red),
        ):
            (tmp_path / name).write_text(body + "\n")
        report = tmp_path / "report.md"

        def e2e(name, live, indi, want_exit=0, want_text=""):
            argv = [
                sys.executable,
                str(Path(__file__).resolve()),
                "--live-cmd",
                f"{sys.executable} {tmp_path / live}",
                "--independent-cmd",
                f"{sys.executable} {tmp_path / indi}",
                "--expect-n",
                "2",
                "--no-stamp",
            ]
            proc = subprocess.run(argv, capture_output=True, text=True, timeout=120)
            check(
                f"cli: {name} -> exit {want_exit}",
                proc.returncode == want_exit and (want_text in proc.stdout if want_text else True),
            )
            return proc

        e2e("agreeing stubs", "live.py", "ind_ok.py", want_text="agreement: 2/2")
        e2e("mismatched stub", "live.py", "ind_bad.py", want_exit=1, want_text="a.c")
        e2e("red live instrument", "live_red.py", "ind_ok.py", want_exit=3)
        proc = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--live-cmd",
                f"{sys.executable} {tmp_path / 'live.py'}",
                "--independent",
                str(tmp_path / "absent_instrument.py"),
                "--expect-n",
                "2",
                "--no-stamp",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        check(
            "cli: absent default instrument -> exit 2 named",
            proc.returncode == 2 and "missing independent instrument" in proc.stderr,
        )
        proc = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--live-cmd",
                f"{sys.executable} {tmp_path / 'live.py'}",
                "--independent-cmd",
                f"{sys.executable} {tmp_path / 'missing.py'}",
                "--expect-n",
                "2",
                "--no-stamp",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        check("cli: failing independent command -> exit 2", proc.returncode == 2)
        subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--live-cmd",
                f"{sys.executable} {tmp_path / 'live.py'}",
                "--independent-cmd",
                f"{sys.executable} {tmp_path / 'ind_ok.py'}",
                "--expect-n",
                "2",
                "--no-stamp",
                "--report",
                str(report),
                "--json",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        body = report.read_text() if report.exists() else ""
        check(
            "cli: markdown report written with 2/2 header",
            "agreement: 2/2" in body and "| `a.b` |" in body,
        )
    print(f"self-test: {len(failures)} failure(s) over {count} assertions")
    for label in failures:
        print(f"  FAILED: {label}")
    return len(failures)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def git_head(cwd):
    try:
        proc = subprocess.run(
            ["git", "-C", str(cwd), "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            timeout=20,
        )
        return proc.stdout.strip() if proc.returncode == 0 else "unknown"
    except (OSError, subprocess.SubprocessError):
        return "unknown"


def build_meta(args):
    cwd = Path(args.cwd).resolve()
    if args.live_json:
        text = Path(args.live_json).read_text()
        live_cmd, live_exit = f"file:{args.live_json}", 0
    else:
        live_cmd = args.live_cmd
        live_exit, text, live_err = run_cmd(shlex.split(live_cmd), cwd)
        if live_exit != 0 and not text.strip():
            raise CompareError(f"live instrument failed with no stdout: exit {live_exit}: {live_err.strip()[:300]}")
    live_payload = load_payload(text, "live")
    live, verdicts, modes = parse_live(live_payload)

    if args.independent_json:
        text = Path(args.independent_json).read_text()
        ind_cmd, ind_exit = f"file:{args.independent_json}", 0
    elif args.independent_cmd:
        ind_cmd = args.independent_cmd
        ind_exit, text, ind_err = run_cmd(shlex.split(ind_cmd), cwd)
        if ind_exit != 0 and not text.strip():
            raise CompareError(
                f"independent instrument failed with no stdout: exit {ind_exit}: {ind_err.strip()[:300]}"
            )
    else:
        ind_path = Path(args.independent) if Path(args.independent).is_absolute() else cwd / args.independent
        if not ind_path.exists():
            raise CompareError(
                f"missing independent instrument: {ind_path} (the C1 re-derivation seat has not "
                "landed it yet, or --independent is wrong)"
            )
        ind_cmd = f"{shlex.quote(sys.executable)} {shlex.quote(str(ind_path))} --json"
        ind_exit, text, ind_err = run_cmd(shlex.split(ind_cmd), cwd)
        if ind_exit != 0 and not text.strip():
            raise CompareError(
                f"independent instrument failed with no stdout: exit {ind_exit}: {ind_err.strip()[:300]}"
            )
    statuses = {}
    independent = parse_independent(load_payload(text, "independent"), statuses)

    res = annotate_statuses(
        compare(live, independent, modes, use_predicates=not args.no_mode_predicates), statuses
    )
    exit_code, reason = decide_exit(
        res, len(live), args.expect_n, live_exit, ind_exit, verdicts, strict_headline=args.strict_headline
    )

    # secondary join, recorded for the adjudicating seat but never the headline:
    # the harness's own expected values (from its JSON) vs the independent ones.
    expected_map = {}
    for record in _record_list(live_payload) or []:
        if isinstance(record, dict) and "expected" in record:
            expected_map[_record_id(record, "live")] = record["expected"]
    secondary = sum(
        1 for cid, v in independent.items() if cid in expected_map and canon(v) == canon(expected_map[cid])
    )

    return {
        "head": git_head(cwd),
        "live": live,
        "verdicts": verdicts,
        "modes": modes,
        "independent": independent,
        "result": res,
        "live_cmd": live_cmd,
        "live_exit": live_exit,
        "ind_cmd": ind_cmd,
        "ind_exit": ind_exit,
        "secondary_agree": secondary,
        "exit": exit_code,
        "reason": reason,
        "strict_headline": args.strict_headline,
        "use_predicates": not args.no_mode_predicates,
        "stamp": "" if args.no_stamp else args.stamp,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="C1 agreement driver: join the live harness observation with a source-blind "
        "independent re-derivation and report N/28."
    )
    parser.add_argument("--independent", default=DEFAULT_INDEPENDENT, help="path to the independent instrument")
    parser.add_argument("--independent-cmd", default=None, help="override the independent command line")
    parser.add_argument("--live-cmd", default=f"{shlex.quote(sys.executable)} {DEFAULT_LIVE} --json")
    parser.add_argument("--independent-json", default=None, help="consume a captured independent JSON instead of running it")
    parser.add_argument("--live-json", default=None, help="consume a captured live JSON instead of running the harness")
    parser.add_argument("--expect-n", type=int, default=28, help="expected live check count (0 disables)")
    parser.add_argument("--cwd", default=str(REPO), help="repo root to run in and scan")
    parser.add_argument("--json", action="store_true", help="emit the machine-readable report on stdout")
    parser.add_argument("--report", default=None, help="write the markdown agreement report to this path")
    parser.add_argument("--stamp", default="", help="free-text provenance line for the markdown report")
    parser.add_argument("--no-stamp", action="store_true", help="omit the stamp line")
    parser.add_argument(
        "--strict-headline", action="store_true", help="make strict value equality decisive (red-team mode)"
    )
    parser.add_argument(
        "--no-mode-predicates", action="store_true", help="ignore the live mode field; strict equality only"
    )
    parser.add_argument("--self-test", action="store_true", help="check the driver's own model")
    args = parser.parse_args(argv)

    if args.self_test:
        return 1 if self_test() else 0

    try:
        meta = build_meta(args)
    except CompareError as exc:
        print(f"compare_harness_independent: ERROR: {exc}", file=sys.stderr)
        return 2
    except (OSError, subprocess.SubprocessError, ValueError) as exc:
        print(f"compare_harness_independent: ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        # machine-readable stdout: JSON only, so `--json > file` is directly parseable
        if args.report:
            Path(args.report).write_text(render_markdown(meta) + "\n")
            print(f"report: {args.report}", file=sys.stderr)
        print(json.dumps(render_json(meta), indent=2, sort_keys=True))
        return meta["exit"]
    for line in summary_lines(meta):
        print(line)
    if args.report:
        Path(args.report).write_text(render_markdown(meta) + "\n")
        print(f"report: {args.report}")
    return meta["exit"]


if __name__ == "__main__":
    sys.exit(main())