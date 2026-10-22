Result: MIXED — 7 of 8 cells of the `check_sources_append_only.py` registry row hold under re-run and source attack, but the verdict-map cell BREAKS: a documented breach shape (row removal) and an environment failure both terminate via uncaught-exception exit 1 instead of the declared verdict behavior.

Attacked row (SKILL.md:467 at tip 58db81c4; identical text at landing commit bf65974c:453; `git diff --stat bf65974c..58db81c4 -- verifiers/check_sources_append_only.py SKILL.md` shows the script untouched, only SKILL.md +14 lines, so all line numbers below are valid at both revisions):

|`verifiers/check_sources_append_only.py`|gate|`python3 -B verifiers/check_sources_append_only.py --base <rev> --rev <rev>`|0=clean, 1=failed, 2=could-not-evaluate|`--self-test`|in-file|none|kotoba|

Environment: sandbox clone /fast/scratch/hyaku/kotoba-r54/W2RowCheckSourcesAppendOnly at 58db81c4 (cloned from the lane, `git rev-parse HEAD` → 58db81c4465b0e9b07ef2485b87d8970683afac6). No tool installs or upgrades were needed (system python3 3.14, git already present).

Counter context: `python3 -B verifiers/check_gate_registry.py --rev 58db81c4` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0, with `verifiers/check_sources_append_only.py  OK` listed. The counter passes; everything below is what the counter does not measure (its docstring says so explicitly).

---

## Findings by severity

### HIGH — verdict map cell BREAKS (script-side): row-removal breach crashes instead of grading

compare() appends removals as a 5-tuple and cell changes as a 4-tuple, but scan() prepends the commit id to both and main() unpacks exactly 5:

- verifiers/check_sources_append_only.py:70-71 — `if a is None: breaches.append((rid, "row", "removed", "", ""))` (5 elements)
- verifiers/check_sources_append_only.py:76-80 — `rec = (rid, col, b[col], a.get(col, ""))` (4 elements)
- verifiers/check_sources_append_only.py:113-115 — `for rec in b: breaches.append((c,) + rec)` → 6-tuple for removals
- verifiers/check_sources_append_only.py:175 — `for c, rid, col, old, new in breaches:` → ValueError on 6-tuples

Empirical (sandbox clone): removed the S001 row from corpus/SOURCES.md, committed, ran the declared entry command:

```
$ python3 -B verifiers/check_sources_append_only.py --base HEAD^ --rev HEAD
Traceback (most recent call last):
  File ".../verifiers/check_sources_append_only.py", line 189, in <module>
    sys.exit(main())
  File ".../verifiers/check_sources_append_only.py", line 175, in main
    for c, rid, col, old, new in breaches:
ValueError: too many values to unpack (expected 5, got 6)
exit=1
```

The gate's own docstring (line 15: "a row present at the parent and absent at the commit -> breach, exit 1"; line 21: "one line per breach, then one summary line") promises a breach line and summary; neither is printed. The `1=failed` class is reached only by CPython's uncaught-exception exit convention, and `delta()` (line 86-87, "row present -> absent") shows the removal shape was designed to reach main and crash there instead. The self-test stays green through this: `python3 -B verifiers/check_sources_append_only.py --self-test` → `self-test: 0 failure(s) over 14 assertions`, exit 0, because its "row removed" arm (line 149-151) exercises only compare(), never scan()→main().

Attack implication: the verdict-map cell's `1=failed` is true on the protected-cell path (verified: cell-change breach → `breach 26e1c502d S001 source: …` + `sources append-only breach 1 change(s) in 1 of 1 commits`, exit 1) but is delivered by crash on the removal path, with no verdict line. A reviewer re-running the gate on a real removal cannot distinguish the crash from the declared verdict without reading the traceback.

### HIGH (same cell, second defect) — environment failure maps onto `failed` instead of `could-not-evaluate`

The docstring (line 22) and the row both say 2 = usage/environment failure / could-not-evaluate. But a blob that is not valid UTF-8 crashes `git(...)`'s `text=True` decode (verifiers/check_sources_append_only.py:36-38) and the interpreter exits 1:

```
$ # appended a SOURCES.md row containing raw 0xFF bytes, committed
$ python3 -B verifiers/check_sources_append_only.py --base HEAD^ --rev HEAD
  File "/usr/lib/python3.14/subprocess.py", line 1099, in _translate_newlines
    data = data.decode(encoding, errors)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 72470: invalid start byte
exit=1
```

Exit 1 reads as `failed` — a corpus breach — for what the declared map classes as could-not-evaluate. No catch exists anywhere between blob() and `__main__` (lines 35-43, 99-118, 160-185). Per PROTOCOL.md § Gate standard ("an undeclared nonzero code reads as could-not-evaluate", PROTOCOL.md:393-395) a crash that happens to exit 1 is indistinguishable from a real breach; here the environment failure is silently graded `failed`.

### Verified-holding cells

