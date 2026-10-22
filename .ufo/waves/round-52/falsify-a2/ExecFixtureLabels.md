# ExecFixtureLabels — round-52 attempt-2 falsify wave: label the three unlabelled non-dump fixture lines

Result: HOLDS — the three routed lines (9, 15, 33) are the only fixture lines that are not verbatim
omp-18.12.6 dump bytes, and labelling them as not-dump bytes leaves every consumer unchanged: the
`verify_surfaces.py --self-test` tally stays 129 assertions / 0 failures (floor 129), the frozen
counter stays `callee-rename robust 4 of 4 fixtures` (also with `--seed 7` and `--seed 1234`), the
extraction result is byte-identical old vs new (8 pairs, same constant table, same module scopes, same
per-call scope tables and parameter-shadow flags), and the diff applies cleanly on top of the lane's
current in-flight working tree.

Scope: one file, `verifiers/fixtures/surfaces/strings-omp-18.12.6.txt`. No lane file was edited; the
lane's copy of the fixture still hashes `53aef789…` (verified below). The lane working tree carries
uncommitted edits from other seats (`PROVINCE.md`, `SCORECARD.md`, `SKILL.md`, `corpus/QUALITY.md`,
`corpus/README.md`, `corpus/SOURCES.md`, `corpus/knowledge/mcp-server-instructions-round52.md`,
`corpus/lessons/round-52.md`, `verifiers/check_correction_sweep.py`, `verifiers/verify_surfaces.py`);
those are other seats' work and were left alone. The L1 applies the diff.

## 1. Which fixture lines are verbatim dump bytes (fresh dump, 18.12.6)

Fresh dump taken from the installed binary, not from a cached artifact.

```
$ omp --version
omp/18.12.6                                     # exit 0
$ sha256sum /home/vgpnk/.local/bin/omp
85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4  /home/vgpnk/.local/bin/omp
$ strings -n 4 /home/vgpnk/.local/bin/omp > scratch/omp-18.12.6.strings.txt   # exit 0
2444467 lines; sha256 953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f
$ strings --version | head -1
GNU strings (GNU Binutils) 2.47
```

The binary hash equals the pin in `verifiers/baseline.json` (`omp_round51_note`), so the dump is the
one the lane pins. A Python set test over all 43 fixture lines (old file) gave the exact split:

| fixture line (old) | text | in fresh dump? |
|---|---|---|
| 1–8, 10–14, 16–32 | the 30 dump-backed lines | YES, verbatim, exact whole-line match |
| 9 | `}` | **NO** |
| 15 | `}` | **NO** |
| 33 | `// packages/coding-agent/src/session/session-summary.ts` | **NO** |
| 34, 35 | the two existing synthetic-label comment lines | NO (already labelled) |
| 36 | `var S$ = "later";` | NO (already labelled by 34) |

Two independent reasons, both measured:

* A bare `}` can never be a `strings -n 4` line. The dump has **0** lines shorter than 4 characters
  (excluding the trailing empty split artifact) and **0** lines equal to `}` (also 0 after `rstrip`).
  GNU strings drops a 1-byte run; `}` alone is 1 byte.
* `session-summary` occurs **0** times in 2,444,467 dump lines. The live dump's session modules are a
  different set (42 `// packages/coding-agent/src/session/*` markers, e.g. `session-entries.ts`,
  `session-loader.ts`, `session-storage.ts`); no `session-summary.ts` exists.

`S$` ordering still matches the live dump and is untouched by this change: `var S$ = "title";` at
dump line 843423, `var S$ = "claude-md";` at 895604, `return bq(u, S$, "CLAUDE.md");` at 895607 — the
same relative order as fixture lines 2, 11, 14.

## 2. The edit

Each of the three routed lines is now preceded by a `//` label in the same style as the existing
synthetic label at old lines 34–35. The label is a plain `//` comment; the extractor never reads it
(proof in §4). The two `}` labels and the marker label are placed so the labelled line is the line
immediately following its label block, matching the existing convention where the label at 34/35
precedes the synthetic `var S$ = "later";` at 36.

