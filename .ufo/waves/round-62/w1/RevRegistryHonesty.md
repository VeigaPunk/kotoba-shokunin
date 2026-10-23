# RevRegistryHonesty — round-62 wave-1 registry honesty review

Seat: `KotobaR62.RevRegistryHonesty` (reviewer, wave 1). Date: 2026-10-23.
Scope: (1) r61 `check_scoped_rules.py` registry-row honesty; (2) `check_gate_registry.py` count at the
dispatch tip; (3) would-be conformance of new `probe`/`gate` rows for the two r62 instruments, tested at
real revisions in a scratch clone; (4) Q35/Q46 wording — is any `claim withdrawn` annotation owed after
the E2f finding. Bounds honored: lane/fleet read-only (git read commands only), all mutations confined to
the scratch clone under `/fast/scratch/hyaku/kotoba-r62/RevRegistryHonesty/`, no dispatch, no pacman.

---

## 1. The r61 `check_scoped_rules.py` registry row (SKILL.md:486 at dispatch tip `45a7ecfa`)

The row, verbatim:

```markdown
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — redesigned v3 round 61 (provenance-authenticating arms; measured on seven r60 worlds), the round-60 exploratory ruling (E2) unchanged | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

- **Kind is `gate`** — yes. The counter accepts it (§2), and per PROTOCOL.md:355 the capability route
  would demand a *probe*; the operator route keeps this a gate and the row says `gate`.
- **Self-test flag exists** — yes, and it is an *exact active handler*: `verifiers/check_scoped_rules.py:2484`
  is `ap.add_argument("--self-test", action="store_true")`, mutually exclusive with `--rev/--fetch/--json`
  (`:2493`). The registry counter's AST handler check passes it.
- **Does it pin the frozen claim/sha?** The frozen **claim** is in-cell ("redesigned v3 round 61 …
  measured on seven r60 worlds"). The frozen **sha** is not printed in the row; the row's pinned-values
  cell is `in-file`, which is honest here: the counter computes and prints its own digest
  (`self_sha()`, `check_scoped_rules.py:465-468`; printed at `:2494` and `:2537` as `counter sha256 <hex>`),
  and the frozen value is recorded in `corpus/knowledge/scoped-rules-counter-round61.md` (`counter sha256
  `5a5adc94…`, frozen at `6a7f722e``). Working-tree check reproduces the freeze exactly:

```text
$ sha256sum verifiers/check_scoped_rules.py
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  verifiers/check_scoped_rules.py
```

  matches the frozen r61 pin `5a5adc94…`. **No capabilities row exists for it** — SKILL.md has no
  capabilities table at all (section map checked; `grep -i capabilit SKILL.md PROTOCOL.md corpus/QUALITY.md`
  hits only unrelated prose), exactly one registry row names the file, and nothing in `verifiers/README.md`
  or the entry constitutes a second row. Operator route respected.

**Row verdict: honest and conformant as landed.** The only owed change is the r62 absorption annotation
(§4/§5), not a correction of any existing cell.

## 2. Counter run at the dispatch tip

Command and output (run from the lane root):

```text
$ python3 -B verifiers/check_gate_registry.py --rev 45a7ecfac9e203297f3146c45d63f5e79367470c
…34 OK lines…
verifiers/verify_surfaces.py                 OK
gate registry rows conformant 35 of 35 lane verifiers; phantom 0
exit=0
2026-10-23T20:52:53Z
```

**Count: 35 of 35, phantom 0, exit 0.** Universe at that rev is exactly the 35 `.py`/`.sh` blobs under
`verifiers/` (`git ls-tree`, no recursion; JSON fixtures and `fixtures/` never count). Re-runs during this
review: at `a1cb8abc` (then-HEAD) also 35 of 35 exit 0; at `9228be47` (tip at report time) **36 of 36,
phantom 0, exit 0** — the growth is `verifiers/check_seat_counts.py` + its registry row landed **in the
same commit** `9f03dcd7` (row at SKILL.md:488), which is precisely the landing pattern §5 D1 requires for
the r62 instruments.

## 3. Would-be conformance of new rows for the r62 instruments — measured, not guessed

Method: `git clone --shared` of the lane into
`/fast/scratch/hyaku/kotoba-r62/RevRegistryHonesty/lane` (clone HEAD `5c924b02`; the lane itself untouched).
`check_gate_registry.main()` reads **both** SKILL.md and the verifier blobs *at the measured revision*
(`t.read("SKILL.md")`, `git show <rev>:…`), so each variant below is a **commit in the scratch clone** and a
full `main()` run against it — not a helper-only call. The two r62 instruments did not exist at any measured
rev, so the scratch clone carries minimal stubs whose only load-bearing property is the real
`argparse` `add_argument("--self-test", …)` handler the rows name; stub bytes are declared scratch-only and
never leave the clone. Row-kind/flag/pin/scope verdicts are about the **row text + handler contract**, which
is what the counter judges.

### 3a. Positive: all three new rows conform (exit 0)

Rows tested (my drafts for the two instruments + the successor row the sibling draft omits):

```markdown
| `verifiers/check_erratum_absorption.py` | gate | `python3 -B verifiers/check_erratum_absorption.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — r62 C1: erratum absorption matrix over E2/E2b/E2c/E2e/E2f against the landed v3 counter, whose sha256 `5a5adc94…` is pinned in-file and fails closed on byte drift | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_routed_repairs_v2.py` | gate | `python3 -B verifiers/check_routed_repairs_v2.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — r62 C2 successor: self-derived committed count + honest-pass over the frozen six (frozen counter unmodified, imported in-process) | `--self-test` | in-file | none (read-only) | kotoba |
| `verifiers/check_scoped_rules_v31.py` | gate | `python3 -B verifiers/check_scoped_rules_v31.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — r62 E2f successor (v3.1): adds the frozen E2f form (G5 key-on-line + G7 raw event-claim conjunct; F6 compound-purpose bound declared surviving); worlds/eligible line unchanged | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

