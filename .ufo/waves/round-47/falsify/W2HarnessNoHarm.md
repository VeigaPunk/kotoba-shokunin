verdict: HOLDS — `verify_harness_claims.py` at 7ad7fad vs c61a973: pass count and DRIFT id set are equal (21/28, same seven ids); the only observed-value change, `oc.roots.names_plus_builtin` 10 → 11, is caused solely by the `OC_BIN` constant move (a 2×2 code×binary matrix isolates it), and it *restores* a built-in term the removed channel had silently dropped.

Lane: KotobaR47-2.W2HarnessNoHarm-2 (leaf, no subagents dispatched).
Target: `verifiers/verify_harness_claims.py` @ 7ad7fadfc09354b74fb66605dfb0c1182c115a2f.
Scratch (canonical layout, symlinked siblings, `--no-hardlinks` clone):
`/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2HarnessNoHarm-2/{kotoba-shokunin=7ad7fad, base=c61a973}`.
Host `plazir27`, python3 3.14 (stock). No tool installed or upgraded this lane (nothing
needed beyond stock python3 + coreutils); no pacman transaction was attempted.

---

## 1. The change under attack

`git diff c61a973 7ad7fad -- verifiers/verify_harness_claims.py` (3 insertions, 2 deletions):

- `verifiers/verify_harness_claims.py:19` (docstring): the opencode authority line moved
  from `` `~/.opencode/bin/opencode` `` to
  `` `~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` ``
  `(npm opencode-ai, round 47)`.
- `verifiers/verify_harness_claims.py:56`: `OC_BIN = HOME / ".npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe"`
  (was `HOME / ".opencode/bin/opencode"`).

Nothing else in the file changed. `verifiers/baseline.json` changed only in
`measured_against` (omp sha/mtime, opencode sha, `round47_note`); the `checks` block
— including `oc.roots.names_plus_builtin` `expect: 7` (`verifiers/baseline.json:87`) —
is byte-identical at both commits.

## 2. No-harm measurement (the acceptance)

Commands (both arms, same host state, same session tree; cwd = the respective clone root):

```
cd /fast/scratch/kotoba-r47/w2/KotobaR47-2.W2HarnessNoHarm-2/kotoba-shokunin && python3 -B verifiers/verify_harness_claims.py ; echo EXIT=$?
cd /fast/scratch/kotoba-r47/w2/KotobaR47-2.W2HarnessNoHarm-2/base        && python3 -B verifiers/verify_harness_claims.py ; echo EXIT=$?
```

| arm | commit | exit | pass | DRIFT id set | `oc.roots.names_plus_builtin` observed |
|---|---|---|---|---|---|
| before | c61a973 | 1 | **21/28** | omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue.total, omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin | **10** |
| after | 7ad7fad | 1 | **21/28** | *identical seven ids, same order* | **11** |
| landed receipt `.ufo/waves/round-47/after/verify_harness_claims.out` | 7ad7fad | 1 | 21/28 | identical | 11 (names+builtin=11) |
| recorded before-battery `.ufo/waves/round-47/before/verify_harness_claims.py.out` | c61a973 | 1 | 21/28 | identical | 10 (names+builtin=10) |

→ **Pass count equal (21/28), DRIFT id set equal (same seven ids).** My reruns also
reproduce the landed receipt and the recorded before-battery byte-for-byte on the pass
line and the DRIFT list.

Full producer JSON diff (tip `--json` vs base `--json`, same host):
`top-level keys equal: True`, `modes equal: True`, `verdicts equal: True`,
`summary_paths equal: True`, `per_skill equal: True`, and the **only** differing
observation fields are:

```
builtin_names        (0 -> 1)
roots_plus_builtin   (10 -> 11)
```

`--self-test` at both commits: `self-test: 0 failure(s) over 10 assertions`, exit 0.

## 3. Where the 10 → 11 comes from (the OC_BIN constant, isolated)

