#!/usr/bin/env python3
"""check_substrate_pins.py — enforce verifiers/baseline.json `measured_against`.

Read-only guard for the round-21/22 named debt: the `measured_against` block
records the substrate binaries' sha256 (omp + opencode) and the omp binary mtime,
but no gate read them, so the 2026-10-16 omp rebuild (ff59fc1b -> bf1e86a9)
passed every gate unnoticed.

Exit ladder (family contract; precedence 3 > 2 > 1 > 0, identical in --json
mode, which carries the code in `exit_code`):

  0  every expected pin is present and holds
  1  a pin drifted, an expected pin is absent from the block, or the block
     declares no pins at all (VACUOUS: measured_against absent / null /
     non-mapping)
  2  a pinned binary cannot be read or stat'd (UNREADABLE), or a discovered pin
     names a substrate with no registered binary path (UNSUPPORTED), or a
     pin-shaped key differs only in case from a contract pin, or carries
     whitespace/control/format characters, or both (UNSUPPORTED: pin keys
     are exact bytes)
  3  the baseline document cannot be read or parsed (NO_BASELINE: missing file,
     directory, EACCES, bad JSON, JSON that is not an object), or a pin value
     cannot be interpreted as its kind (BAD_PIN)

The 1/3 boundary is deliberate: 3 means the baseline cannot be read as a pin
document (IO / JSON / value-level type or syntax); 1 means the document was read
and declares a pin set that does not satisfy the guard — a deleted pin is as
loud as a moved substrate (round-21 lesson: an unenforced pin is the defect).
The block-level cases (absent / null / non-mapping) sit on 1 per the round-23
claim, which maps the M6-D2 vacuity class to the drift tier; P1's spec had them
at 3 and P6's D1 fix suggested 2 — the claim decides, and both predecessors'
concern (never a silent pass, never a traceback) is preserved.

Read-only: the guard opens the baseline and the binaries for reading only; it
never executes a pinned binary (an exec writes to ~/.local/share/opencode/log,
the observation surface of verify_harness_claims.py) and never re-pins.
Deterministic: no wall clock, host, pid or duration appears in either mode.
Stdlib only (Python >= 3.11).

Host-anchored: the default binary paths are this host's installs (same values
as verify_harness_claims.py OMP_BIN/OC_BIN and verify_surfaces.py
DEFAULT_BINARIES; round 47 moved opencode to the npm `opencode-ai` bytes the
`~/.local/bin/opencode` npx wrapper executes — the wrapper itself is never the
pinned file, its sha says nothing about the ELF that runs), so a clone's green is a statement about that
installation, not about the clone; --omp-binary/--opencode-binary override both
for fixture runs.
"""

from __future__ import annotations

import argparse
import calendar
import contextlib
import hashlib
import io
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parent.parent
# Round 72: omp is the ELF `omp.real` (the `omp` file installed 2026-10-23 is a
# crash-restart shell wrapper; its sha says nothing about the ELF that runs) and
# opencode is v2.1.4 at `~/.opencode/bin/opencode` (the npx 1.19.4 path is gone).
BINARIES = {
    "omp": "/home/vgpnk/.local/bin/omp.real",
    "opencode": "/home/vgpnk/.opencode/bin/opencode",
}
# The pin set the guard's contract requires. Discovery additionally checks any
# other measured_against key shaped like `<substrate>_binary_<kind>`: a pin the
# guard cannot resolve is UNSUPPORTED (exit 2), never a silent skip — the
# round-21 vacuity lesson applied to coverage. The shape matches
# case-insensitively, but pin names are exact-case: a key differing only in
# case from a contract pin (e.g. OMP_binary_sha256) is discovered and reported
# UNSUPPORTED, not skipped.
EXPECTED_PINS = (
    ("omp_binary_sha256", "omp", "sha256"),
    ("omp_binary_mtime", "omp", "mtime"),
    ("opencode_binary_sha256", "opencode", "sha256"),
)
DISCOVER_RE = re.compile(r"^(?P<prefix>[a-z0-9_]+)_binary_(?P<kind>[A-Za-z0-9]+)$",
                         re.IGNORECASE)