The labelled lines themselves are byte-unchanged: the `}` lines stay `}` and the marker stays
`// packages/coding-agent/src/session/session-summary.ts`. The marker must keep its exact text because
`MODULE_MARKER_RE` (`^//[ \t]*\S+\.(?:[cm]?[jt]sx?)[ \t]*$`) keys on it — it is the module scope opener
that holds the synthetic `S$` rebind, which is what the "last binding wins" decoy needs.

### Full unified diff (`git diff`, 7 insertions, 0 deletions, 1 file)

```
diff --git a/verifiers/fixtures/surfaces/strings-omp-18.12.6.txt b/verifiers/fixtures/surfaces/strings-omp-18.12.6.txt
index 88b343d..f0d4a7a 100644
--- a/verifiers/fixtures/surfaces/strings-omp-18.12.6.txt
+++ b/verifiers/fixtures/surfaces/strings-omp-18.12.6.txt
@@ -6,12 +6,16 @@ var v$ = "agents-md";
 var _7 = "AGENTS.md";
 async function zBt(u) {
   return bq(u, v$, "AGENTS.md");
+// synthetic line (not in the live dump): a lone "}" closing the loader body
+// above; strings -n 4 emits runs of 4+ printable bytes, never a bare brace
 }
 // packages/coding-agent/src/discovery/claude-md.ts
 var S$ = "claude-md";
 var I7 = "CLAUDE.md";
 async function XBt(u) {
   return bq(u, S$, "CLAUDE.md");
+// synthetic line (not in the live dump): a lone "}" closing the loader body
+// above; strings -n 4 emits runs of 4+ printable bytes, never a bare brace
 }
 // packages/coding-agent/src/discovery/gemini.ts
   const T = Kl(u, "gemini", "GEMINI.md");
@@ -30,6 +34,9 @@ var Cm = "windsurf";
     Ho(u, "windsurf", "mcp_config.json")
   const T = Kl(u, "windsurf", "memories/global_rules.md");
   const M = Ho(u, "windsurf", "rules");
+// synthetic line (not in the live dump): the module marker below has no
+// counterpart in the 18.12.6 dump -- "session-summary" occurs 0 times in it;
+// the marker only opens the scope that holds the synthetic S$ rebind below
 // packages/coding-agent/src/session/session-summary.ts
 // synthetic line (not in the live dump): a LATER rebind of S$, so a
 // "last binding wins" rule cannot pass this fixture either
```

Sandbox commit: `bea07f89a2a96381bcb36a9943cdf52b34bee0fb` (sandbox only, never pushed). Edited
fixture sha256 `b3c6f551090e73370fe58e586ff624ab66aa216e310a3450a5db3fabb71b1245`, 2000 bytes, 43
lines, LF-terminated, 0 CR, 0 NUL, 0 non-ASCII.

### Every non-dump line is now labelled

A checker walked the 43 edited lines against the fresh dump and required each non-dump line either to
*be* a label line or to sit inside a contiguous comment block containing a label line:

```
UNLABELLED non-dump lines: []
dump-backed lines: 30
label lines: 4
labelled-but-in-dump (should be 0): []
```

The 13 non-dump lines are now: 4 label lines, 2 label lines for the `}`s, 3 label lines for the marker,
the marker itself, the two pre-existing label lines, and `var S$ = "later";` — each covered.

## 3. Gates (all run in the sandbox clone)

### 3.1 The self-test (must stay 129 / 0 failures)

```
$ python3 -B verifiers/verify_surfaces.py --self-test      # sandbox at bea07f8
ERROR omp strings dump not found: .../NO-SUCH.txt
ERROR inventory file not found: .../NO-SUCH.md
ERROR baseline not found: .../NO-SUCH.json
0 failure(s) over 129 assertions
EXIT=0
```