`oc.roots.names_plus_builtin` = `len(names) + builtin`
(`verifiers/verify_harness_claims.py:504`), where
`builtin = 1 if b"customize-opencode" in binary.read_bytes() else 0`
(`verifiers/verify_harness_claims.py:479`), and `names` enumerates
`~/.agents/skills`, `~/.config/opencode/skills`, `~/.claude/skills` (lines 473-476).

Measured: `root_live_names` = **10 in both arms**; `builtin_names` 0 → 1. So the delta
is *not* a skill-set change — it is the built-in term.

Counterfactual 2×2 matrix (script code × binary actually read); artifact:
`.ufo/waves/round-47/falsify/W2HarnessNoHarm.matrix.txt`:

| script code | `--oc-bin` | names+builtin | pass | exit |
|---|---|---|---|---|
| base c61a973 | `~/.opencode/bin/opencode` (**absent** on this host) | 10 | 21/28 | 1 |
| base c61a973 | npx `opencode-ai/bin/opencode.exe` | **11** | 21/28 | 1 |
| tip 7ad7fad | `~/.opencode/bin/opencode` (absent) | 10 | 21/28 | 1 |
| tip 7ad7fad | npx `opencode-ai/bin/opencode.exe` | **11** | 21/28 | 1 |

**The code change is inert on the observations; the constant move is the entire cause.**
Repro:
```
cd <scratch>/{base|kotoba-shokunin} && python3 -B verifiers/verify_harness_claims.py \
  --oc-bin "$HOME/.opencode/bin/opencode"            # -> names+builtin=10
cd <scratch>/{base|kotoba-shokunin} && python3 -B verifiers/verify_harness_claims.py \
  --oc-bin "$HOME/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe"  # -> 11
```

Why it moved: `~/.opencode/bin/` was removed from this host on 2026-10-20 (the v2.0.26
channel), so at BASE the constant pointed at a **dead path** → `binary.is_file()` false →
`builtin = 0`. The live npx ELF **does** carry the built-in skill name:
`grep -c -a -F customize-opencode ~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` → `2`.
So tip's 11 = 10 host skill names + 1 built-in; base's 10 = 10 names + 0 built-in — i.e.
the constant move **restored** a term the dead path had silently dropped (round-10's own
doc, `corpus/knowledge/harness-verifier-round10.md:126`, treats the built-in as part of
this row: "18 == 17+1 … builtin `customize-opencode` confirmed present in the opencode ELF").
The row was already in DRIFT (expect 7) at both commits, so no verdict flipped and no
baseline re-pin was needed.

### 3a. Binary identity of the new OC_BIN (freshness cross-check)

```
sha256sum ~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
  179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
sha256sum /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3
  179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9      # == frozen SHA256SUMS
```
`stat -c '%i'` → both paths are inode **43795736** (hardlink; `opencode-ai/bin/opencode.exe`
and `opencode-linux-x64/bin/opencode`), 186,013,824 B. The sha also equals
`verifiers/baseline.json` `measured_against.opencode_binary_sha256`. The path the
verifier now reads is byte-identical to the evidence the C1 re-derivation was measured on.

Docstring authority strings, verified present in the new ELF:
`available_skills` ×3, `EmbeddedSource.make` ×1, `customize-opencode` ×2.
omp ELF unchanged: `A8n` ×3, `H7s` ×9, `ldl` ×20, template anchor
`Compress into one routing hint` ×1 (273 B template, sha `c1f03c8e…` — matches baseline).

---

## 4. Findings, by severity

### F-1 (MED — calibration/consistency) The moved constant creates a *new* producer-vs-independent disagreement on `oc.roots.names_plus_builtin`

The independent oracle `verifiers/verify_harness_independent.py` never reads the
opencode binary; it derives the row from the log's source directories and **declares the
built-in term 0 by construction** (`verifiers/verify_harness_independent.py:614-615`:
`"…plus the shared agents root (%d names); built-in names: 0 by declaration"`).