# Pin keys are exact bytes (round-32 claim W). A key that is not byte-identical
# to its own canonical form is a hygiene violation and must FAIL, never skip.
# The predicate is a Unicode-CATEGORY test, not str.strip(): str.strip() removes
# whitespace (Zs/Zl/Zp and the ASCII controls) but leaves the FORMAT characters
# (Cf) that render invisibly -- U+200B ZERO WIDTH SPACE, U+FEFF BOM/ZWNBSP,
# U+00AD SOFT HYPHEN, the bidi marks. Scout M4 (round 31) found the padded-key
# silent skip; a strip()-based fix still admits Cf-padded keys, so this guard
# classifies by category (round-32 scout W3, the one named design difference
# from the strip()-normalizing draft).
HYGIENE_CATEGORIES = ("Zs", "Zl", "Zp", "Cc", "Cf")


def hygiene_offenders(key: str) -> list[str]:
    """Every character that makes `key` non-canonical, in key order."""
    return [c for c in key if unicodedata.category(c) in HYGIENE_CATEGORIES]


def canonical_pin_key(key: str) -> str:
    """`key` with every hygiene offender removed: the exact-bytes identity a
    pin key must already have. Legitimate keys are their own canonical form."""
    return "".join(c for c in key
                   if unicodedata.category(c) not in HYGIENE_CATEGORIES)


def hygiene_detail(key: str) -> str:
    return "pin key is not exact bytes: %s; pin keys are exact bytes" % ", ".join(
        "U+%04X %s" % (ord(c), unicodedata.category(c))
        for c in hygiene_offenders(key))
KINDS = ("sha256", "mtime")
SHA_RE = re.compile(r"^[0-9a-fA-F]{64}$")
FRAC_RE = re.compile(r"\.(\d+)")

# Verdict -> exit code. Anything not listed is a bug, not a pass.
VERDICT_CODE = {
    "PASS": 0,
    "DRIFT": 1,
    "PIN_ABSENT": 1,
    "VACUOUS": 1,
    "UNREADABLE": 2,
    "UNSUPPORTED": 2,
    "NO_BASELINE": 3,
    "BAD_PIN": 3,
}


def code_of(results: list[dict]) -> int:
    """Highest-precedence verdict code; 0 only when every verdict is PASS."""
    return max((VERDICT_CODE[r["verdict"]] for r in results), default=1)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_iso_ns(text: str) -> tuple[int, int]:
    """ISO-8601 stamp -> (epoch_ns, tolerance_ns) at the pin's own precision.

    Exact for a 9-digit pin — no float and no microsecond truncation, because
    `datetime.fromisoformat(...).timestamp()` is 874 ns low on the live omp pin
    and would fabricate a DRIFT on a faithful record. A pin with d fractional
    digits states its instant only to 10**(9-d) ns, so its acceptance window is
    that quantum (a 6-digit pin accepts the same microsecond); the window is
    reported, so a coarse pin is visible rather than silently weak.
    """
    if not isinstance(text, str):
        raise ValueError("pin is not a string")
    m = FRAC_RE.search(text)
    digits = m.group(1) if m else ""
    if len(digits) > 9:
        raise ValueError("more than 9 fractional digits")
    frac_ns = int(digits.ljust(9, "0")) if digits else 0
    tolerance_ns = 10 ** (9 - len(digits)) - 1 if digits else 10**9 - 1
    base = FRAC_RE.sub("", text, count=1)
    dt = datetime.fromisoformat(base)
    if dt.tzinfo is None:
        raise ValueError("pin has no UTC offset")
    secs = calendar.timegm(dt.utctimetuple())
    return secs * 1_000_000_000 + frac_ns, tolerance_ns


