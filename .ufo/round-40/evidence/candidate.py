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

Scoped-out rows (round 38, seat P1 — C1 closure; hardened round 39, seat P1).
A row the independent instrument cannot derive blind is not a disagreement and
must not be smoothed into agreement either: the instrument publishes it with
status ``SCOPED_OUT`` and a non-empty reason, plus a top-level ``scoped_out``
map.  Round 38 read that set from the payload under test and validated only its
*shape*, so a builder that simply failed to derive a row could declare it
scoped out (in both payload channels plus the map) and the row left the join
with no failure — a self-consistent declaration was enough to launder a real
disagreement into exit 0 (r38 R1-D1, HIGH).

Round 39 closes that hole with three independent locks, none of which the
payload under test controls:

1. **The set is read from a committed file**, ``verifiers/harness-independent-scope.json``
   (``--scope-file``), not from the payload.  A scope-out exists because that
   file lists it.  The payload's own declaration must match the committed set
   exactly: a row declared scoped out that the file does not list is exit 2 (the
   laundering shape), and a committed row the payload no longer declares is exit
   2 (an undeclared deletion).
2. **Every scoped row must carry a machine-checkable probe** — a blind,
   value-free structural census (kind ``structural-census``) the driver
   *recomputes itself* from the substrate root the committed file pins.  The
   declared observable must equal the recomputed one exactly and must be
   non-vacuous, and the probe's falsifying tokens must be absent.  A fabricated
   or redirected probe is exit 2.
3. **The blocker's falsifier is checked**: the strings whose presence would put
   the rule back inside the substrate set are swept for; any occurrence is exit
   2.

So a genuine disagreement cannot self-declare its way out of the join: the
declaration needs a committed entry *and* a probe whose recomputed fact holds.
Scoped-out rows still leave the join entirely: they are listed by name in both
report shapes, they never count as agreement (the numerator cannot gain from a
scope-out, only the denominator narrows), and the headline is stated over the
landed scope.  ``--expect-n`` still covers the live check set.