- **Name** — HOLDS. File is a blob directly under `verifiers/` at the revision; the C2 counter lists it OK (run above).
- **Kind `gate`** — HOLDS. PROTOCOL.md:388-392: a gate "reads surfaces, compares them against expected values … and returns a verdict. A tool that cannot fail is a probe." This script reads the SOURCES.md history surface, compares against the append-only rule constants in-file, and demonstrably fails (exit 1 produced). It declares `0=clean` and `1=failed` as a gate must. Residual blind spot below.
- **Entry command** — HOLDS. Ran twice in the clone: `--base 422ffd10 --rev 58db81c4` and `--base bf65974c --rev 58db81c4`, both → `log 5a097e12b S046 used-by: …` + `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`, exit 0. Flags match argparse (`--rev` line 162, `--base` line 163). The observed `log` line (permitted `used-by` change in commit 5a097e12b) matches the docstring's report-not-grade behavior (lines 17-19).
- **Self-test `--self-test`** — HOLDS as declared. `--self-test` is a literal argparse flag (line 165) dispatching to the in-file `self_test()` (lines 168-169, 121-157); it is the script's own comparative-arm test over in-memory fixtures — no nested invocation, no subprocess, no usage text. Observed: `self-test: 0 failure(s) over 14 assertions`, exit 0; failure path returns 1 (line 157). Residual: the arms never execute scan()/main(), which is exactly why the HIGH crash above is invisible to it; and per PROTOCOL.md:398-402 a gate self-test should assert "both the exit code and a stable expected finding-id" — these arms assert breach/note counts only, and this gate's records carry no finding ids at all.
- **Pinned values `in-file`** — HOLDS. The script's only constants are in-file: `PATH = "corpus/SOURCES.md"`, `PERMITTED = ("status","recheck","used-by")`, row/header regexes (lines 29-32). No external pin file is read anywhere (no open() for read, no baseline JSON).
- **Write scope `none`** — HOLDS. Source contains no file writes (only `subprocess.run` git reads with `capture_output=True` and stdout prints); empirically `git status --porcelain | wc -l` → 0 after both entry-command runs in the clone. The self-test also writes nothing.
- **Owner `kotoba`** — HOLDS. Lane repo is kotoba-shokunin; the counter's owner check passes (row OK in the 24-of-24 run).

Exit-code production summary for the verdict-map cell (empirically produced codes: 0, 1, 2 — none missing, none undeclared):
- 0 = clean: produced (`rows clean` summary), including the permitted-log case. Holds.
- 2 = could-not-evaluate: produced twice (`--rev 0000000000000000000000000000000000000000` → stderr `rev-list failed: fatal: bad object …`, exit 2 via line 104; `--definitely-not-a-flag` → argparse usage error, exit 2). Holds.
- 1 = failed: produced with meaning on the protected-cell path; produced by crash on the removal path (no verdict line) and by crash on the decode path (wrong class — should be 2). Breaks as a whole-cell claim.

## Proposed corrections (text only; no lane files touched)

Row text: the cell declarations are correct as written — the defect is in the script, so the corrected row is byte-identical; do not widen the verdict-map cell to bless the crash behavior. Script fixes for the L1 to consider:

1. compare() line 71 → `breaches.append((rid, "row", "", ""))` (4-tuple, matching the cell-change shape; delta() lines 86-87 already render `row present -> absent` for empty old/new). The existing self-test arm still passes (it counts breaches, not shapes).
2. Wrap the blob reads in scan() (lines 107-108) in `try/except UnicodeDecodeError: raise SystemExit(2)` — an undecodable registry is could-not-evaluate, not a breach.
3. Extend self_test() with one end-to-end arm over a temp git repo exercising scan()+main() and asserting the exit code, per PROTOCOL.md:398-402; this would have caught defect 1.

## Residual risk and verification gaps

- Merge blind spot: scan() uses `rev-list --reverse --no-merges <base>..<rev> -- corpus/SOURCES.md` and diffs each commit against its first parent (lines 100-107); changes landing only inside a merge commit are never scanned. Rare in this lane's linear jj-colocated history, but the gate cannot see a merge-carried rewrite.
- Header-corruption state: if the `| id |` header (line 32 regex, case-sensitive) ever fails to match in both compared snapshots, parse() returns {} for both and the gate prints clean. I tested a header rename (`| id |` → `| ID |`) plus a protected-cell edit in one commit: it fails CLOSED (mass removal breaches → the line-175 crash, exit 1), so no silent bypass was demonstrated at this revision — but the closed failure is again the crash, not the declared verdict.
- Malformed rows (cell count ≠ header, lines 58-59) are skipped from parsing; such an edit currently surfaces only as a removal-breach crash (fails closed, crashily) rather than a graded finding.
- I fuzzed three shapes (protected-cell edit, row removal, invalid UTF-8) plus header rename and usage/bad-rev paths; other shapes (deep histories, `--quiet-log`, non-first-parent topologies) were not exercised.
- All runs were on the tip revision in my sandbox clone; the script is byte-identical at bf65974c (drift check cited above), so the findings apply to the landing commit equally.