def check_pins(baseline: object, binaries: dict[str, Path]) -> list[dict]:
    """Returns the (possibly single synthetic) verdict records."""
    if not isinstance(baseline, dict):
        return [{"pin": "-", "verdict": "NO_BASELINE",
                 "detail": "baseline is not a JSON object"}]
    ma = baseline.get("measured_against")
    if not isinstance(ma, dict):
        return [{"pin": "-", "verdict": "VACUOUS",
                 "detail": "measured_against is %s, declares no pins"
                           % ("absent" if ma is None else type(ma).__name__)}]

    keys: list[str] = [p[0] for p in EXPECTED_PINS]
    for key in sorted(ma):
        if key in keys:
            continue
        # A pin-shaped key is discovered by its CANONICAL form, so a key that
        # only differs from pin shape by hygiene characters still enters the
        # report (and then fails there) instead of vanishing from it.
        if (DISCOVER_RE.match(key) or DISCOVER_RE.match(canonical_pin_key(key))
                or hygiene_offenders(key)):
            keys.append(key)

    results: list[dict] = []
    known = {p[0]: (p[1], p[2]) for p in EXPECTED_PINS}
    for key in keys:
        m = DISCOVER_RE.match(canonical_pin_key(key))
        prefix, kind = known.get(key, (m.group("prefix"), m.group("kind"))
                                 if m else ("-", "-"))
        entry: dict = {"pin": key, "kind": kind, "substrate": prefix}
        if key not in ma:
            entry.update(verdict="PIN_ABSENT", expect=None, observed=None,
                         detail="pin declared by the guard's contract, absent "
                                "from measured_against")
            results.append(entry)
            continue
        if hygiene_offenders(key):
            entry.update(verdict="UNSUPPORTED", observed=None,
                         detail=hygiene_detail(key))
            results.append(entry)
            continue
        key_canon = canonical_pin_key(key)
        canonical = next((p[0] for p in EXPECTED_PINS
                          if p[0] != key and p[0].casefold() == key_canon.casefold()),
                         None)
        if canonical is not None:
            entry.update(verdict="UNSUPPORTED", observed=None,
                         detail="mis-cased pin key: matches %s except for case; "
                                "pin keys are exact-case" % canonical)
            results.append(entry)
            continue
        expect = ma[key]
        entry["expect"] = expect
        if prefix not in BINARIES or kind not in KINDS:
            entry.update(verdict="UNSUPPORTED", observed=None,
                         detail="pinned substrate/kind not resolvable by this "
                                "guard (%s)" % key)
            results.append(entry)
            continue
        binary = binaries[prefix]
        entry["binary"] = str(binary)
        if kind == "sha256":
            if not (isinstance(expect, str) and SHA_RE.match(expect)):
                entry.update(verdict="BAD_PIN", observed=None,
                             detail="sha256 pin is not 64 hex characters")
                results.append(entry)
                continue
            try:
                live = sha256_of(binary)
            except OSError as exc:
                entry.update(verdict="UNREADABLE", observed=None, detail=str(exc))
                results.append(entry)
                continue
            entry["observed"] = live
            entry["verdict"] = "PASS" if live == expect.lower() else "DRIFT"
        else:
            try:
                expect_ns, tolerance_ns = parse_iso_ns(expect)
            except ValueError as exc:
                entry.update(verdict="BAD_PIN", observed=None, detail=str(exc))
                results.append(entry)
                continue
            try:
                live_ns = binary.stat().st_mtime_ns
            except OSError as exc:
                entry.update(verdict="UNREADABLE", observed=None, detail=str(exc))
                results.append(entry)
                continue
            delta = live_ns - expect_ns
            entry.update(observed=str(live_ns), delta_ns=delta,
                         tolerance_ns=tolerance_ns,
                         verdict="PASS" if abs(delta) <= tolerance_ns else "DRIFT")
        results.append(entry)
    return results