Measured (`verifiers/verify_harness_independent.py --json`, exit 0):
`oc.roots.names_plus_builtin = 10`.
Against the captured producer payloads, using the comparator's own predicate
(`compare_harness_independent.py:210`, mode `equal` → strict equality):

```
live tip   11  vs independent 10 -> predicate_agree('equal', 11, 10) = False   # NEW
live base  10  vs independent 10 -> predicate_agree('equal', 10, 10) = True    # pre-existing
```

The comparator documents exit **1** for a protocol disagreement
(`verifiers/compare_harness_independent.py:117-118`). [INFERENCE] the join's exit code
would go from 0 to 1 on this row once the session-tree blocker below is out of the way;
I could not measure that exit code (see §5).

This falsifies a still-live corpus claim, unchanged by round 47 —
`corpus/knowledge/harness-independent-round37.md:464-465` (at 7ad7fad):

> **`oc.roots.names_plus_builtin`'s built-in term is declared 0** in both instruments
> (the string `customize-opencode` is absent from the binary); a future binary carrying
> it would move both readings together, un-adjudicated.

Two halves of that sentence are now false: (a) the string is **not** absent from the
current binary (2 hits in the 1.19.3 ELF); (b) a binary carrying it did **not** move both
readings together — the producer moved to 11 while the independent instrument stayed at
10, because it never reads the binary. Round 47 re-derived the *harness* row's channel
(OC_BIN) without re-opening the *independent* row or the r37 sentence that predicts the
pair's behaviour. [INFERENCE] the disagreement is a genuine protocol disagreement rather
than an un-adjudicated pair, because `mode` for the row is `equal` in the live payload
(`verify_harness_claims.py:544`) and the comparator's `equal` branch is strict equality
(`compare_harness_independent.py:210-213`).

Suggested (not applied — read-only lane): either teach the independent instrument to read
the same built-in marker, or scope/adjudicate the row; and correct the r37 sentence.

### F-2 (LOW — disclosure/calibration) The ledger discloses the pass count but not the observed-value move

`LOG.md:2326` (round-47 landing, "Not claimed"):

> Not claimed: `verifiers/verify_harness_claims.py` 21/28 before and after (same seven
> DRIFT ids; three host skills born 2026-10-20 — Q09 debt)

Literally true and confirmed by my reruns — but the same commit moved the `OC_BIN`
constant, and that move changed this row's *observed* value 10 → 11. The ledger attributes
the drift solely to the three new host skills; the built-in-term restoration is not
mentioned anywhere in the round-47 entry (`LOG.md:2321-2326`) or in `plans/round-47.md:43`.
The raw receipt does carry it (`.ufo/waves/round-47/after/verify_harness_claims.out`,
`names+builtin=11`), so this is a prose gap, not a missing measurement.

### F-3 (LOW — the assignment's phrasing is imprecise; the code is fine) Only 1 of 15 `oc.*` checks reads the binary

"confirm the oc.* checks read the new binary" is only literally true of one check.
`binary` is referenced in `oc_observations` exactly once
(`verifiers/verify_harness_claims.py:478-479`); the other 14 `oc.*` rows are derived from
the opencode **log** and the skill-root directories and are byte-identical between base
and tip (proved by the JSON field diff in §2: only `builtin_names` and
`roots_plus_builtin` differ). Only `oc.roots.names_plus_builtin`
(`verifiers/verify_harness_claims.py:544`) consumes the binary.

### F-4 (LOW — efficiency) The move makes every run allocate ~186 MB for one substring test

`verifiers/verify_harness_claims.py:479` does `b"customize-opencode" in binary.read_bytes()`
— the whole 186,013,824-byte ELF is materialised in RAM. At BASE the path was dead so
zero bytes were read; at tip every invocation now allocates the full image. A chunked
scan (e.g. 8 MiB windows with a 17-byte overlap) yields the same verdict at constant
memory. Not a correctness defect; noted because the change introduced the cost.