Those three ERROR lines are the script's own deliberate missing-file probes (they also appear on the
unmodified base — same three, same 129, exit 0). The tally is unchanged at 129, floor 129.

The self-test genuinely reads the edited file — proven by mutation, not asserted: I copied the sandbox,
changed `var S$ = "claude-md";` to `var S$ = "claude-md-MUTANT";` in the edited fixture, and the
self-test went red on the fixture-reading arms:

```
$ python3 -B verifiers/verify_surfaces.py --self-test     # mutated copy
self-test FAIL: fx-renamed-var: PASS literal_present: got 'FAIL surfaces.literal_present: ...
self-test FAIL: ambiguous-rebind: S$ surfaces unresolved: got [... ('claude-md-MUTANT', 'CLAUDE.md') ...]
10 failure(s) over 129 assertions
EXIT=1
```

So the green at 129 on the edited fixture is earned by the edited bytes, not by the self-test ignoring
the file.

### 3.2 The frozen counter (must stay 4 of 4)

```
$ python3 -B verifiers/check_callee_rename.py --rev bea07f89a2a96381bcb36a9943cdf52b34bee0fb
strings-omp-clean.txt        control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'jDe': 'L6', 'Id': 'Ev'}
strings-omp-newcallees.txt   control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'Dl': 'L6', 'I5': 'Ev', 'Co': 'U4', 'Gl': 'Wk', 'Mo': 'Gn'}
strings-omp-18.12.5.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'lq': 'L6', 'Xl': 'Ev', 'Fo': 'U4'}
strings-omp-18.12.6.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'bq': 'L6', 'Kl': 'Ev', 'Ho': 'U4'}
callee-rename robust 4 of 4 fixtures
EXIT=0
```

Seed variants: `--seed 7` → `callee-rename robust 4 of 4 fixtures`, exit 0. `--seed 1234` → same,
exit 0. `--root <sandbox>` → `4 of 4`, exit 0.

**Counter caveat, stated because it is load-bearing for the L1's reading of this number:**
`check_callee_rename.py` reads its **fixtures from `FIXTURE_REV = c8579a4c…`**, not from `--rev`
(`verifiers/check_callee_rename.py:61`, `:158` — `git_show(FIXTURE_REV, …)`; only the *gate script*
comes from `--rev`, `:141`). So this counter measures the gate, not the fixture bytes, and its `4 of 4`
is unchanged by construction whether or not the fixture is edited. The evidence that the *edited*
fixture is still accepted by the gate is §3.3 and §4, not this counter.

### 3.3 The gate run directly against the edited fixture

```
$ python3 -B verifiers/verify_surfaces.py --repo verifiers/fixtures/surfaces \
    --omp-strings verifiers/fixtures/surfaces/strings-omp-18.12.6.txt \
    --opencode-strings verifiers/fixtures/surfaces/strings-opencode-clean.txt \
    --baseline verifiers/fixtures/surfaces/baseline-18.12.5.json \
    --inventory verifiers/fixtures/surfaces/inventory-clean.md \
    --check surfaces.literal_present --check surfaces.no_uncovered_class
PASS surfaces.literal_present: 8 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
EXIT=0
```

### 3.4 Other gates and no-harm checks

| command | result | exit |
|---|---|---|
| `python3 -B verifiers/check_assertion_floors.py` | 12 PASS, incl. `PASS surfaces observed=129 floor=129` | 0 |
| `python3 -B verifiers/check_correction_sweep.py --rev bea07f8…` | `correction sweep: 0 stale block(s)` | 0 |
| `python3 -B verifiers/check_correction_sweep.py --self-test` | `0 failure(s) over 5 assertions` | 0 |
| `python3 -B verifiers/check_mcp_instructions.py --rev bea07f8…` | `mcp instructions backed 5 of 7 clients` | 0 |
| `python3 -B verifiers/check_overlap_levers.py --rev bea07f8…` | `overlap levers backed 7 of 7 clients` | 0 |
| `python3 -B verifiers/verify_corpus_independent.py --self-test` | `self-test: 91 assertions, 0 failures` | 0 |
| `python3 -B verifiers/verify_surfaces.py --json` (live gate, installed omp 18.12.6) | pass 6 / fail 1 | 1 |