def emit(results: list[dict], code: int, json_mode: bool, error: str | None = None) -> None:
    if json_mode:
        payload = {
            "checks": results,
            "pass": sum(1 for r in results if r["verdict"] == "PASS"),
            "fail": sum(1 for r in results if r["verdict"] != "PASS"),
            "exit_code": code,
        }
        if error is not None:
            payload["error"] = error
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    if not results:
        return  # a baseline that could not be read has nothing to summarise
    for r in results:
        if r["verdict"] == "PASS":
            extra = ("delta %d ns (tolerance %d ns)" % (r["delta_ns"], r["tolerance_ns"])
                     if "delta_ns" in r else r["observed"])
            print("PASS %s: %s" % (r["pin"], extra))
        elif r["verdict"] == "DRIFT" and "delta_ns" in r:
            print("FAIL %s: mtime drift (sha256 not compared): pinned_ns=%s "
                  "observed_ns=%s delta_ns=%d tolerance_ns=%d"
                  % (r["pin"], r["expect"], r["observed"], r["delta_ns"],
                     r["tolerance_ns"]))
        elif r["verdict"] == "DRIFT":
            print("FAIL %s: sha256 drift: expect=%s got=%s"
                  % (r["pin"], r["expect"], r["observed"]))
        else:
            print("FAIL %s: %s: %s" % (r["pin"], r["verdict"], r["detail"]))
    failed = [r["pin"] for r in results if r["verdict"] != "PASS"]
    if failed:
        label = next((r["verdict"] for r in results if r["verdict"] == "DRIFT"),
                     max((r for r in results if r["verdict"] != "PASS"),
                         key=lambda r: VERDICT_CODE[r["verdict"]])["verdict"])
        print("%s %d/%d pins failed: %s" % (label, len(failed), len(results),
                                            ", ".join(failed)))
    else:
        print("OK %d/%d pins hold" % (len(results), len(results)))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=str(DEFAULT_REPO),
                    help="repo root for default paths (default: script's grandparent)")
    ap.add_argument("--baseline", metavar="PATH",
                    help="baseline JSON (default: <repo>/verifiers/baseline.json)")
    ap.add_argument("--omp-binary", metavar="PATH", default=BINARIES["omp"])
    ap.add_argument("--opencode-binary", metavar="PATH", default=BINARIES["opencode"])
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--self-test", action="store_true",
                    help="assert checks and exit codes on temporary fixtures only")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    baseline_path = Path(args.baseline) if args.baseline else (
        Path(args.repo) / "verifiers" / "baseline.json")
    binaries = {"omp": Path(args.omp_binary), "opencode": Path(args.opencode_binary)}

    try:
        baseline = json.loads(baseline_path.read_text())
    except (OSError, ValueError) as exc:
        error = "NO_BASELINE %s: %s" % (baseline_path, exc)
        if not args.json:
            print("ERROR %s" % error, file=sys.stderr)
        emit([], 3, args.json, error)
        return 3

    results = check_pins(baseline, binaries)
    code = code_of(results)
    if code >= 2 and not args.json:
        for r in results:
            if VERDICT_CODE[r["verdict"]] == code:
                print("ERROR %s %s: %s" % (r["verdict"], r["pin"], r["detail"]),
                      file=sys.stderr)
    emit(results, code, args.json)
    return code


