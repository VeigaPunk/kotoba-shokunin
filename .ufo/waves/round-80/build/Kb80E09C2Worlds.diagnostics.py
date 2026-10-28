#!/usr/bin/env python3
"""Final diagnostics for the C2 control receipt.

1. The counter's OWN generator world on the isolated six-row registry: which
   surfaces it loses and why (per-surface findings).
2. The msaf page: where the REAL first heading sits in the text view versus
   where the counter's '#'-prefix heuristic puts the first heading, and whether
   any quote can be admissible.
"""
import importlib.util, sys, os, tempfile, subprocess, hashlib, shutil
from pathlib import Path

PORT = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E09C2Worlds.counter-port.py"
spec = importlib.util.spec_from_file_location("port", PORT)
m = importlib.util.module_from_spec(spec)
sys.modules["port"] = m
spec.loader.exec_module(m)
m._WORK = tempfile.mkdtemp(prefix="probe6-", dir=os.environ["TMPDIR"])

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
REV = "398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93"
NAMES = {"spec": "S226-spec.md", "claude": "S227-claude.md",
         "factory": "S228-factory.md", "msaf": "S229-msaf.html",
         "pi": "S230-pi.md", "vibe": "S231-vibe.md"}
SID = {"spec": "S226", "claude": "S227", "factory": "S228",
       "msaf": "S229", "pi": "S230", "vibe": "S231"}


def blob(p):
    return subprocess.run(["git", "-C", LANE, "show", f"{REV}:{p}"],
                          capture_output=True).stdout


print("=== 1. the counter's own generator world, per-surface findings ===")
# build the six-row registry exactly as the G0 arm does
rows = []
snaps = {}
keys = {}
for key in m.SURFACE_ORDER:
    sid = SID[key]
    name = NAMES[key]
    raw = blob(".ufo/waves/round-79/snapshots/" + name)
    text = raw.decode("utf-8", "replace")
    view = m.text_view(name, text)
    quote = m._mech_quote(view, m.SURFACES[key])
    row = [sid, f"{m.SURFACES[key]['display']} — {m.SURFACES[key]['display']}",
           "docs", "A", "control scope",
           f"§ control; fetched {m.CAPTURE}T00:00:00Z, HTTP 200, "
           f"{len(raw)} B, sha256 {hashlib.sha256(raw).hexdigest()}",
           "control teaches cell", "mined", m.CAPTURE, "90d", m.ENTRY]
    rows.append(row)
    snaps[sid] = (name, text)
    keys[sid] = key

files = {
    m.ENTRY: m._mech_entry(rows, snaps, keys),
    m.SOURCES: m._registry_of(rows),
    m.MANIFEST: "".join(f"{hashlib.sha256(t.encode()).hexdigest()}  {n}\n"
                        for n, t in snaps.values()),
    m.PROVINCE: m.mech_province(),
    m.SKILLMD: m.mech_skill(),
}
for n, t in snaps.values():
    files[f"{m.SNAPDIR}/{n}"] = t

d = Path(tempfile.mkdtemp(prefix="genworld6-", dir=os.environ["TMPDIR"]))
try:
    m._commit_tree(d, files)
    n, findings, backed, opened = m.check(m.Repo(d, "HEAD"))
    print(f"  generator world score: {n} of {m.TOTAL}; backed={backed}")
    for f in findings:
        print("    finding:", f)
finally:
    shutil.rmtree(d, ignore_errors=True)

print()
print("=== 2. the msaf page: the real first heading vs the '#' heuristic ===")
raw = blob(".ufo/waves/round-79/snapshots/S229-msaf.html").decode("utf-8", "replace")
view = m.text_view("S229-msaf.html", raw)
raw_lines = raw.splitlines()
h1 = [i for i, l in enumerate(raw_lines) if "<h1" in l]
field = [i for i, l in enumerate(raw_lines) if "allowed-tools" in l]
print(f"  raw HTML: <h1> at line(s) {h1}; the field at raw line(s) {field}")
# the h1's TEXT in the text view
h1_text = None
for i, l in enumerate(raw_lines):
    if "<h1" in l:
        import re as _re
        t = _re.sub(r"<[^>]+>", " ", l)
        h1_text = _re.sub(r"\s+", " ", t).strip()
        h1_view_line = i
        break
print(f"  the h1's text is {h1_text!r} (raw line {h1_view_line})")
occ = [i for i, l in enumerate(view)
       if __import__("re").search(r"(?<![A-Za-z0-9_])allowed-tools(?![A-Za-z0-9_])", l)]
hash_lines = [i for i, l in enumerate(view) if l.startswith("#")]
print(f"  text view: the field at view line(s) {occ}")
print(f"  text view: lines starting with '#' at {hash_lines[:5]} "
      f"(count {len(hash_lines)}) -> {view[hash_lines[0]][:70]!r}")
print(f"  the '#'-heuristic's first heading is at view line {hash_lines[0]}; "
      f"the field is at view line {occ[0]}")
print(f"  => every window carrying the field starts at or before view line "
      f"{occ[0]}, and the counter rejects idx <= first_head+1 = "
      f"{hash_lines[0] + 1}: msaf admits no admissible quote.")

# what the counter's OWN generator derives for msaf, and why it fails
sp = m.SURFACES["msaf"]
q = m._mech_quote(view, sp)
ok, why = m.quote_location(view, q)
print(f"  the counter's generator quote for msaf: {q!r}")
print(f"    quote_location -> {ok} {why!r}")
print(f"    the label it derives: {m.SCRIPT_LABEL_FOR(q)!r} "
      f"(frozen label {sp['grant']!r})")