```text
scratch rev 3375b89dde97cefbcbba57811eb80fd60d532173 (universe 38)
verifiers/check_erratum_absorption.py        OK
verifiers/check_routed_repairs_v2.py         OK
verifiers/check_scoped_rules_v31.py          OK
gate registry rows conformant 38 of 38 lane verifiers; phantom 0
exit=0
```

Kind rules that force `gate` for both instruments, measured:

- **Naive probe** (kind `probe`, verdict map `0=clean, 1=failed, 2=…`, files present):

```text
verifiers/check_erratum_absorption.py        no probe verdict map declares 1=failed; probe script has an exact --self-test handler
verifiers/check_routed_repairs_v2.py         no probe verdict map declares 1=failed; probe script has an exact --self-test handler
gate registry rows conformant 36 of 38 lane verifiers; phantom 0
exit=1
```

- **Minimal legal probe** (verdict map `0=clean` only — still rejected because the script handles
  `--self-test`; this is Q46's "a `probe` relabel is checked against the counter first" clause):

```text
verifiers/check_erratum_absorption.py        no probe script has an exact --self-test handler
gate registry rows conformant 36 of 38 lane verifiers; phantom 0
exit=1
```

- **Gate with `none` cells** (self-test `none` + pinned `none`):

```text
verifiers/check_routed_repairs_v2.py         no gate with self-test none; gate with pinned values none
gate registry rows conformant 36 of 38 lane verifiers; phantom 0
exit=1
```

All rejections at 2026-10-23T20:59:13Z. **Conclusion: any `probe` row for either instrument is
unlandable while the instrument has a `--self-test` handler (both frozen predicates are `--self-test`
lines), so both rows MUST be `gate`, MUST name their real flag in backticks, and a `gate` may not say
`none` in the self-test or pinned-values cells.** `2=could-not-evaluate` is honest for both (the absorption
instrument fails closed exit 2 on sha drift; the successor maps could-not-evaluate like its parent).

The sibling's alternative cell style (ExecRegistryRows.md: entry `--self-test` for the absorption row;
pinned-values cells naming `verifiers/check_scoped_rules.py` / `verifiers/check_routed_repairs.py`)
**also conforms** — tested in the same clone with my corrected r61 row (§5) in place:

```text
scratch commit "corrected r61 row + sibling instrument rows"
verifiers/check_scoped_rules.py              OK
verifiers/check_erratum_absorption.py        OK
verifiers/check_routed_repairs_v2.py         OK
verifiers/check_scoped_rules_v31.py          OK
gate registry rows conformant 38 of 38 lane verifiers; phantom 0
exit=0
2026-10-23T21:00:57Z
```