def run_capture(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


def self_test() -> int:
    import tempfile

    failures: list[str] = []
    total = 0

    def rec(what: str, ok: bool, got: object) -> None:
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    with tempfile.TemporaryDirectory(prefix="pins-selftest-") as tmp:
        tmp = Path(tmp)
        mini = tmp / "mini.bin"
        mini.write_bytes(b"#!kotoba-pin-fixture-mini-v1\n" + bytes(range(64)))
        sha = sha256_of(mini)
        ns = mini.stat().st_mtime_ns
        seq = 0

        def iso_of(value_ns: int, digits: int) -> str:
            secs, sub = divmod(value_ns, 10**9)
            stamp = datetime.fromtimestamp(secs, tz=timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S")
            return "%s.%s+00:00" % (stamp, str(sub).rjust(9, "0")[:digits])

        iso9 = iso_of(ns, 9)
        iso6 = iso_of(ns, 6)

        def write(name: str, payload: object) -> str:
            path = tmp / name
            path.write_text(payload if isinstance(payload, str)
                            else json.dumps(payload))
            return str(path)

        def world(**pins: object) -> str:
            nonlocal seq
            seq += 1
            base = {"measured_against": {
                "omp_binary_sha256": sha, "omp_binary_mtime": iso9,
                "opencode_binary_sha256": sha, **pins}}
            return write("baseline-%02d.json" % seq, base)

        def run(base: str, *extra: str) -> tuple[int, str, str]:
            return run_capture(["--baseline", base, "--omp-binary", str(mini),
                                "--opencode-binary", str(mini), *extra])

        # -- ladder slot 0: every expected pin present and holding ------------
        code, out, err = run(world())
        rec("match: exit 0", code == 0, code)
        rec("match: stdout names all three pins as PASS",
            all(p in out for p in ("omp_binary_sha256", "omp_binary_mtime",
                                   "opencode_binary_sha256")) and "FAIL" not in out, out)
        rec("match: OK summary", "OK 3/3 pins hold" in out, out)
        rec("match: clean stderr", err == "", err)
        rec("match: no Traceback", "Traceback" not in out + err, out + err)

        # -- ladder slot 1: drift, absent pin, vacuity ------------------------
        code, out, _ = run(world(omp_binary_sha256="0" * 64))
        rec("sha drift: exit 1", code == 1, code)
        rec("sha drift: names the pin", "FAIL omp_binary_sha256:" in out, out)
        code, out, _ = run(world(omp_binary_mtime="2000-01-01T00:00:00.000000000+00:00"))
        rec("mtime drift: exit 1", code == 1, code)
        rec("mtime drift: names the pin", "FAIL omp_binary_mtime:" in out, out)
        code, out, _ = run(world(omp_binary_mtime=iso6))
        rec("mtime truncated to us (same microsecond): exit 0", code == 0, code)
        code, out, _ = run(world(omp_binary_sha256=sha.upper()))
        rec("sha case-insensitive: exit 0", code == 0, code)
        base = world(omp_binary_mtime=iso9)
        os_ns = ns + 1
        os_utime(mini, os_ns)
        code, out, _ = run(base)
        rec("mtime drift of 1 ns: exit 1 (ns-exact on a 9-digit pin)", code == 1, code)
        os_utime(mini, ns)
        code, out, _ = run(write("vacuous-null.json", {"measured_against": None}))
        rec("measured_against null: exit 1", code == 1, code)
        rec("measured_against null: VACUOUS named",
            "FAIL -: VACUOUS" in out and "VACUOUS 1/1 pins failed" in out
            and "Traceback" not in out, out)
        code, out, _ = run(write("vacuous-int.json", {"measured_against": 5}))
        rec("measured_against int: exit 1, no traceback",
            code == 1 and "Traceback" not in out, (code, out))
        code, out, _ = run(write("vacuous-empty.json", {"measured_against": {}}))
        rec("measured_against empty: exit 1", code == 1, code)
        rec("measured_against empty: all three pins PIN_ABSENT",
            sum(1 for line in out.splitlines()
                if line.startswith("FAIL ") and ": PIN_ABSENT:" in line) == 3, out)
        code, out, _ = run(write("one-pin-missing.json", {"measured_against": {
            "omp_binary_sha256": sha, "opencode_binary_sha256": sha}}))
        rec("deleted single pin: exit 1 (P7 C9 silent-shrink closed)", code == 1, code)
        rec("deleted single pin: PIN_ABSENT names it",
            "FAIL omp_binary_mtime: PIN_ABSENT" in out, out)
        code, out, _ = run(world(cursor_binary_sha256="0" * 64))
        rec("stray pin from an unregistered substrate: exit 2 (never silent)",
            code == 2, code)
        rec("stray pin: UNSUPPORTED named",
            "FAIL cursor_binary_sha256: UNSUPPORTED" in out, out)
        code, out, _ = run(world(OMP_binary_sha256="0" * 64))
        rec("mis-cased key OMP_binary_sha256: exit 2 (exact-case, never skipped)",
            code == 2, code)
        rec("mis-cased key: UNSUPPORTED names key and canonical pin",
            "FAIL OMP_binary_sha256: UNSUPPORTED: mis-cased pin key: matches "
            "omp_binary_sha256 except for case" in out, out)
        rec("mis-cased key: summary 1/4 names it, the three real pins still PASS",
            "UNSUPPORTED 1/4 pins failed: OMP_binary_sha256" in out
            and sum(1 for ln in out.splitlines() if ln.startswith("PASS ")) == 3,
            out)
        code, _, _ = run(world(omp_Binary_sha256="0" * 64))
        rec("mis-cased separator omp_Binary_sha256: exit 2", code == 2, code)
        code, _, _ = run(world(omp_binary_SHA256=sha))
        rec("mis-cased kind omp_binary_SHA256: exit 2", code == 2, code)
        code, out, _ = run(world(**{" omp_binary_sha256": sha}))
        rec("whitespace-padded key: exit 2 (exact bytes, never skipped)",
            code == 2, code)
        rec("whitespace-padded key: UNSUPPORTED names the key and the char",
            "FAIL  omp_binary_sha256: UNSUPPORTED: pin key is not exact bytes: "
            "U+0020 Zs" in out, out)
        rec("whitespace-padded key: summary 1/4, the three real pins still PASS",
            "UNSUPPORTED 1/4 pins failed:  omp_binary_sha256" in out
            and sum(1 for ln in out.splitlines() if ln.startswith("PASS ")) == 3,
            out)
        for label, key in (("trailing space", "omp_binary_sha256 "),
                           ("leading tab", "\tomp_binary_sha256"),
                           ("NBSP", "\u00a0omp_binary_sha256"),
                           ("ZWSP (Cf)", "\u200bomp_binary_sha256"),
                           ("BOM (Cf)", "\ufeffomp_binary_sha256")):
            code, out, _ = run(world(**{key: sha}))
            rec("%s key: exit 2 (category test, not str.strip)" % label,
                code == 2, (code, out))
        code, out, _ = run(world(**{"   ": sha}))
        rec("all-whitespace key (not pin-shaped): exit 2, never a silent 0",
            code == 2 and "UNSUPPORTED" in out, (code, out))
        code, out, _ = run(world(**{" cursor_binary_sha256": "0" * 64}))
        rec("padded STRAY substrate key: exit 2, not a silent 0",
            code == 2 and "UNSUPPORTED" in out, (code, out))
        code, out, _ = run(world(**{"\u200bcursor_binary_sha256": "0" * 64}))
        rec("Cf-padded stray substrate key: exit 2", code == 2, code)
        code, out, _ = run(world(opencode_binary_mtime=iso9))
        rec("extra pin on a registered substrate is compared: exit 0 when it holds",
            code == 0, code)
        code, out, _ = run(world(omp_binary_mtime=iso_of(ns + 2000, 6)))
        rec("mtime pin 2 us off at us precision: exit 1 — the window is the pin's "
            "own quantum, not a blob tolerance", code == 1, code)
        code, out, _ = run(world(omp_binary_mtime=iso6))
        rec("coarse pin: its acceptance window is reported, not silent",
            code == 0 and "tolerance 999 ns" in out, (code, out))

        # -- ladder slot 2: environment unreadable ----------------------------
        code, out, err = run(world(), "--omp-binary", str(tmp / "nope"))
        rec("missing binary: exit 2", code == 2, code)
        rec("missing binary: UNREADABLE names the pin",
            "FAIL omp_binary_sha256: UNREADABLE" in out, out)
        code, _, _ = run(world(), "--opencode-binary", str(tmp))
        rec("binary is a directory: exit 2", code == 2, code)
        dangling = tmp / "dangling"
        if not dangling.is_symlink():
            dangling.symlink_to(tmp / "gone")
        code, _, _ = run(world(), "--omp-binary", str(dangling))
        rec("dangling symlink: exit 2", code == 2, code)
        denied = tmp / "denied.bin"
        denied.write_bytes(b"x")
        denied.chmod(0o000)
        code, _, _ = run(world(), "--omp-binary", str(denied))
        rec("unreadable binary (mode 000): exit 2", code == 2, code)
        denied.chmod(0o644)

        # -- ladder slot 3: the baseline itself -------------------------------
        code, out, err = run(str(tmp / "does-not-exist.json"))
        rec("missing baseline: exit 3", code == 3, code)
        rec("missing baseline: no OK line on stdout (exit 3 is never a pass)",
            out.strip() == "" and "ERROR" in err, (out, err))
        code, _, err = run(str(tmp))
        rec("baseline is a directory: exit 3", code == 3, code)
        code, _, err = run(write("bad.json", "{oops"))
        rec("unparseable baseline: exit 3", code == 3, code)
        code, out, _ = run(write("array.json", [1, 2]))
        rec("baseline is a JSON array: exit 3, no traceback",
            code == 3 and "Traceback" not in out, (code, out))
        code, out, _ = run(world(omp_binary_sha256=12345))
        rec("sha pin of the wrong type: exit 3 BAD_PIN, no traceback",
            code == 3 and "BAD_PIN" in out and "Traceback" not in out, (code, out))
        code, out, _ = run(world(omp_binary_sha256="deadbeef"))
        rec("short sha pin: exit 3 BAD_PIN", code == 3, code)
        code, out, _ = run(world(omp_binary_mtime="garbage"))
        rec("unparseable mtime pin: exit 3 BAD_PIN", code == 3, code)
        code, out, _ = run(world(omp_binary_mtime=12345))
        rec("mtime pin of the wrong type: exit 3 BAD_PIN, no traceback",
            code == 3 and "Traceback" not in out, (code, out))
        code, out, _ = run(world(omp_binary_mtime="2026-01-01T00:00:00"))
        rec("mtime pin without a UTC offset: exit 3 BAD_PIN", code == 3, code)

        # -- precedence and the json/text agreement ---------------------------
        base = write("both-broken.json", {"measured_against": {
            "omp_binary_sha256": 12345, "opencode_binary_sha256": sha}})
        code, _, _ = run(base, "--opencode-binary", str(tmp / "nope"))
        rec("BAD_PIN outranks UNREADABLE: exit 3", code == 3, code)
        base = world(omp_binary_sha256="0" * 64)
        code, _, _ = run(base, "--opencode-binary", str(tmp / "nope"))
        rec("UNREADABLE outranks DRIFT: exit 2", code == 2, code)
        for name, make, extra, expect in (
            ("json match", world, (), 0),
            ("json sha drift", lambda: world(omp_binary_sha256="0" * 64), (), 1),
            ("json missing binary", world,
             ("--opencode-binary", str(tmp / "nope")), 2),
            ("json bad pin", lambda: world(omp_binary_mtime="garbage"), (), 3),
        ):
            code, out, _ = run(make(), *extra, "--json")
            payload = json.loads(out)
            rec("%s: exit %d and exit_code agrees" % (name, expect),
                code == expect and payload["exit_code"] == expect, (code, out))
        code, out, _ = run(str(tmp / "does-not-exist.json"), "--json")
        payload = json.loads(out)
        rec("json missing baseline: exit 3 with an error envelope",
            code == 3 and payload["exit_code"] == 3 and "error" in payload, out)

    print("%d failure(s) over %d assertions" % (len(failures), total))
    for f in failures:
        print("FAIL: %s" % f)
    return 1 if failures else 0


def os_utime(path: Path, ns: int) -> None:
    import os
    os.utime(path, ns=(ns, ns))


if __name__ == "__main__":
    sys.exit(main())