The live gate's single failure is `surfaces.opencode_extract`, and it is **pre-existing and unrelated
to this edit**: the same clone at the unmodified base `c8407a4…` gives the identical pass 6 / fail 1
with the same failing check. Its cause is host drift in the *opencode* binary
(`opencode_binary_sha256` expect `179ca421…` vs got `538fcb1b…`, `check_substrate_pins.py` →
`DRIFT 1/3 pins failed`), also reproduced identically at the base commit. The omp side of both is
green at base and after: `PASS omp_binary_sha256`, `PASS omp_binary_mtime delta 0 ns`, and
`surfaces.literal_present` / `surfaces.no_uncovered_class` PASS.

## 4. Why the labels are invisible to the extractor

Extracted and compared old vs new fixture text with the gate's own functions imported from
`verifiers/verify_surfaces.py` (Python, exit 0):

| property | old | new |
|---|---|---|
| extracted (group, file) pairs | 8 | 8 (identical set) |
| module scopes (`module_scopes`) | 9 | 9 |
| module markers (`MODULE_MARKER_RE`) | 8 | 8 |
| dump-wide `constant_table` | `{jO, v$, _7, I7, Cm}` | identical dict |
| `ASSIGN_RE` hits | 8 bindings | identical 8 bindings |
| `OMP_GENERIC_CALL_RE` callees | 11 | identical 11 |
| `PARAM_HEADER_RE` hits | `async function zBt(u)`, `async function XBt(u)` | identical |
| per-call scope table + parameter-shadow flag | 11 calls | identical for all 11 |

The label text cannot collide with the extractor's regexes:

* `MODULE_MARKER_RE` requires the whole line to be `// <path>.<ext>`. The label lines end in
  `loader body`, `bare brace`, `has no`, `in it;`, `below` — none ends in `.ts`/`.js`/`.jsx`, so none
  opens a new module scope. Marker count stays 8.
* `ASSIGN_RE` needs `name = "literal"`. No label line contains `= "`. Binding set unchanged.
* `OMP_GENERIC_CALL_RE` needs `callee(arg, "group", "file.md")`. No label line contains `.md` in a
  call shape. Callee list unchanged.
* `PARAM_HEADER_RE` needs `function name(...)` or an arrow. No label line contains `function` followed
  by `(`. Header list unchanged.

`param_shadowed` is the sharpest consumer (it makes a `S$` that is a function parameter stay
unresolved), and it is unchanged for every call site, so the round-52 (b2i) parameter-shadow arm and
the round-51 (b2g) ambiguous-rebind arm still behave exactly as before.

## 5. Diff applies cleanly — including on top of the lane's in-flight edits

```
$ git -C <pristine clone at c8407a4> apply --check --verbose <diff>
Checking patch verifiers/fixtures/surfaces/strings-omp-18.12.6.txt...
APPLY_CHECK_EXIT=0
$ git -C <pristine clone> apply <diff>            # APPLY_EXIT=0
$ sha256sum <pristine>/…/strings-omp-18.12.6.txt <sandbox>/…/strings-omp-18.12.6.txt
b3c6f551090e73370fe58e586ff624ab66aa216e310a3450a5db3fabb71b1245  (both identical)
```

Rehearsal of the exact L1 action — copy the lane's current working tree (including every other seat's
uncommitted edit), apply the diff, run the gates:

```
$ git apply <diff>                                 # APPLY_EXIT=0
b3c6f551090e73370fe58e586ff624ab66aa216e310a3450a5db3fabb71b1245  verifiers/fixtures/surfaces/strings-omp-18.12.6.txt
$ python3 -B verifiers/verify_surfaces.py --self-test
0 failure(s) over 129 assertions                    # EXIT=0
$ python3 -B verifiers/check_callee_rename.py --root <rehearsal>
callee-rename robust 4 of 4 fixtures               # EXIT=0
$ python3 -B verifiers/check_correction_sweep.py --root <rehearsal>
correction sweep: 0 stale block(s)                 # EXIT=0
```