Both styles pass; pick one per row and keep the write-scope cell matching the landed bytes' real side
effects (Q31 leaves actual exit/write behavior to reviewers — that is this seat's residual check at landing).

### 3b. Ordering: rows and files must land in the same commit

The counter reads both sides from one rev, so any intermediate tip violates Q35 in one of two measured
directions — rows without files:

```text
(PHANTOM run — SKILL.md rows committed, stub files absent at that rev)
PHANTOM verifiers/check_erratum_absorption.py
PHANTOM verifiers/check_routed_repairs_v2.py
PHANTOM verifiers/check_scoped_rules_v31.py
gate registry rows conformant 35 of 35 lane verifiers; phantom 3
exit=1
```

and files without rows (the inverse, direct from `judge()`: a universe path with zero naming rows gets
`why: ["registry rows naming it: 0 (need 1)"]` → exit 1). E1 addendum 2 (`9228be4`) orders "the instrument
and its hollow/label/presence controls (same commit)" but commit-order item 6 still lands SKILL registry
rows later (with SOURCES/entry/lesson) — that window breaks the invariant. Landed precedent `9f03dcd7`
(`check_seat_counts.py` + row in one commit) shows the fix. **Each of the three rows lands in the same
commit as its file.**

## 4. Q35/Q46 wording after the E2f finding — no `claim withdrawn` anywhere

- **Q35** (`corpus/QUALITY.md:46`): every `verifiers/*.py|.sh` needs exactly one registry row; a gate row
  names a self-test flag the script handles itself. Drives D1/D2 below; nothing about withdrawal.
- **Q46** (`corpus/QUALITY.md:57`): the in-cell `claim withdrawn` annotation is for **"a counter whose
  claim is withdrawn"**. The E2f finding does **not** withdraw the v3 counter's claim — the claim in the
  row is the seven-r60-worlds measurement (committed receipt `b4a8d2ee`), which still holds. The finding
  narrows erratum-absorption coverage, which the row never asserted. Precedent wording ("claim withdrawn
  rNN before data; not a claim gate until redesigned and re-controlled", rows for `check_agentdef_boxes`
  r56 / `check_infoless_fences` r57 / `check_sweep_mutants` r58) is reserved for withdrawn claims;
  `grep -c "claim withdrawn" SKILL.md` = **3** today and must stay 3 after r62.
- **Therefore: no `claim withdrawn` annotation is needed anywhere.** The scoped-rules row keeps `gate` and
  gains the r62 absorption annotation in-cell (§5 text, counter-validated 38 of 38). The sibling reached
  the same verdict; my probe runs additionally prove the `probe` relabel Q46 warns about is mechanically
  rejected (§3a), not merely ill-advised.
- **Where the E2f contradiction actually lives:** the committed knowledge entry
  `corpus/knowledge/scoped-rules-counter-round61.md` § Arms states "**A2 semantic action (guarded, E2f)** —
  … with a RAW tokenizer (`content_words` strips backticked spans) and `apply` excluded from the claim
  verbs (MutA2's measured guards G5+G7+G9)". The landed bytes carry no G7/G9: `action_conjunct`
  (`check_scoped_rules.py:1010-1046`) implements only the forward 2/3 overlap, page-occurrence, and reverse
  support checks — there is no claim-verb set, no all-cell-words-on-one-line claim-span rule, no
  compound-purpose rule (corroborating the plan's E1 finding, measured pre-data by the instance seats).
  Q46 is registry-scoped, so the fix is **not** a registry annotation: the entry needs a dated correction
  in the r62 data commit, e.g. appending to the A2 bullet: *"r62 correction: G7/G9 were the frozen
  requirement (plans/round-61.md § E2f addendum) but are absent from the landed bytes — measured pre-data;
  the E2f instance survives; carried by `check_scoped_rules_v31.py`."* This is exactly the round's mined
  lesson class ("erratum recorded as absorbed without an arm-level receipt"). The entry's "Not held" list
  discloses A2's F6 bound but not the G7/G9 absence — that is the wording gap.

## 5. Defects and exact corrections, by severity

**D1 (blocks the registry invariant in the landing window — process).** E1 addendum 2's commit order lands
the instruments before SKILL registry rows (item 6). Between those commits any `check_gate_registry` run
exits 1 in either direction (measured both ways, §3b). **Correction:** land each row in the same commit as
its instrument (precedent `9f03dcd7`). Applies to all three files, not two.

**D2 (defect in the sibling's candidate block).** `ExecRegistryRows.md`'s candidate table has no row for
`verifiers/check_scoped_rules_v31.py`. The successor still lands under `verifiers/` (E1 addendum keeps it
as landed fix evidence and *grows* its scope to E2c 5/6, E2e, E2f G7), so the moment the file lands the
counter exits 1 with `registry rows naming it: 0 (need 1)`. **Correction:** add the third row (text in
§3a, validated).

**D3 (stale sibling blocker).** ExecRegistryRows.md blocks on "plan internally inconsistent: `surviving 2`
vs `surviving 1`". Resolved upstream by erratum E1 (`5c924b02`): the predicate is now
`errata measured 5 of 5; absorbed K of 5; surviving N; controls 2 of 2` with K/N computed. **Correction:**
no count-bearing text in any registry annotation until the matrix runs (my §5 row text below is
count-free).

**D4 (corpus honesty).** The entry's A2 "measured guards G5+G7+G9" sentence over-claims the landed bytes
(§4). Fix in the r62 data commit via the entry correction + planned Q57/lesson; no registry change.

**D5 (style fork, not a defect).** Two validated cell styles for the instrument rows (§3a): entry-command
`--rev <rev>` with the finding in the verdict-map cell (my drafts) vs entry `--self-test` with
pinned-values naming the consumed frozen counter (sibling's). Both 38 of 38. Either may land; do not mix
per-row without re-running the counter.

**Exact corrected r61 row** (the only row text this review changes; counter-validated 38 of 38 exit 0 at
2026-10-23T21:00:57Z):

```markdown
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — redesigned v3 round 61 (provenance-authenticating arms; measured on seven r60 worlds), the round-60 exploratory ruling (E2) unchanged; r62 absorption matrix: E2f (A2 guarded action) unabsorbed — the G7 raw event-claim conjunct and the G9 compound-purpose conjunct are absent from the landed bytes; carried by the v3.1 successor | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

Note: E1 addendum measured **E2c conditions 5/6 and E2e also absent** (at-least-three-survivors), so if the
integrator prefers the annotation to name every surviving class, extend the clause to "E2c (conditions
5/6), E2e, E2f unabsorbed" — keep it count-free until the matrix prints K/N. I tested only the E2f-only
wording.

## 6. Residual risk and verification gaps

- The two r62 instruments and the v31 successor do not exist at any rev I measured; §3's verdicts bind the
  **row text + `--self-test` handler contract**, not the instruments' actual behavior. Their real
  write-scope cells must be reconciled with the landed bytes at the landing commit (Q31).
- Scratch stubs and scratch commits are mine, under `/fast/scratch/…/RevRegistryHonesty/lane` (a
  `--shared` clone); the lane repo was only read (git log/show/ls-tree/cat-file/diff, sha256sum, counter
  runs). No lane, fleet, `.ufo/state`, or jj/git-index mutation.
- The lane tip moved three times during this review (`45a7ecfa` → `a1cb8abc` → `5c924b02` → `9228be47` +
  two more during writing); counts are stamped per rev above. If more verifiers land, re-run
  `check_gate_registry.py --rev <tip>` after the last landing.
- I did not run `check_scoped_rules.py --self-test` (the C1 no-harm arm owns that re-run) nor the
  absorption matrix (ExecAbsorbInstrument owns it); the E2f absence is cited from the plan's E1 addendum
  plus my read of `action_conjunct`, not from an instrument run.
- The plan says the row is "annotated with the r62 absorption finding" — if wave 2 falsifies the matrix's
  K/N or survivor set, the annotation's class list (D5 note) must be re-derived from the receipt, not from
  this report.

---

Installs: **no installs** (no pacman; only existing git/python3 used).
Blockers: **none** (the sibling's plan-inconsistency blocker is resolved by erratum E1 at `5c924b02`).
Attacked/produced: attacked the r61 scoped-rules registry row, the gate-registry count at the dispatch tip,
and would-be probe/gate rows for both r62 instruments with measured rejections and a same-commit landing
rule; produced the corrected r61 row text, a third (v31) row the sibling draft omits, and the
no-`claim-withdrawn` wording verdict with the entry-correction locus.