### F-5 (INFO — positive) Channel consistency and no stale path left in the target file

`verifiers/verify_surfaces.py:130` and `verifiers/check_substrate_pins.py:66` point at the
same npx ELF, so the three default paths moved together as the round-47 note claims
(`verifiers/baseline.json` `round47_note`). `grep -n "\.opencode" verifiers/verify_harness_claims.py`
at 7ad7fad → **no hits**: no stale reference remains in the target file. The only
remaining `~/.opencode/bin` mentions in the repo are historical corpus prose
(`corpus/knowledge/claude-md-surface.md:9`, `opencode-extraction-round14.md:98`,
`opencode-offer-trace-round8.md:6`, `skill-activation-telemetry.md:21`) — those are dated
round-8/10/14 records, and `corpus/knowledge/instruction-surface-census-round13.md:218`
already records the removal ("v2.0.26 (`~/.opencode/bin`, removed 2026-10-20)"), so no
live gate points at the dead channel.

---

## 5. What I did NOT check

- **The producer↔independent join exit code was never measured.** Both arms
  (`--live-json tip` and `--live-json base`) exit **2** with the *identical* error class:
  `false blocker: scoped row omp.catalogue.{found,matched,missing_names} declares
  observable {"candidate_blocks": 23882,…} but recomputation gives {"candidate_blocks":
  23892,…}` (tip) / `24030` (base). The blocker is the r39 committed scope probe
  (`verifiers/harness-independent-scope.json`, `kind=rule-spread-census`) recomputing over
  `$HOME/.omp/agent/sessions`, whose candidate-block count grows with every session file
  written during the run (the arm is live-session-hostile). Artifact:
  `.ufo/waves/round-47/falsify/W2HarnessNoHarm.join-blocked.txt`. Because the failure is
  identical for both arms it is not attributable to the `OC_BIN` move; F-1's row-level
  divergence is measured directly from the two captured payloads plus the comparator's own
  `predicate_agree`.
- I did **not** run the rest of the round-47 battery (surfaces, pins, checklist, corpus
  integrity/independent, fault harness, floors) — other lanes; I only re-ran the harness
  verifier and its independent oracle.
- I did **not** execute `opencode` in any form (contract: never run the
  `~/.local/bin/opencode` npx wrapper); the ELF was read as bytes only. `omp` was never
  launched either — only its bytes and the sqlite cache were read.
- I did **not** verify the omp-side observations are time-invariant: `session files scanned`
  moved 13874 → 15048 → 15125 across the battery and my runs (the host keeps writing
  session files). The catalogue row *values* (total 10, matched 7, missing
  `['create-toolset','unreal-mcp','unreal-skill']`) were identical in every arm I ran.
- I did **not** re-derive the C1 surfaces/census re-derivation, the C2 checklist trigger
  rule, or the C3 governance erratum (other lanes).
- I did **not** check non-Linux channels, the `~/.local/bin/opencode` wrapper's own
  resolution semantics, or the omp binary sha pin in `check_substrate_pins.py`.
- I did **not** attempt the comparator's `--self-test` (round-46 carried residuals there;
  out of my lane, and it cannot change the F-1 row verdict).

## 6. Verdict

**HOLDS** for the assigned no-harm property: tip and base agree on 21/28 and on the exact
seven DRIFT ids; the single observed-value change (`oc.roots.names_plus_builtin` 10 → 11)
is fully explained by the `OC_BIN` constant and is a *restoration* of the built-in term,
not a new drift. **One new, real consequence** (F-1): the moved constant makes the
producer's reading (11) disagree with the independent oracle's (10) on that row, which
falsifies the still-live prediction at `corpus/knowledge/harness-independent-round37.md:464-465`
and should be carried as a round-48 debt (re-open the row, or teach the independent
instrument the built-in marker). F-2 (ledger prose omits the 10 → 11 move) and F-3/F-4
(low) are noted for calibration and hygiene.
