# FalsifyRegistryRows — attack on the three new SKILL.md registry rows

Round 62 wave 2 (falsify). Lane tip measured: `e6da78bbe420722dd18a13182a7c4b64ce02f005`
(`git rev-parse HEAD`, run in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`).
Rows read from the **committed** blob (`git show e6da78b…:SKILL.md` lines 488–490) —
identical to the working tree.

## Verdict: NO DEFECT FOUND. All three rows are conformant and every cell claim is honest.

## 1. The registry counter at final tip

```
$ python3 -B verifiers/check_gate_registry.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
…
verifiers/check_erratum_absorption.py        OK
verifiers/check_routed_repairs_v2.py         OK
verifiers/check_scoped_rules_v31.py          OK
…
gate registry rows conformant 39 of 39 lane verifiers; phantom 0
EXIT=0
```

All three new rows are inside the first table under `## Gate registry`, exactly once
each (the checker's "exactly one row" rule passed — no duplicates), and none is a
phantom (all three name real blobs in the `verifiers/` universe at tip).

## 2. Row-by-row cell audit

### Row A — `verifiers/check_erratum_absorption.py` (SKILL.md:488)

| cell | row says | verified |
|---|---|---|
| kind | `gate` | Instrument has real failure capability: exit 1 on `measured≠5`/`controls≠2` and on `MatrixFailure`/`OSError`/`ImportError`/`AttributeError` (check_erratum_absorption.py:476-478,494-495). Gate kind honest. |
| entry command | `python3 -B verifiers/check_erratum_absorption.py --self-test` | The instrument's ONLY mode: no flag → `parser.error("--self-test is required")` → exit 2 (measured: `NO-FLAG-EXIT=2`). Command is exactly the frozen predicate. |
| verdict map | `0=clean, 1=failed, 2=could-not-evaluate` | Exit rule (lines 494–496): `return 0` iff `summary.measured == 5 and summary.controls == 2`; else 1; `CounterPinMismatch`/`EnvError` → 2 (lines 470-475). |
| self-test | `` `--self-test` `` | Real handler: `parser.add_argument("--self-test", action="store_true")` at :466. |
| pinned values | `in-file` | `COUNTER_SHA256 = "5a5adc94…52b91"` at :15, enforced against `check_scoped_rules.py` bytes at :82-85 (fails closed → exit 2). Gates may not say `none`; `in-file` is the honest value. |
| write scope | `none (read-only)` | `grep -cE 'tempfile|mkdtemp|write_text|write_bytes|mkdir|open\('` → **0** hits. Counter loaded via `path.read_bytes()`; `sys.dont_write_bytecode = True` (:80). |
| owner | `kotoba` | matches frozen OWNER constant. |

**Exit-rule claim match (the assigned attack).** The instrument's exit 0 is gated on
`measured == 5 and controls == 2` ONLY — `absorbed` is computed and printed but is
**not** in the exit condition. Live proof:

```
$ python3 -B verifiers/check_erratum_absorption.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
…
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
… (6 survivor lines)
EXIT=0
```

So "clean" on this gate means **measured 5 + controls 2, NOT absorbed 5** — exactly as
the assignment frames it. The row declares `0=clean` (the checker's own frozen verdict
class), which is the correct and only allowed rendering; the row does not claim
`absorbed 5`. **Consistent.** Matches receipt `C1-absorb-measure.txt:11` byte-for-byte
on the summary line.

### Row B — `verifiers/check_routed_repairs_v2.py` (SKILL.md:489)

| cell | row says | verified |
|---|---|---|
| kind | `gate` | Exit 1 when score<6 (`return 0 if score == 6 else 1`, :646). Real failure capability. |
| entry command | `--rev <rev>` | `parser.add_argument("--rev", default=None, …)` :613. |
| verdict map | `0=clean, 1=failed, 2=could-not-evaluate` | 0 iff `score==6`; 1 if score<6; 2 on unresolved rev / unreadable tree / missing LOG.md|QUALITY.md blobs (:623-637). |
| self-test | `` `--self-test` `` | Real handler :614; self-test returns `0 if not failures else 1` (:608). |
| pinned values | `in-file` | `INPUT_PATHS`, base rev and expected-count constants in-file. |
| write scope | `none (read-only)` | Zero write-syscall patterns (grep count 0). All subprocess calls are read-only git (`cat-file`, `ls-tree`, `rev-parse --verify`, `show`). |
| owner | `kotoba` | ✓ |

Live check of the entry command:

```
$ python3 -B verifiers/check_routed_repairs_v2.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
R-a count correction: ok … R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
EXIT=0
```

**Consistent.**

### Row C — `verifiers/check_scoped_rules_v31.py` (SKILL.md:490)

| cell | row says | verified |
|---|---|---|
| kind | `gate` | Exit rule `predicate(args.fetch, found)` (:2709, :1627-1631): 0 iff fetching AND `TARGET` frozen AND `found >= TARGET`; no-fetch always 1; `TARGET None` → 1; 2 on unreadable own bytes / non-40-hex rev / git failure (:2642-2654,2671-2672). Real failure capability. |
| entry command | `--rev <rev> --fetch` | Handlers `--rev` :2634, `--fetch` :2635 exist. |
| verdict map | `0=clean, 1=failed, 2=could-not-evaluate` + annotation | Map matches `predicate`/`main` returns. Annotation audited below. |
| self-test | `` `--self-test` `` | Handler :2637; rejects combination with `--rev/--fetch/--json` via `ap.error` → exit 2 (:2645-2646). |
| pinned values | `in-file` | `BASE61`, `PREDICATE_LINE`, `RECEIPT`, `KEY_ROWS`, `HOSTS`, survivor-id catalogue in-file. |
| write scope | `self-test repos under $TMPDIR (removed); --fetch reads the network` | `tempfile.mkdtemp(prefix="csr-world-")` :2175, `mkdir`/`write_bytes` :2182-2183, `shutil.rmtree(td)` in `finally` :2626-2627 (removal guaranteed even on failure). Fetch via `curl -sSL --max-time 30 …` subprocess :1551-1567. Honest. |
| owner | `kotoba` | ✓ |

**Annotation audit** — every clause measured live:

```
$ timeout 110 python3 -B verifiers/check_scoped_rules_v31.py --self-test
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
EXIT=0
```

- "closes five of the six measured survivor instances (E2c ×2, E2e ×2, E2f G7)" —
  measured `survivors closed 5 of 6`; the six frozen ids are loaded from
  `check_erratum_absorption.ERRATA` (:2563-2570), not restated, and the expected
  verdict tuple `(True×5, False)` is asserted (:2577-2579).
- "the r61 worlds/eligible line unchanged" — `worlds reject 7 of 7; eligible rows
  pass 4 of 4` printed and `check`ed against `(7,7)`/`4` (:2533-2539).
- "G9 compound-purpose stays a declared bound" — `bool(after[g9_id]) == False`
  asserted (:2612-2613) and printed.
- "the frozen counter's bytes are unchanged" — `check_scoped_rules.py` sha256
  `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`
  (`sha256sum`, this seat), matching the pin `COUNTER_SHA256` the instrument enforces;
  v31's self-test scores the frozen counter via `absorption.load_counter` (:2552)
  which raises on any byte drift.

**Consistent — all four annotation clauses verified on committed bytes.**

## 3. Cross-checks

- Frozen `check_scoped_rules.py` row (SKILL.md:487) carries the r62 absorption
  annotation `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2` —
  matches both the receipt and this seat's live run (§2A). The routed r61 item
  ("annotated with the r62 absorption finding") is satisfied.
- Committed rows == working-tree rows (`git show e6da78b…:SKILL.md` vs `SKILL.md`
  lines 488–490 identical).
- Receipts: `C1-v31-successor.txt` tail shows `exit=0` on both `--self-test` and the
  `--rev … --fetch` CLI; `C1-absorb-measure.txt:11` matches the live matrix line.
- Extra handler `--json` (:2636) is unlisted in row C — not required: the frozen
  checker only demands that flags *named in the self-test cell* have handlers.
- Tooling: no installs needed or performed (system python3/git suffice); pacman
  paused host-wide per directive.

## 4. Residual risk / observations (non-blocking)

1. **Row A is unannotated.** A reader skimming `0=clean` could misread the verdict as
   "no errata survived" — the landed instrument exits 0 with `absorbed 2 of 5;
   surviving 6`. The adjacent `check_scoped_rules.py` row does carry the annotation
   quoting exactly that line. The row is *correct* (the checker requires `0=clean`;
   "clean" is the frozen verdict class, and the instrument's exit rule is
   measured+controls only), so this is a legibility asymmetry, not a dishonesty.
   Informational only — no row change required for conformance.
2. The checker (by its own docstring, Q31) does not run the verifiers; this seat ran
   all three live: absorption `--self-test` exit 0, v2 `--rev <tip>` exit 0 `6 of 6`,
   v31 `--self-test` exit 0 with `0 failure(s) over 201 assertions`.
3. Write-scope claims for rows A/B verified by pattern grep (0 write-syscall hits)
   rather than strace; both files are small (500/650 lines) and fully greppable.

## Findings by severity

- **None.** All three rows: conformant (39/39, phantom 0, exit 0), kind `gate` honest
  (each instrument has real exit-1 capability), self-test flag backticked AND
  implemented, pinned-values `in-file` accurate, write-scope claims match the code,
  owner `kotoba`, and each verdict map matches the instrument's actual exit rule —
  including the subtle case that absorption's exit 0 means *measured 5 + controls 2*,
  not *absorbed 5*.