Freeze-before-compare receipt (round 38, seat P2 — A1-D1).  The protocol's §6
receipt is executable here: ``--receipt FILE`` writes, per run, the sha256 and
byte count of the exact bytes the join consumed on *both* sides (the captured
file bytes under ``--live-json`` / ``--independent-json``, or the instrument's
stdout text under a live run), the instrument file hashes where the path is
known, and the full invocation record (each side's producer command plus this
driver's own argv and verdict).  The hashes are taken at input read, before the
join runs, so a reader can check the ordering from the receipt alone; the
strongest form — both sides consumed from files captured by their own
instruments — is labelled ``frozen-inputs``, a live capture is labelled
``live-capture`` (a narrowing, not a proof: the residue stays stated in the
corpus doc's §5).  Receipts are JSON, deterministic apart from the timestamp.

Exit: 0 every check agrees and both instruments are green; 1 protocol
disagreement(s) or un-adjudicated rows; 2 unreadable / unparseable /
non-joinable inputs; 3 joined but an instrument reported failure.  Read-only
apart from the paths given on the command line (and ``--receipt``).
Deterministic output.
"""

import argparse
import hashlib
import json
import re
import shlex
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_LIVE = "verifiers/verify_harness_claims.py"
DEFAULT_SCOPE = "verifiers/harness-independent-scope.json"
DEFAULT_INDEPENDENT = "verifiers/verify_harness_independent.py"
RUN_TIMEOUT_S = 300

ID_KEYS = ("check", "id", "name")
IND_VALUE_KEYS = ("expected", "expected_value", "re_derived", "value", "observed")
DOTTED_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z0-9_]+)+$")
KNOWN_MODES = ("equal", "zero", "positive")
SCOPE_KINDS = ("rule-in-author-scope", "substrate-absent", "external-authority")
ISO_STAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z")
ENTRY_LINE_RE = re.compile(r"(?m)^\s*-\s+\S")
_PROBE_CACHE = {}


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


def _reconcile_channels(payload, where):
    """CROSS-CHANNEL RECONCILIATION (T1 candidate, round 40).

    R1's r39 F-3: ``_record_list`` reads only the FIRST of results/rows/checks, so a
    divergent value hidden in a later channel is never read.  Here every published
    list channel is parsed and must agree record-for-record on the value each
    publishes; a divergence is a loud error, never a silent first-wins.

    Returns the reconciled {check id: value} or raises CompareError.
    """
    if not isinstance(payload, dict):
        return None
    channels = {}
    for key in ("results", "rows", "checks"):
        if isinstance(payload.get(key), list):
            channels[key] = payload[key]
    if not channels:
        return None
    parsed = {}
    for key, records in channels.items():
        out = {}
        for i, record in enumerate(records):
            if not isinstance(record, dict):
                raise CompareError(f"{where}: {key}[{i}] is not an object: {show(record)}")
            cid = _record_id(record, where)
            vkeys = [k for k in IND_VALUE_KEYS if k in record]
            if not vkeys:
                raise CompareError(
                    f"{where}: record {cid} carries no value (keys {IND_VALUE_KEYS}): {show(record)}"
                )
            out[cid] = (vkeys, record)
        parsed[key] = out
    names = sorted(parsed)
    base_key = names[0]
    base_map = parsed[base_key]
    for key in names[1:]:
        other = parsed[key]
        for cid in sorted(set(base_map) & set(other)):
            b_keys, b_rec = base_map[cid]
            o_keys, o_rec = other[cid]
            # compare the value under each channel's own highest-priority key
            b_val = b_rec[b_keys[0]]
            o_val = o_rec[o_keys[0]]
            if canon(b_val) != canon(o_val):
                raise CompareError(
                    f"{where}: channel divergence for {cid}: {base_key}.{b_keys[0]}="
                    f"{show(b_val)} but {key}.{o_keys[0]}={show(o_val)} "
                    f"(all published channels must agree; a divergent value cannot hide "
                    f"behind a clean one)"
                )
        only_base = sorted(set(base_map) - set(other))
        only_other = sorted(set(other) - set(base_map))
        if only_base or only_other:
            raise CompareError(
                f"{where}: channel membership differs between {base_key} and {key}: "
                f"only in {base_key}: {only_base}; only in {key}: {only_other}"
            )
    # the dotted-map channel (`checks`): the live instrument publishes it as a
    # {check id: value} mapping beside the two list channels, so reconciling only
    # the lists leaves it as a hiding place (measured: payload C reads exit 0
    # against a list-only reconciliation).
    map_channel = _dotted_map(payload.get("checks"))
    if map_channel is not None:
        for cid, val in sorted(map_channel.items()):
            if cid in base_map:
                if canon(val) != canon(base_map[cid][1][base_map[cid][0][0]]):
                    raise CompareError(
                        f"{where}: channel divergence for {cid}: checks={show(val)} but "
                        f"{base_key}.{base_map[cid][0][0]}="
                        f"{show(base_map[cid][1][base_map[cid][0][0]])} "
                        f"(the dotted-map channel must agree with the list channels)"
                    )
    return {cid: rec[keys[0]] for cid, (keys, rec) in base_map.items()}


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
            vkeys = [k for k in IND_VALUE_KEYS if k in record]
            if not vkeys:
                raise CompareError(
                    f"independent: record {cid} carries no value (keys {IND_VALUE_KEYS}): {show(record)}"
                )
            # WITHIN-RECORD CROSS-CHECK (T1 candidate, round 40 — R1's F-2):
            # the F-2 payload is a record that carries a harness-side `expected`
            # ALONGSIDE a derived channel reading "NOT DERIVED".  The two must
            # agree; an explicit non-derivation cannot be outranked by a
            # harvested value.  A record carrying ONLY `expected` is a documented
            # shape (the driver's own self-test pins it and the flat/nested map
            # forms are contract), so it is not rejected here — the channel
            # reconciliation below is what closes that door.
            derived = [k for k in ("re_derived", "value", "observed") if k in record]
            foreign = [k for k in ("expected", "expected_value") if k in record]
            if foreign and derived:
                fval = record[foreign[0]]
                for dk in derived:
                    dval = record[dk]
                    if isinstance(dval, str) and dval.strip().upper() in (
                        "NOT DERIVED", "NOT-DERIVED", "UNDERIVED", "N/A"
                    ):
                        raise CompareError(
                            f"independent: record {cid} claims {foreign[0]}={show(fval)} while "
                            f"{dk} reads {show(dval)}; a harvested value cannot outrank an "
                            f"explicit non-derivation: {show(record)}"
                        )
                    if canon(dval) != canon(fval):
                        raise CompareError(
                            f"independent: record {cid} disagrees with itself: "
                            f"{foreign[0]}={show(fval)} vs {dk}={show(dval)} "
                            f"(the value channels must agree)"
                        )
            out[cid] = record[vkeys[0]]
            if statuses is not None:
                status = record.get("status", record.get("state"))
                if isinstance(status, str):
                    statuses[cid] = status
        # cross-channel reconciliation: a divergent value hidden in `rows`/`checks`
        # behind a clean `results` is a loud error, never a silent first-wins (F-3)
        reconciled = _reconcile_channels(payload, "independent")
        if reconciled is not None and len(reconciled) == len(out):
            for cid in out:
                if canon(reconciled[cid]) != canon(out[cid]):
                    raise CompareError(
                        f"independent: {cid} reads {show(out[cid])} in the first list channel "
                        f"but {show(reconciled[cid])} when all channels are reconciled"
                    )
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


def compare(live, independent, modes, use_predicates=True, scoped_out=None):
    """Two columns: strict value equality and the mode-aware protocol predicate.

    ``scoped_out`` (round 38) is the independent instrument's own declared set of
    rows it cannot derive blind.  Those rows leave the join by name: they are
    never counted as agreement or disagreement, and they do not read as
    "uncovered" (a scope-out is a declared exclusion, not a missing reading).
    A scoped-out id the live side does not carry is recorded separately so the
    caller can fail loudly rather than let an invented id hide there.
    """
    scoped_out = scoped_out or {}
    covered = set(independent) | set(scoped_out)
    uncovered = sorted(set(live) - covered)
    unknown = sorted(set(covered) - set(live))
    rows = []
    for cid in sorted(live):
        if cid not in independent or cid in scoped_out:
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
        "scoped_out_rows": sorted(cid for cid in scoped_out if cid in live),
        "scoped_out": {cid: scoped_out[cid] for cid in sorted(scoped_out)},
        "scoped_out_absent_from_live": sorted(set(scoped_out) - set(live)),
    }


def parse_scoped_out(payload, independent):
    """The independent payload's own scoped-out declaration, validated loudly.

    Round-38 C1 closure: a row the independent instrument cannot derive blind is
    neither a disagreement nor agreement.  It publishes the set; this driver
    checks it is well formed — every name present in the independent payload,
    its own status literally ``SCOPED_OUT``, and a non-empty reason — and
    returns {check id: reason}.  Any other shape is a loud error (exit 2): a
    scope-out must never be a way to make a check disappear quietly.
    """
    if not isinstance(payload, dict):
        return {}
    raw = payload.get("scoped_out")
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise CompareError(
            f"independent: scoped_out is not a mapping: {show(raw)}")
    if not raw:
        raise CompareError(
            "independent: scoped_out is present but empty (declare the set or "
            "omit the key; an empty declaration is ambiguous)")
    statuses = {}
    records = _record_list(payload)
    if records is not None:
        for record in records:
            if isinstance(record, dict):
                status = record.get("status", record.get("state"))
                if isinstance(status, str):
                    statuses[_record_id(record, "independent")] = status
    out = {}
    for cid, reason in raw.items():
        if cid not in independent:
            raise CompareError(
                f"independent: scoped_out names {cid}, absent from its own "
                f"payload (a scope-out must not hide an unlanded row)")
        status = statuses.get(cid, "")
        if status != "SCOPED_OUT":
            raise CompareError(
                f"independent: scoped_out names {cid} but its status is "
                f"{status!r}, not 'SCOPED_OUT'")
        if not (isinstance(reason, str) and reason.strip()):
            raise CompareError(
                f"independent: scoped_out reason for {cid} is empty (the "
                f"blocker must be named, never silent)")
        out[cid] = reason
    return out


def load_scope_file(path):
    """The committed scope-out set: {check id: entry}, read from a repo file.

    Round 39 (C1, seat P1).  This is lock 1 against the r38 laundering hole: the
    set of rows allowed to leave the join is committed, so it cannot be extended
    by the payload under test.  Each entry carries the blocker kind and the
    probe contract the driver will recompute.
    """
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise CompareError(f"scope file unreadable: {path}: {exc}") from exc
    try:
        document = json.loads(raw)
    except ValueError as exc:
        raise CompareError(f"scope file is not JSON: {path}: {exc}") from exc
    if not isinstance(document, dict):
        raise CompareError(f"scope file is not an object: {path}: {show(document)}")
    entries = document.get("scope_out")
    if entries is None:
        raise CompareError(f"scope file carries no 'scope_out' mapping: {path}")
    if not isinstance(entries, dict):
        raise CompareError(
            f"scope file 'scope_out' is not a mapping: {path}: {show(entries)}")
    out = {}
    for cid, entry in entries.items():
        if not isinstance(entry, dict):
            raise CompareError(f"scope file row {cid} is not an object: {show(entry)}")
        if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
            raise CompareError(f"scope file row {cid} carries no blocker reason")
        if entry.get("kind") not in SCOPE_KINDS:
            raise CompareError(
                f"scope file row {cid} has kind {entry.get('kind')!r}, not one of "
                f"{SCOPE_KINDS}")
        out[cid] = entry
    contract = document.get("probe_contract")
    return out, contract if isinstance(contract, dict) else {}


def recompute_probe(probe):
    """Recompute a scoped row's blind probe in this process; return its observable.

    Lock 2 against the laundering hole.  The probe is deliberately narrow: it is
    a *structural census*, not the row's value (the value needs the rule the
    instrument may not read).  It answers the question the blocker actually
    rests on — is the carrier surface large, and does the row's value move when
    a blind builder varies the rule it cannot see? — and it is computed here
    rather than trusted from the payload.

    A substring sweep for the rule's own literals was tried first and rejected:
    the carrier is this lane's own session tree, so its transcripts *quote* the
    rule's text (measured: `min(10, len(known))` occurs in
    `KotobaLane.jsonl` and others), and any such sweep fails the true rows.  The
    census below is the sound form: it reads structure, never prose.

    Only ``rule-spread-census`` is defined; any other kind is a loud error, so a
    future probe shape cannot slip through as un-verified.
    """
    kind = probe.get("kind")
    if kind != "rule-spread-census":
        raise CompareError(f"probe kind {kind!r} is not 'rule-spread-census'")
    target = probe.get("target")
    if not isinstance(target, str) or not target.startswith("/"):
        raise CompareError(
            f"probe target must be an absolute path (relative targets would be "
            f"resolved against the wrong tree): {show(target)}")
    key = (kind, target)
    if key in _PROBE_CACHE:
        return _PROBE_CACHE[key]
    carrier = Path(target)
    if not carrier.is_dir():
        raise CompareError(f"probe target is not a directory: {target}")
    cands = []
    session_files = files_with_block = 0
    for path in sorted(carrier.rglob("*.jsonl")):
        session_files += 1
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        stamps = ISO_STAMP_RE.findall(text)
        newest = max(stamps) if stamps else ""
        mtime = path.stat().st_mtime
        start = 0
        while True:
            start = text.find("<skills>", start)
            if start < 0:
                break
            end = text.find("</skills>", start)
            if end < 0:
                break
            block = text[start:end].replace("\\n", "\n")
            cands.append({
                "entries": len(ENTRY_LINE_RE.findall(block)),
                "newest_stamp": newest,
                "mtime": mtime,
                "order": len(cands),
            })
            start = end + len("</skills>")
        if text.count("<skills>"):
            files_with_block += 1
    if not cands:
        raise CompareError(f"probe target carries no candidate block: {target}")
    rule_totals = {}
    for name, picker in (
        ("newest-mtime", lambda c: (c["mtime"], -c["order"])),
        ("newest-iso-stamp", lambda c: (c["newest_stamp"], -c["order"])),
        ("first-in-scan-order", lambda c: (-c["order"],)),
        ("last-in-scan-order", lambda c: (c["order"],)),
        ("newest-nonempty", lambda c: (c["mtime"],) if c["entries"] else (-1, 0,)),
    ):
        chosen = max(cands, key=picker)
        rule_totals[name] = chosen["entries"]
    out = {
        "observable": {
            "session_files": session_files,
            "files_with_skills_block": files_with_block,
            "candidate_blocks": len(cands),
            "distinct_totals": sorted(set(rule_totals.values())),
            "rule_totals": rule_totals,
        },
        "present_tokens": [],
    }
    _PROBE_CACHE[key] = out
    return out


def check_scope_probes(scoped_out, probes, committed, contract, statuses=None):
    """Validate every scoped row against the committed set and its own probe.

    Failure classes, each named and each exit 2 by the caller:

    * **laundering** — the payload declares a row scoped out that the committed
      file does not list.  This is r38 R1-D1's exact shape: a real disagreement
      (or a row the builder merely failed to derive) cannot buy its way out of
      the join by declaring itself out; the set is committed, not self-served.
      This is the decisive lock, and it is the one the payload cannot reach.
    * **channel split** — a record whose own status says ``SCOPED_OUT`` while the
      payload's ``scoped_out`` map omits it (or the reverse).  The two channels
      must agree, or a row could leave one and re-enter the other.
    * **false blocker** — the declared probe does not survive recomputation: a
      probe block that is missing, misdirected, vacuous, whose declared
      observable disagrees with the recomputed census, or whose blind-plausible
      rules all land on one total (which would mean the row *is* derivable blind
      and the scope-out is a false claim).

    Deliberately NOT a failure: a committed row the payload now derives.  That is
    the comparison getting *stronger* — the row re-enters the join and is checked
    like any other — and the join's own uncovered/unknown rules already cover a
    row that merely vanishes.  Failing it would punish a builder for succeeding.

    The committed set may legitimately be empty (a tree with no scope-outs): then
    any payload scope-out is laundering, and the live join proceeds normally.
    """
    problems = []
    for cid, status in sorted((statuses or {}).items()):
        if status == "SCOPED_OUT" and cid not in scoped_out:
            problems.append(
                f"channel split: record {cid} carries status SCOPED_OUT but the "
                f"payload's scoped_out map omits it (declare it in both channels)")
        elif status != "SCOPED_OUT" and cid in scoped_out:
            problems.append(
                f"channel split: {cid} is in the scoped_out map but its own record "
                f"status is {status!r}, not 'SCOPED_OUT'")
    for cid in sorted(scoped_out):
        if cid not in committed:
            problems.append(
                f"laundering: the payload scopes out {cid}, which the committed scope "
                f"file does not list (a scope-out must be committed, not self-declared)")
    for cid in sorted(scoped_out):
        if cid not in committed:
            continue
        probe = probes.get(cid)
        if not isinstance(probe, dict):
            problems.append(
                f"false blocker: scoped row {cid} carries no probe block (a blocker "
                f"without a recomputable probe is an assertion, not a measurement)")
            continue
        declared_kind = contract.get("kind")
        if declared_kind and probe.get("kind") != declared_kind:
            problems.append(
                f"false blocker: scoped row {cid} probe kind {probe.get('kind')!r} does "
                f"not match the committed contract kind {declared_kind!r}")
            continue
        declared = probe.get("observable")
        try:
            recomputed = recompute_probe(probe)
        except CompareError as exc:
            problems.append(f"false blocker: scoped row {cid}: {exc}")
            continue
        if declared != recomputed["observable"]:
            problems.append(
                f"false blocker: scoped row {cid} declares observable "
                f"{show(declared)} but recomputation gives {show(recomputed['observable'])}")
            continue
        obs = recomputed["observable"]
        if obs["session_files"] == 0 or obs["candidate_blocks"] == 0:
            problems.append(
                f"false blocker: scoped row {cid} probe is vacuous "
                f"({show(obs)}): 'cannot derive' must not rest on an empty surface")
        elif len(obs.get("distinct_totals") or []) < 2:
            problems.append(
                f"false blocker: scoped row {cid}: every blind-plausible rule agrees "
                f"on one total {show(obs.get('distinct_totals'))}, so the row is "
                f"derivable without reading the harness's rule and is not out of scope")
    if problems:
        raise CompareError("; ".join(problems))
    return True


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


def scope_totals(meta):
    """(joined_n, scope_n, live_n) — the headline is stated over the joined scope.

    Round 38: scoped-out rows stay in ``live`` (the instrument's check set) but
    leave the join, so they narrow the denominator instead of the numerator.  A
    scope-out can therefore never buy agreement; it can only shrink the claim.
    """
    res = meta["result"]
    joined_n = len(res["rows"])
    scope_n = joined_n + len(res["uncovered"])
    live_n = len(meta["live"]) + len(res["uncovered"])
    return joined_n, scope_n, live_n


def decide_exit(res, live_n, expect_n, live_exit, ind_exit, verdicts, strict_headline=False):
    if expect_n and live_n != expect_n:
        return 2, f"live check set has {live_n} checks, expected {expect_n}"
    if res["scoped_out_absent_from_live"]:
        return 2, ("scoped-out ids absent from the live check set: "
                   + ", ".join(res["scoped_out_absent_from_live"]))
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
    joined_n, scope_n, live_n = scope_totals(meta)
    label, headline_n = headline(meta)
    return [
        f"agreement: {headline_n}/{scope_n} ({label} headline; {live_n} live checks, "
        f"{len(res['scoped_out'])} scoped out by the independent instrument)",
        f"columns: protocol {len(res['agree'])}/{scope_n}; strict {res['strict_agree_n']}/{scope_n}; "
        f"adjudicated rows: {len(res['adjudicated'])}; un-adjudicated modes: {len(res['unadjudicated'])}",
        f"disagree: {len(res['disagree'])}; uncovered: {len(res['uncovered'])}; unknown: {len(res['unknown'])}; "
        f"provisional (unlanded-based agreement): {len(res['provisional'])}; scoped-out: {len(res['scoped_out'])}",
        f"live: {meta['live_cmd']} -> exit {meta['live_exit']}, {len(meta['live'])} checks, "
        f"{sum(1 for v in meta['verdicts'].values() if v == 'PASS')} PASS",
        f"independent: {meta['ind_cmd']} -> exit {meta['ind_exit']}, {len(meta['independent'])} checks",
        f"secondary (independent expected vs live expected): {meta['secondary_agree']}/{scope_n}",
        f"verdict: exit {meta['exit']} \u2014 {meta['reason']}",
    ]


HEADER = """# harness-independent agreement report — round 37/38 (C1, seats P4/P1)

Driver: `verifiers/compare_harness_independent.py` (embeds no expected value; joins both
instruments' outputs only). Source-blindness rule honoured while building it: no harness
source, no `baseline.json` harness rows and no doc quoting them were read.

Agreement predicate follows the round-37 C1 adjudication protocol §2 (frozen surface):
`equal` -> value equality; `zero` -> both readings empty; `positive` -> numeric direction.
Strict value equality is reported alongside; rows where it fails but the predicate holds
are adjudicated and named, never smoothed.

Round-38 C1 closure: rows the independent instrument scopes out (status `SCOPED_OUT`,
blocker named by that instrument) leave the join by name and are listed below with their
blockers. The headline is stated over the joined scope, so a scope-out can only narrow
the claim, never add to the numerator.
"""


def render_markdown(meta):
    res = meta["result"]
    joined_n, scope_n, live_n = scope_totals(meta)
    out = [HEADER]
    if meta.get("head"):
        out.append(f"- HEAD scanned: `{meta['head']}`")
    if meta.get("stamp"):
        out.append(f"- stamp: {meta['stamp']}")
    label, headline_n = headline(meta)
    out += [
        f"- live command: `{meta['live_cmd']}` (exit {meta['live_exit']})",
        f"- independent command: `{meta['ind_cmd']}` (exit {meta['ind_exit']})",
        f"- **agreement: {headline_n}/{scope_n}** ({label} headline over the joined scope; "
        f"{live_n} live checks, {len(res['scoped_out'])} scoped out) — protocol {len(res['agree'])}/{scope_n}, "
        f"strict {res['strict_agree_n']}/{scope_n} — {meta['reason']}",
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
    out += ["", "## Scoped out by the independent instrument (blocker named — not a disagreement, not agreement)", ""]
    if res["scoped_out"]:
        for cid, reason in res["scoped_out"].items():
            out.append(f"- `{cid}`: {reason}")
    else:
        out.append("- none")
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
        f"- secondary join (independent expected vs live expected): {meta['secondary_agree']}/{scope_n}",
        f"- driver exit: {meta['exit']} — {meta['reason']}",
        "",
    ]
    return "\n".join(out)


def render_json(meta):
    res = meta["result"]
    joined_n, scope_n, live_n = scope_totals(meta)
    label, headline_n = headline(meta)
    return {
        "head": meta.get("head"),
        "headline": {"column": label, "n": headline_n, "total": scope_n,
                     "joined_scope": scope_n, "live_checks": live_n},
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
            "n_scoped_out": len(res["scoped_out"]),
            "total": scope_n,
        },
        "scoped_out": res["scoped_out"],
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
def side_receipt(text, cmd, exit_code, json_path, cwd):
    """One side's frozen-input record: the exact bytes the join consumed.

    ``sha256`` is taken from the captured text at input-read time, before any
    join runs.  When the side came from a file (``--live-json`` /
    ``--independent-json``) the file's own digest is recorded as the source of
    truth; otherwise the captured stdout text is hashed and labelled as such.
    """
    payload = text.encode("utf-8")
    record = {
        "cmd": cmd,
        "exit": exit_code,
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }
    if json_path:
        path = Path(json_path)
        record["source"] = f"file:{json_path}"
        record["file_exists"] = path.is_file()
        if path.is_file():
            record["file_bytes"] = path.stat().st_size
            record["file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    else:
        record["source"] = "stdout-capture"
    return record


def render_receipt(meta, argv, cwd):
    """The freeze-before-compare receipt (protocol §6, A1-D1), executable.

    Both sides' input digests plus the invocation record.  The receipt is a
    *narrowing* of the blindness residue, not a proof; its mode field says
    which form it is: ``frozen-inputs`` (both sides consumed from files
    captured beforehand) or ``live-capture`` (at least one side's bytes are
    this run's own stdout).
    """
    frozen = bool(meta.get("live_json_used") and meta.get("ind_json_used"))
    instruments = {}
    for name, rel in (("harness", DEFAULT_LIVE), ("independent", DEFAULT_INDEPENDENT)):
        path = cwd / rel
        instruments[name] = {
            "path": rel,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None,
        }
    # Round 39 (C1, seat P1): the committed scope-out set is a lock on the
    # headline, so its bytes are recorded here too.  A receipt that names the two
    # instruments but not the scope file cannot show which scope the join ran under.
    scope_path = Path(meta.get("scope_file") or "")
    if not scope_path.is_absolute():
        scope_path = cwd / scope_path
    scope_record = {
        "path": meta.get("scope_file"),
        "sha256": hashlib.sha256(scope_path.read_bytes()).hexdigest() if scope_path.is_file() else None,
    }
    res = meta["result"]
    joined_n, scope_n, live_n = scope_totals(meta)
    label, headline_n = headline(meta)
    return {
        "receipt": "freeze-before-compare",
        "round": 39,
        "claim": "C1 (depth) — source-blind harness re-derivation",
        "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "head": meta.get("head"),
        "mode": "frozen-inputs" if frozen else "live-capture",
        "driver_argv": list(argv),
        "driver_cwd": str(cwd),
        "inputs": {
            "live": meta["receipt"]["live"],
            "independent": meta["receipt"]["independent"],
        },
        "instrument_files": instruments,
        "scope_file": scope_record,
        "scope_locks": {
            "committed_set": sorted(meta.get("committed_scope") or []),
            "probe_kind": meta.get("scope_probe_kind"),
        },
        "join": {
            "headline_column": label,
            "n": headline_n,
            "joined_scope": scope_n,
            "live_checks": live_n,
            "joined_rows": joined_n,
            "n_scoped_out": len(res["scoped_out"]),
            "scoped_out": res["scoped_out"],
            "n_disagree": len(res["disagree"]),
            "exit": meta["exit"],
            "reason": meta["reason"],
        },
    }




def _raises_compare_error(fn):
    try:
        fn()
    except CompareError:
        return True
    except Exception:
        return False
    return False


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
    # ROUND 40 (T1): this arm used to pin read-first as the contract, which is
    # exactly R1's F-3 (a divergent value hidden in a later channel).  The
    # contract is now cross-channel agreement: the same payload must fail closed,
    # and the ledger's C payload is the end-to-end proof.
    check(
        "independent: a divergent sibling channel fails closed (was: rows preferred)",
        _raises_compare_error(
            lambda: parse_independent({"checks": {"a.b": 99}, "rows": [{"check": "a.b", "value": 1}]})
        ),
    )
    check(
        "independent: agreeing channels still parse",
        parse_independent({"checks": {"a.b": 1}, "rows": [{"check": "a.b", "value": 1}]}) == {"a.b": 1},
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

    # scoped-out rows (round 38): a declared scope-out leaves the join, never
    # counts as agreement, and every malformed declaration fails loudly
    scoped_payload = {"results": [
        {"check": "a.b", "expected": 1, "status": "DERIVED"},
        {"check": "a.c", "expected": None, "status": "SCOPED_OUT"},
    ], "scoped_out": {"a.c": "the carrier's selection rule is the author's own scope"}}
    scoped_vals = parse_independent(scoped_payload, {})
    check("scoped: named row parsed from its own status",
          scoped_vals == {"a.b": 1, "a.c": None})
    scoped_map = parse_scoped_out(scoped_payload, scoped_vals)
    check("scoped: set validated from the payload itself",
          list(scoped_map) == ["a.c"] and "selection rule" in scoped_map["a.c"])
    live_scoped = {"a.b": 1, "a.c": 1}
    modes_scoped = {"a.b": "equal", "a.c": "equal"}
    res_so = compare(live_scoped, scoped_vals, modes_scoped, scoped_out=scoped_map)
    check(
        "scoped: the row leaves the join and is not a disagreement",
        [r["check"] for r in res_so["rows"]] == ["a.b"]
        and not res_so["disagree"] and not res_so["uncovered"] and not res_so["unknown"],
    )
    check(
        "scoped: the scope-out is named with its blocker and narrows the scope",
        res_so["scoped_out_rows"] == ["a.c"] and len(res_so["scoped_out"]) == 1,
    )
    code_so, _ = decide_exit(res_so, 2, 2, 0, 0, {"a.b": "PASS", "a.c": "PASS"})
    check("scoped: a declared scope-out is not a failure", code_so == 0)
    # the numerator cannot gain: dropping the scope-out map turns the same tree red
    res_no = compare(live_scoped, scoped_vals, modes_scoped)
    code_no, reason_no = decide_exit(res_no, 2, 2, 0, 0, {"a.b": "PASS", "a.c": "PASS"})
    check(
        "scoped: without the declaration the same tree disagrees (no free agreement)",
        code_no == 1 and "a.c" in reason_no,
    )
    # the empty-payload row that would otherwise be a silent pass
    res_so2 = compare({"a.b": 1, "a.c": 1, "a.d": 0},
                      {"a.b": 1, "a.c": None, "a.d": 0}, modes_scoped,
                      scoped_out={"a.c": "blocked", "a.d": "blocked"})
    check(
        "scoped: a scoped row's live reading never enters the comparison",
        [r["check"] for r in res_so2["rows"]] == ["a.b"] and res_so2["strict_agree_n"] == 1,
    )
    # malformed declarations: each shape is a loud error, never a quiet pass
    for label, payload, vals, want in (
        ("empty declaration is ambiguous",
         {"results": [{"check": "a.b", "expected": 1}], "scoped_out": {}}, {"a.b": 1},
         "present but empty"),
        ("a named row absent from the payload",
         {"results": [{"check": "a.b", "expected": 1}], "scoped_out": {"a.z": "x"}}, {"a.b": 1},
         "absent from its own payload"),
        ("a row whose status is not SCOPED_OUT",
         {"results": [{"check": "a.b", "expected": 1, "status": "DERIVED"}], "scoped_out": {"a.b": "x"}},
         {"a.b": 1}, "not 'SCOPED_OUT'"),
        ("an empty reason",
         {"results": [{"check": "a.b", "expected": 1, "status": "SCOPED_OUT"}], "scoped_out": {"a.b": "  "}},
         {"a.b": 1}, "reason"),
        ("a non-mapping declaration",
         {"results": [{"check": "a.b", "expected": 1}], "scoped_out": ["a.b"]}, {"a.b": 1},
         "not a mapping"),
    ):
        try:
            parse_scoped_out(payload, vals)
            check(f"scoped: rejected — {label}", False)
        except CompareError as exc:
            check(f"scoped: rejected — {label}", want in str(exc))
    # a scoped id the live side does not carry is exit 2, not a silent exclusion
    res_so3 = compare({"a.b": 1}, {"a.b": 1}, {"a.b": "equal"}, scoped_out={"a.z": "x"})
    code_so3, reason_so3 = decide_exit(res_so3, 1, 1, 0, 0, {"a.b": "PASS"})
    check("scoped: an id absent from the live set is exit 2 named",
          code_so3 == 2 and "a.z" in reason_so3)

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
    # round-38 scope-out arms: the independent stub scopes a.c out, so a tree
    # whose live reading would disagree still exits 0 with a 1/1 joined scope
    stub_live_scoped = (
        "import json;print(json.dumps({'results':["
        "{'check':'a.b','observed':1,'verdict':'PASS','mode':'equal'},"
        "{'check':'a.c','observed':1,'verdict':'PASS','mode':'equal'}]}))"
    )
    stub_ind_scoped = (
        "import json;print(json.dumps({'results':["
        "{'check':'a.b','expected':1,'status':'DERIVED'},"
        "{'check':'a.c','expected':None,'status':'SCOPED_OUT'}],"
        "'scoped_out':{'a.c':'the carrier rule is the author scope'}}))"
    )
    stub_ind_scoped_bad = (
        "import json;print(json.dumps({'results':["
        "{'check':'a.b','expected':1,'status':'DERIVED'},"
        "{'check':'a.c','expected':None,'status':'DERIVED'}],"
        "'scoped_out':{'a.c':'the carrier rule is the author scope'}}))"
    )
    with tempfile.TemporaryDirectory(prefix="cmp-ind-selftest-") as tmp:
        tmp_path = Path(tmp)
        for name, body in (
            ("live.py", stub_live),
            ("ind_ok.py", stub_ind_ok),
            ("ind_bad.py", stub_ind_bad),
            ("live_red.py", stub_live_red),
            ("live_scoped.py", stub_live_scoped),
            ("ind_scoped.py", stub_ind_scoped),
            ("ind_scoped_bad.py", stub_ind_scoped_bad),
        ):
            (tmp_path / name).write_text(body + "\n")
        report = tmp_path / "report.md"

        def e2e(name, live, indi, want_exit=0, want_text="", scope=None):
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
            if scope is not None:
                argv += ["--scope-file", str(scope)]
            proc = subprocess.run(argv, capture_output=True, text=True, timeout=120)
            check(
                f"cli: {name} -> exit {want_exit}",
                proc.returncode == want_exit and (want_text in proc.stdout if want_text else True),
            )
            return proc

        e2e("agreeing stubs", "live.py", "ind_ok.py", want_text="agreement: 2/2")
        e2e("mismatched stub", "live.py", "ind_bad.py", want_exit=1, want_text="a.c")
        e2e("red live instrument", "live_red.py", "ind_ok.py", want_exit=3)
        # a.c is scoped out, so the live 1 vs the independent None never joins:
        # 1/1 joined, exit 0, and the report names the scope-out and its blocker.
        # Round 39: the scope-out now has to be committed in the scope file AND
        # carry a probe the driver recomputes, so the arm builds both.
        carrier = tmp_path / "carrier"
        carrier.mkdir()
        for i, (stamp, entries) in enumerate((("2026-01-01T00:00:00.000Z", 2),
                                              ("2026-02-02T00:00:00.000Z", 5))):
            block = "\\n".join("- entry %d" % n for n in range(entries))
            (carrier / f"s{i}.jsonl").write_text(
                '{"stamp":"%s","text":"<skills>%s\\n</skills>"}\n' % (stamp, block),
                encoding="utf-8")
        empty_carrier = tmp_path / "empty-carrier"
        empty_carrier.mkdir()
        scope_file = tmp_path / "scope.json"
        observable = recompute_probe(
            {"kind": "rule-spread-census", "target": str(carrier)}
        )["observable"]
        scope_file.write_text(json.dumps({
            "schema": "kotoba-harness-independent-scope-v1",
            "probe_contract": {"kind": "rule-spread-census"},
            "scope_out": {"a.c": {"kind": "rule-in-author-scope",
                                  "reason": "the carrier rule is the author's scope"}},
        }), encoding="utf-8")

        def stub_scoped(ind_path, observable_json, status="SCOPED_OUT", with_probe=True,
                        target=None, kind="rule-spread-census"):
            probe = ("{'kind':%r,'target':%r,'observable':%s}"
                     % (kind, target if target is not None else str(carrier),
                        observable_json)) if with_probe else "None"
            record = "{'check':'a.c','expected':None,'status':" + repr(status)
            if with_probe:
                record += ",'probe':" + probe
            record += "}"
            body = ("import json;print(json.dumps({'results':["
                    "{'check':'a.b','expected':1,'status':'DERIVED'},"
                    + record + "],"
                    "'scoped_out':{'a.c':'the carrier rule is the author scope'},"
                    "'scoped_out_probes':{'a.c':" + probe + "}}))")
            ind_path.write_text(body + "\n", encoding="utf-8")

        stub_scoped(tmp_path / "ind_scoped.py", json.dumps(observable))
        probe_for_c = lambda: ("{'kind':'rule-spread-census','target':%r,'observable':%s}"
                               % (str(carrier), json.dumps(observable)))
        proc = e2e("scope-out stub narrows the scope", "live_scoped.py", "ind_scoped.py",
                   want_text="agreement: 1/1", scope=scope_file)
        check("cli: scope-out stub reports the scoped row count",
              "1 scoped out" in proc.stdout)
        # round-39 counter-probes: each shape of the r38 laundering hole must
        # fail closed, and the decisive one is a row the committed file does not list
        stub_scoped(tmp_path / "ind_launder.py", json.dumps(observable))
        uncommitted = tmp_path / "scope-empty.json"
        uncommitted.write_text(json.dumps({"scope_out": {}}), encoding="utf-8")
        proc = e2e("laundering: an uncommitted scope-out fails closed", "live_scoped.py",
                   "ind_launder.py", want_exit=2, scope=uncommitted)
        check("cli: laundering is named as the class",
              "laundering" in proc.stderr and "a.c" in proc.stderr)
        # a committed row whose declared census does not recompute
        stub_scoped(tmp_path / "ind_fake.py", json.dumps(dict(observable, distinct_totals=[7])))
        proc = e2e("false blocker: a declared census that does not recompute", "live_scoped.py",
                   "ind_fake.py", want_exit=2, scope=scope_file)
        check("cli: false blocker is named as the class", "false blocker" in proc.stderr)
        # a probe with no probe block at all
        stub_scoped(tmp_path / "ind_noprobe.py", "{}", with_probe=False)
        proc = e2e("false blocker: a scoped row with no probe", "live_scoped.py",
                   "ind_noprobe.py", want_exit=2, scope=scope_file)
        check("cli: a probe-less scope-out is named", "no probe block" in proc.stderr)
        # a probe pointed at a tree that cannot corroborate anything
        stub_scoped(tmp_path / "ind_redirect.py", json.dumps(observable),
                    target=str(empty_carrier))
        proc = e2e("false blocker: a redirected probe", "live_scoped.py",
                   "ind_redirect.py", want_exit=2, scope=scope_file)
        check("cli: a redirected probe is named", "no candidate block" in proc.stderr)
        # a record marked SCOPED_OUT that the map omits: the two channels must agree.
        # The map must be non-empty and well-formed for this arm to reach the
        # channel check, so it declares a.c and the split is on a.d.
        (tmp_path / "ind_split.py").write_text(
            "import json;print(json.dumps({'results':["
            "{'check':'a.b','expected':1,'status':'DERIVED'},"
            "{'check':'a.c','expected':None,'status':'SCOPED_OUT'},"
            "{'check':'a.d','expected':None,'status':'SCOPED_OUT'}],"
            "'scoped_out':{'a.c':'the carrier rule is the author scope'},"
            "'scoped_out_probes':{'a.c':" + probe_for_c() + "}}))\n", encoding="utf-8")
        proc = e2e("channel split: status and map disagree", "live_scoped.py",
                   "ind_split.py", want_exit=2, scope=scope_file)
        check("cli: a split channel is named", "channel split" in proc.stderr)
        # an unknown probe kind cannot slip through as un-verified
        stub_scoped(tmp_path / "ind_kind.py", json.dumps(observable), kind="assertion")
        proc = e2e("false blocker: an unknown probe kind", "live_scoped.py",
                   "ind_kind.py", want_exit=2, scope=scope_file)
        check("cli: an unknown probe kind is named", "probe kind" in proc.stderr)
        e2e("scope-out with a mismatched status fails closed", "live_scoped.py",
            "ind_scoped_bad.py", want_exit=2, scope=scope_file)
        proc = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--live-cmd",
                f"{sys.executable} {tmp_path / 'live_scoped.py'}",
                "--independent-cmd",
                f"{sys.executable} {tmp_path / 'ind_scoped_bad.py'}",
                "--expect-n",
                "2",
                "--no-stamp",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        check("cli: scope-out status mismatch names the class and the row",
              proc.returncode == 2 and "SCOPED_OUT" in proc.stderr and "a.c" in proc.stderr)
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

        # round-38 receipt arms (seat P2, A1-D1): the freeze receipt is a
        # first-class output, and its mode field must distinguish a fully frozen
        # comparison from one side's own stdout capture
        receipt_path = tmp_path / "receipt.json"
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
                "--receipt",
                str(receipt_path),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        receipt = json.loads(receipt_path.read_text()) if receipt_path.exists() else {}
        check("receipt: written with the freeze-before-compare label",
              receipt.get("receipt") == "freeze-before-compare")
        check("receipt: live-capture mode when both sides run",
              receipt.get("mode") == "live-capture")
        check(
            "receipt: both sides' input digests recorded before the join",
            all(isinstance(receipt.get("inputs", {}).get(side, {}).get("sha256"), str)
                and len(receipt["inputs"][side]["sha256"]) == 64
                for side in ("live", "independent")),
        )
        check("receipt: invocation record carries the driver argv and verdict",
              isinstance(receipt.get("driver_argv"), list)
              and receipt.get("join", {}).get("exit") == 0)
        # round 39: the committed scope file is a lock on the headline, so the
        # receipt must show which scope bytes the join ran under.  The path is
        # recorded repo-relative (as given on the command line); the digest is
        # the load-bearing part.
        check("receipt: the committed scope file's digest is recorded",
              receipt.get("scope_file", {}).get("path") == DEFAULT_SCOPE
              and isinstance(receipt.get("scope_file", {}).get("sha256"), str)
              and len(receipt["scope_file"]["sha256"]) == 64)
        check("receipt: the receipt records the committed scope set and probe kind",
              isinstance(receipt.get("scope_locks", {}).get("committed_set"), list)
              and len(receipt["scope_locks"]["committed_set"]) == 4)
        live_bytes = (tmp_path / "live.json")
        ind_bytes = (tmp_path / "ind.json")
        subprocess.run(
            [sys.executable, str(tmp_path / "live.py")], capture_output=True, text=True,
            timeout=60,
        )
        live_bytes.write_text(
            subprocess.run([sys.executable, str(tmp_path / "live.py")],
                           capture_output=True, text=True, timeout=60).stdout)
        ind_bytes.write_text(
            subprocess.run([sys.executable, str(tmp_path / "ind_ok.py")],
                           capture_output=True, text=True, timeout=60).stdout)
        receipt_frozen = tmp_path / "receipt-frozen.json"
        subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--live-json",
                str(live_bytes),
                "--independent-json",
                str(ind_bytes),
                "--expect-n",
                "2",
                "--no-stamp",
                "--receipt",
                str(receipt_frozen),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        frozen = json.loads(receipt_frozen.read_text()) if receipt_frozen.exists() else {}
        check("receipt: frozen-inputs mode when both sides consume files",
              frozen.get("mode") == "frozen-inputs")
        check(
            "receipt: a frozen side records its own file digest",
            all(frozen.get("inputs", {}).get(side, {}).get("file_sha256") ==
                frozen.get("inputs", {}).get(side, {}).get("sha256")
                for side in ("live", "independent")),
        )
        proc = subprocess.run(
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
                "--receipt",
                str(tmp_path / "no-such-dir" / "receipt.json"),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        check("receipt: unwritable path is a named exit 2, never a traceback",
              proc.returncode == 2 and "receipt path unwritable" in proc.stderr)

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
        live_receipt = side_receipt(text, live_cmd, live_exit, args.live_json, cwd)
    else:
        live_cmd = args.live_cmd
        live_exit, text, live_err = run_cmd(shlex.split(live_cmd), cwd)
        if live_exit != 0 and not text.strip():
            raise CompareError(f"live instrument failed with no stdout: exit {live_exit}: {live_err.strip()[:300]}")
        live_receipt = side_receipt(text, live_cmd, live_exit, None, cwd)
    live_payload = load_payload(text, "live")
    live, verdicts, modes = parse_live(live_payload)

    if args.independent_json:
        text = Path(args.independent_json).read_text()
        ind_cmd, ind_exit = f"file:{args.independent_json}", 0
        ind_receipt = side_receipt(text, ind_cmd, ind_exit, args.independent_json, cwd)
    elif args.independent_cmd:
        ind_cmd = args.independent_cmd
        ind_exit, text, ind_err = run_cmd(shlex.split(ind_cmd), cwd)
        if ind_exit != 0 and not text.strip():
            raise CompareError(
                f"independent instrument failed with no stdout: exit {ind_exit}: {ind_err.strip()[:300]}"
            )
        ind_receipt = side_receipt(text, ind_cmd, ind_exit, None, cwd)
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
        ind_receipt = side_receipt(text, ind_cmd, ind_exit, None, cwd)
    statuses = {}
    ind_payload = load_payload(text, "independent")
    independent = parse_independent(ind_payload, statuses)
    scoped_out = parse_scoped_out(ind_payload, independent)
    # Round 39 (C1, seat P1) — the three locks on the scope-out, in order:
    # the set is committed (not self-served), each row's blind probe is
    # recomputed here, and the blocker's falsifier is swept for.
    committed, contract = load_scope_file(args.scope_file)
    probes = {}
    if isinstance(ind_payload, dict):
        raw_probes = ind_payload.get("scoped_out_probes")
        if isinstance(raw_probes, dict):
            probes = {k: v for k, v in raw_probes.items() if isinstance(v, dict)}
        if not probes:
            # the per-record channel the instrument also publishes
            for record in _record_list(ind_payload) or []:
                if isinstance(record, dict) and isinstance(record.get("probe"), dict):
                    probes[_record_id(record, "independent")] = record["probe"]
    check_scope_probes(scoped_out, probes, committed, contract, statuses)
    scoped_out = {cid: scoped_out[cid] for cid in sorted(scoped_out)}
    scope_probe_kind = None
    for probe in probes.values():
        if isinstance(probe, dict) and probe.get("kind"):
            scope_probe_kind = probe["kind"]
            break

    res = annotate_statuses(
        compare(live, independent, modes, use_predicates=not args.no_mode_predicates,
                scoped_out=scoped_out), statuses
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
        "live_json_used": bool(args.live_json),
        "ind_json_used": bool(args.independent_json),
        "scope_file": args.scope_file,
        "committed_scope": sorted(committed),
        "scope_probe_kind": scope_probe_kind,
        "receipt": {"live": live_receipt, "independent": ind_receipt},
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
    parser.add_argument(
        "--receipt",
        default=None,
        help="write the freeze-before-compare receipt (both sides' input sha256 + invocation record) to this path",
    )
    parser.add_argument("--stamp", default="", help="free-text provenance line for the markdown report")
    parser.add_argument("--no-stamp", action="store_true", help="omit the stamp line")
    parser.add_argument(
        "--strict-headline", action="store_true", help="make strict value equality decisive (red-team mode)"
    )
    parser.add_argument(
        "--scope-file",
        default=DEFAULT_SCOPE,
        help="committed scope-out set the payload's own declaration is checked against "
             "(round 39: a scope-out must be committed, never self-declared)",
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

    if args.receipt:
        try:
            receipt = render_receipt(meta, argv if argv is not None else sys.argv[1:], Path(args.cwd).resolve())
            Path(args.receipt).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        except OSError as exc:
            print(f"compare_harness_independent: ERROR: receipt path unwritable: {args.receipt}: {exc}", file=sys.stderr)
            return 2
        print(f"receipt: {args.receipt}", file=sys.stderr if args.json else sys.stdout)

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