Note the diff is written with `a/`/`b/` prefixes (`git -c diff.mnemonicPrefix=false diff …`). The
host has `diff.mnemonicprefix=true` in `~/.config/git/config`, so a bare `git diff` prints `i/`/`w/`
prefixes; that form does not apply with `git apply`. The `a/`/`b/` form in §2 is the one to use.

## 6. Lane untouched

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && sha256sum verifiers/fixtures/surfaces/strings-omp-18.12.6.txt
53aef7894142e0cab63e8ef2bba98408129929e3ad19dcdb11dff94facff7d92   # unchanged
$ git rev-parse HEAD
c8407a453788df964df5a7b835dd0ce1360de882
```

No git write command was run in the lane (no add/commit/stash/checkout/reset/pull/push/worktree), no
jj command was run, no lane file was edited. All work happened in
`/fast/scratch/hyaku/kotoba-r52a2/ExecFixtureLabels` (plus throwaway clones `pristine`, `mut`,
`lane-rehearsal` under the same seat directory). The only file written is this report.

Tools installed or upgraded: none.

## 7. Residual risk and gaps

* **The counter cannot see this fixture.** `check_callee_rename.py` reads fixtures from
  `FIXTURE_REV = c8579a4c…` (`verifiers/check_callee_rename.py:61`, `:158`); only the gate script
  comes from `--rev`. Its `4 of 4` therefore certifies the gate, not the edited fixture. The fixture's
  own acceptance rests on §3.1 (self-test 129/0, mutation-proven to read the file) and §3.3 (gate CLI
  green on the edited fixture). [INFERENCE] The plan's C1 statement is unaffected by this change
  because the counter never read the edited bytes in the first place.
* **No gate enforces the labelling.** The labelling is a documentation fix; nothing in `verifiers/`
  checks a fixture line against a dump (the round-51 finding already noted this). A future edit could
  reintroduce an unlabelled non-dump line without turning any gate red. The round-51 recommendation to
  add such a gate (fixture line == exact line of `strings -n 4` of the pinned binary, reporting SKIP
  when the binary is absent) is still open and out of my scope — I did not add it.
* **Two open items from the same round-51 finding are not addressed here**, and are the L1's to
  decide: (a) the fixture still carries no provenance header (dump sha `953b19df…`, binary sha
  `85d9daf3…`) and no omission markers — it is still an in-order *excerpt* that reads as a contiguous
  block, and 14 of the 27 dump-backed line pairs are not adjacent in the live dump; (b) the decoy's
  expected value still rests on the unproven module-scope premise (the source-path comment is a proxy
  for a variable scope). My labels do not claim the marker is real — the marker label says outright
  that it has no counterpart in the dump — but the scope premise itself is unchanged.
* **Line numbers cited elsewhere now point elsewhere.** `corpus/lessons/round-51.md:174-177`,
  `corpus/lessons/round-51-verifier-spotcheck.md:50-52`, `plans/round-52.md:72-73` and
  `.ufo/waves/round-51/falsify/FixtureFaithful.md` refer to the *pre-label* line numbering (9, 15, 33
  of 36 lines). After this change the file is 43 lines and the routed lines are 11, 19 and 40. Those
  are historical records of the round-51 finding and of the plan; I did not edit them (the L1 owns
  those files, and the round-51 lesson and the round-51 falsify report are dated records of what was
  true then). Flagging so the L1 can decide whether the round-52 lesson should record the new
  numbering.
* **`surfaces.opencode_extract` is red and `check_substrate_pins.py` reports `DRIFT 1/3`** on this
  host — both pre-existing at `c8407a4…` and both caused by the opencode binary's sha256 drifting
  from the pin. Not caused by, and not fixable from, this fixture edit.
