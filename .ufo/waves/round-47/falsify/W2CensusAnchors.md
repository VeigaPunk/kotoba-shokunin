verdict: PARTIAL — every backticked span in § B′ evidence cells and every ledger count in the round-47 class ledger reproduces exactly on the frozen opencode-1.19.3 dump, and all cited dump line numbers are correct; but one ledger cell states a count for a non-literal anchor ("priority array") that the ledger's own documented count command cannot reproduce, and 11 of the 18 round-14 anchor families the § B′ prose claims are "present" with "counts: the round-47 ledger" are absent from that ledger.

---

# W2CensusAnchors — falsification of `corpus/knowledge/instruction-surface-census-round13.md` § B′ + the round-47 class ledger

Lane: `KotobaR47-2.W2CensusAnchors-2` (leaf; no subagents).
Target commit: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` ("round-47: C1 re-derive+re-pin omp 18.12.5/opencode 1.19.3; C2 trigger.no_xml_tag; C3 governance erratum + corpus index; frontier S012-S015, M20-M22, Q19; wave-1 evidence").
Scratch clone: `/fast/scratch/kotoba-r47/w2/W2CensusAnchors/kotoba-shokunin` (detached at 7ad7fad). Production tree untouched.
Frozen substrate read-only: `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` (sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`), `bin/opencode-1.19.3` (sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`).

## Artifacts

- `W2CensusAnchors.check_anchors.py` — first-pass span/line harness (superseded; kept for the raw counts it prints).
- `W2CensusAnchors.check_anchors2.py` — refined harness (evidence-cell vs ledger separation, true line numbers).
- `W2CensusAnchors.w2_census_anchors.py` — **final harness**; checks A (evidence-cell spans present), B (ledger spans present with the stated count), C (§ B′ prose-declared counts exact), D (cited dump line carries the cited span), E (true line of each anchor), F (dump provenance: `strings -n 4` of the frozen binary == frozen dump), G (the ledger's own documented count command reproduces every stated count). Output: `W2CensusAnchors.w2_census_anchors.out`.
- `W2CensusAnchors.w2_ledger_power.py` — **ledger anchor discriminating-power analysis** (per-anchor subsystem attribution; "could this anchor decide its own verdict?"). Output: `W2CensusAnchors.w2_ledger_power.out`.

## Commands run (all exit codes as shown)

```
cd /fast/scratch/kotoba-r47/w2/W2CensusAnchors/kotoba-shokunin
git checkout -q --detach 7ad7fadfc09354b74fb66605dfb0c1182c115a2f      # exit 0
python3 verifiers/verify_surfaces.py                                    # exit 0, 7 PASS, 0 FAIL
python3 verifiers/check_substrate_pins.py                               # exit 0, "OK 3/3 pins hold"
python3 w2_census_anchors.py census.md /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
                                                                     # exit 1 (1 hard failure + 0 line-cite defects)
python3 w2_ledger_power.py census.md /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings   # exit 0
strings -n 4 /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3 | cmp - opencode-1.19.3.strings # exit 0 (byte-identical)
sha256sum -c /fast/scratch/kotoba-r47/shared/SHA256SUMS                # exit 0, 4/4 OK
```

## Section map at 7ad7fad (for every citation below)

| path:line | content |
|---|---|
| `corpus/knowledge/instruction-surface-census-round13.md:212` | `### B′. opencode — instruction model (re-derived 2026-10-21 for 1.19.3, round 47)` |
| `…:249`–`:257` | the 9 § B′ class rows (evidence cell = 5th column) |
| `…:305` | `**Class ledger (round 47; every id the census ever declared for opencode).** Count command: …` |
| `…:310`–`:321` | the 12 ledger rows |
| `…:287` | `## Superseded class rows and the round-47 opencode ledger (not inventory)` |
| `…:358` | `## Honest ceiling — what this census cannot decide` |
| `verifiers/verify_surfaces.py:366`–`:430` | the OC-1..OC-6 rule block (anchors + comments) |

---

# Findings

## F1 — MEDIUM (calibration). The ledger's `opencode:instructions/AGENTS.md` row states a count for an anchor that is not a literal, and the ledger's own documented count command returns 0, not the stated 1.

`corpus/knowledge/instruction-surface-census-round13.md:315`

```
| `opencode:instructions/AGENTS.md` | historical (round 18) | resurrected | priority array 1 |
```

The ledger header at `…:305`–`:307` documents the count method as a literal-substring count:

```
Count command: `python3 -c 'import sys;d=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings '<anchor>'`
```

Repro (exit 0, prints `0`):

```
$ python3 -c 'import sys;d=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))' \
    /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings 'priority array'
0
```

`grep -c "priority array" /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` → `0`. The string `priority array` is **prose describing a code construct, not a substring of the dump**. The intended literal is `y=["AGENTS.md",` (count 1, dump:443993) — that is what § B′ row `…:249` cites, and it is what the round-47 ledger row should have said.

This is the **only** ledger row whose stated count the documented command cannot reproduce. The other 11 rows all round-trip exactly (harness check G: 15/15 anchors, all `OK`).

Why it matters: this ledger is the round's C1 calibration artifact. `corpus/lessons/round-47.md:56`–`:58` points the C1 claim at exactly this section ("every opencode id the census ever declared, with its verdict and the dump count that decides it"). A reader who runs the documented command on the row as written gets `0` for a verdict cell that says `1` — a silently wrong number in the artifact that is supposed to make the count checkable.

**Not** a mechanism error: the *verdict* (`resurrected`) is right — `y=["AGENTS.md",` is present once on dump:443993 and the priority list is live (see F4).

## F2 — MEDIUM (calibration). 11 of the 18 round-14 anchor families the § B′ prose cites as "present" are absent from the round-47 ledger the prose points to for their counts.

`corpus/knowledge/instruction-surface-census-round13.md:224`

```
and every round-14 anchor is present (counts: the round-47 ledger after § D).
```

The parenthetical points at the ledger at `…:305`–`:321` as where the **counts** live. Measured against the 18 round-14 anchor families enumerated in `corpus/knowledge/opencode-extraction-round14.md:41`–`:47` (the round-14 rule table), the ledger cites 7 of 18:

| round-14 anchor family | in the ledger? |
|---|---|
| `["AGENTS.md"` | **absent** |
| `disableClaudeCodePrompt?["CLAUDE.md"]` | **absent** |
| `"CONTEXT.md"]` | **absent** |
| `X.join(r.config,"AGENTS.md")` | cited (`:311`) |
| `X.join(r.home,".claude","CLAUDE.md")` | cited (`:318`) |
| `for(let O of T.instructions)` | cited (`:314`) |
| `q.startsWith("https://")` | **absent** |
| `q.startsWith("http://")` | **absent** |
| `Instructions from: ` | cited (`:319`) |
| `fn("Instruction.resolve")` | cited (`:320`) |
| `<system-reminder>` | **absent** |
| `OPENCODE_DISABLE_PROJECT_CONFIG` | **absent** |
| `globUp(T,d.directory,d.worktree)` | **absent** |
| `globUp(T,r.config,r.config)` | **absent** |
| `InstructionContext.observe` | cited (`:321`) |
| `Key.make("core/instructions")` | **absent** |
| `targets:["AGENTS.md"]` | **absent** |
| `system-context-builtins` | cited (`:321`) |

**11 of 18 absent** (8 counted above plus `q.startsWith("http://")`, `Key.make("core/instructions")`, `targets:["AGENTS.md"]`).

The *substance* of the claim is TRUE and I verified it independently: **all 18 round-14 anchor families are present on the 1.19.3 dump** (harness check: 18/18 `OK`, 0 absent — including `globUp(T,d.directory,d.worktree)` count 1, `globUp(T,r.config,r.config)` count 1, `Key.make("core/instructions")` count 1, `targets:["AGENTS.md"]` count 1, `<system-reminder>` count 18, `OPENCODE_DISABLE_PROJECT_CONFIG` count 9). So the claim itself holds; the **pointer** to where the counts are is wrong. The count for e.g. `globUp(T,r.config,r.config)` (= 1) exists nowhere in the ledger, so the pointer sends the reader to a section that does not contain what it promises.

Minimal fix (not mine to make): either widen the ledger to carry all 18 round-14 anchor counts, or change `…:224` to name where the counts actually are (the round-14 evidence file `corpus/knowledge/opencode-extraction-round14.md:41`–`:47` plus the § B′ evidence cells, which do cite 5 of the missing families at `…:250`, `:251`, `:255`, `:256`, `:257`).

## F3 — LOW (calibration). The § B′ prose's "Every v2.0.26 anchor is absent" over-reads: 4 of the 12 anchors of the retired v2.0.26 rule set are present on the 1.19.3 dump.

`corpus/knowledge/instruction-surface-census-round13.md:221`–`:224`

```
**Lineage finding.** Every v2.0.26 anchor is absent from the 1.19.3 dump
(`ConfigInstructionPlugin` 0, `ReadTool.Plugin` 0, `SessionInstructions` 0,
`session.instructions.entry.put` 0, `j5(r.config,"AGENTS.md")` 0, `InstructionDiscovery` 0),
```

The six anchors *enumerated in the parenthesis* are all exactly 0 — verified (harness check C: 6/6 `OK`). But "**Every** v2.0.26 anchor" is a universal claim over the retired rule set, and the retired set (base `verifiers/verify_surfaces.py` at `c61a973`, OC-1..OC-6) had 12 anchors. Four of them are present on 1.19.3:

| retired v2.0.26 anchor | count on 1.19.3 dump |
|---|---|
| `targets:["AGENTS.md"]` (base OC-1 `OC_PROJECT_TARGETS`) | **1** |
| `ambient instructions` (base OC-3 `OC_AMBIENT_SCHEMA`) | **2** |
| `OPENCODE_DISABLE_PROJECT_CONFIG` (base OC-5) | **9** |
| `/instructions/entries` (base OC-6 `OC_API_ROUTE`) | **3** |

`/instructions/entries` is the sharpest case: the census itself says at `…:243` that it "survives only in the generated client SDK" — i.e. the same section simultaneously says "every v2.0.26 anchor is absent" and "one of them survives". (The 3 hits are all in the client-SDK chunk at dump:606940, `instructions:{entry:{list:…}}` — no server route, consistent with the census's own reading.)

The fix is a wording fix, not a data fix: the sentence should read "Every *v2.0.26-specific* anchor is absent" or enumerate the 12. As written, a reader auditing the base rule set finds 4 contradicting hits. Note this is a **carried-forward** framing, not a round-47 regression: the same "every v2.0.26 anchor" phrasing is at `verifiers/verify_surfaces.py:355`–`:360`.

## F4 — LOW (calibration, carried). The § B′ row for `opencode:instructions/AGENTS.md` attributes the priority-list resolution to `globUp`, but the dump shows the priority array is walked with `findUp`.

`corpus/knowledge/instruction-surface-census-round13.md:249`

```
| `opencode:instructions/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | `y=["AGENTS.md",` first priority-list element; first-match per directory via `globUp(T,d.directory,d.worktree)` (OC-1, OC-5; dump 443993) |
```

The span `globUp(T,d.directory,d.worktree)` does exist (count 1, dump:443993) — so the anchor check passes. But the *mechanism* is misattributed. Dump:443993, `Instruction.systemPaths`:

```
if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)for(let O of y){let U=yield*e.findUp(O,d.directory,d.worktree).pipe(...);if(U.length>0){U.forEach((q)=>w.add(X.resolve(q)));break}}
```

The priority array `y` is walked with **`e.findUp(O,d.directory,d.worktree)`**, not `globUp`. The `globUp(T,d.directory,d.worktree)` / `globUp(T,r.config,r.config)` pair on the same line belongs to a *different* helper — the `fnUntraced` resolver `m` used for the `T.instructions` declared-list path branch (dump:443993 @7161, called as `m(U)` @8325) — i.e. it is OC-5's project-vs-config switch for the **declared instructions list**, not the priority list.

Corroboration that `findUp` is the priority-list mechanism: `findUp` is the *exact-filename* walker (`FileSystem.findUp`, dump:447206: `yw=B.fn("FileSystem.findUp")(function*(Q,U,Y){let g=[],L=U;while(!0){let jx=yy(L,Q);if(yield*A.exists(jx))g.push(jx);…` — it joins one literal name per directory and collects every ancestor hit, hence "first-match per directory" holds for `findUp`, and `globUp` is the *glob-pattern* walker (`ww=B.fn("FileSystem.globUp")`, `…$y(Q,{cwd:L,absolute:!0,include:"file",dot:!0})`).

Note this wording is **inherited, not new in round 47**: the round-14 census at `29c17be` line 174 said the same `globUp("AGENTS.md",cwd,worktree)` shape, and `c61a973` (BASE) has no § B′. The round-47 § B′ row is a re-derivation that re-asserted the inherited anchor without re-reading which walker the priority list actually uses.

Impact is bounded: the census's *class identity* claim (AGENTS.md is the first priority-list element, gated) is correct and independently confirmed; only the named resolver is wrong, and it is named in the *evidence* column, which the census's own § Honest ceiling (`:403`) already declares has no machine counterpart. So this is a prose defect a reader can catch, not a gate escape.

## F5 — LOW (operability). The ledger's `Instructions from: ` anchor is shared by 4 subsystems and its count (4) does not decide the `opencode:config/instructions-remote` verdict on its own.

`corpus/knowledge/instruction-surface-census-round13.md:319` (and § B′ row `:255`)

`Instructions from: ` occurs 4 times, and the 4 hits sit in **four different renderers**:

| dump line | renderer |
|---|---|
| 443993 | `Instruction.system` — the local `d` (systemPaths) render, `O[R]?[\`Instructions from: ${q}` |
| 443994 | `Instruction.system` — the remote `w` (declared-URL) render, `U[R]?[\`Instructions from: ${q}` |
| 443995 | `Instruction.resolve` — the read-hook's per-file content push |
| 445482 | `InstructionContext.observe` — the second subsystem's `XP` render |

So the count `4` is correct but **not discriminating**: deleting the remote half (the only thing `opencode:config/instructions-remote` is about) would leave 3. The census's own § B′ row `:255` gets this right by also citing the discriminating pair — `(T.instructions??[]).filter((q)=>q.startsWith("https://")||q.startsWith("http://"))` (count 1) and `{concurrency:4}` (count 1) — which *are* unique to the remote branch (verified: the `filter(` shape has exactly 1 hit; `{concurrency:4}` exactly 1; the `startsWith("https://")` inside the `.filter(` has exactly 1 hit on 1.19.3, versus 24 for the bare `startsWith("https://")`).

Same shape on row `:316` (`disableClaudeCodePrompt` count 3): 2 hits are the `y`/`n` array gates at dump:443993 and 1 is the RuntimeFlags definition at dump:447067 — the count is right but the third hit is a different subsystem (the env→flag map), so the count is not purely the class's own signal.

The census's own § B′ prose at `:226`–`:228` already names this failure mode for OC-4 ("`<system-reminder>` alone is a generic token (18 hits)") and fixes it by adding the `ReadTool.execute` caller anchor. The same treatment was applied to OC-3b's *pattern* but not to its *render* anchor, and the ledger row was not tightened alongside. Low severity because the machine check (`OC-3b`) already requires both the `.filter(` pattern and the render token, so the verdict is not decided by the render count alone.

---

# What survived the attack (recorded, not padded)

These are the claims I set out to break and could not.

**S1 — every backticked span in a § B′ evidence cell is present on the dump.** All 9 rows, 24 spans, 24/24 present (harness A). Highlights: `y=["AGENTS.md",` (1), `...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]` (1), `"CONTEXT.md"]` (1), `n=[X.join(r.config,"AGENTS.md")` (1), `X.join(r.home,".claude","CLAUDE.md")` (1), `for(let O of T.instructions)` (1), the full `.filter((q)=>q.startsWith("https://")||q.startsWith("http://"))` (1), `{concurrency:4}` (1), `fn("Instruction.resolve")` (1), `fn("ReadTool.execute")` (1), `InstructionContext.observe` (1), `targets:["AGENTS.md"]` (1), `jX(L.config,"AGENTS.md")` (1), `Key.make("core/instructions")` (1), `system-context-builtins` (1).

**S2 — every ledger count is exact.** 11 of 12 rows: all 15 backticked anchors reproduce their stated count under the ledger's own documented command (harness G: 15/15 `OK`). Including the retirement rows: `ConfigInstructionPlugin.projectSource` 0, `ReadTool.Plugin` 0, `SessionInstructions.load` 0, `session.instructions.entry.put` 0, `instructions:{entry:{list:` 1, `j5(r.config,…)` 0 (the ellipsis form is a deliberate non-literal and the count 0 is right for it). And the *retirement* verdicts are substantiated: `instructions:{entry:{list:` is at dump:606940 inside the generated client SDK and all 3 `/instructions/entries` hits are there, with `session.instructions` occurring 0 times anywhere — the census's "no server route" reading at `:243`–`:244` is correct.

**S3 — every cited dump line number is correct.** All 4 single-line cites and the 1 range cite carry the span they claim, and each span's *true* line is the cited line (harness D/E, 0 defects): 443993 → `y=["AGENTS.md",` / `n=[X.join(r.config,"AGENTS.md")` / `X.join(r.home,".claude","CLAUDE.md")` / `for(let O of T.instructions)` / `q.startsWith("https://")` / `{concurrency:4}` / `globUp(T,d.directory,d.worktree)`; 443995 → `fn("Instruction.resolve")` / `while(G.startsWith(N)&&G!==N)`; 444228 → `fn("ReadTool.execute")`; 445481–445487 → `Key.make("core/instructions")` (445481), `InstructionContext.observe` + `targets:["AGENTS.md"]` + `jX(L.config,"AGENTS.md")` (445482), `system-context-builtins` (445487). This is notable because the census's § Method (`:56`–`:60`) records that a *previous* round's `strings` line numbers were found stale — the round-47 cites are fresh and correct.

**S4 — the § B′ prose-declared counts are exact.** 9/9 (harness C): the six v2.0.26-absence counts 0, `<system-reminder>` = 18, `2.0.26` = 0, `var n="1.19.3"` = 1 (at dump:447186).

**S5 — dump provenance is sound.** `strings -n 4 /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3` is **byte-identical** to the frozen `opencode-1.19.3.strings` (`cmp` exit 0; regenerated sha256 `f4d8f34a…` == the frozen dump's sha256). `sha256sum -c SHA256SUMS` → 4/4 OK. The npm path the census names at `:214` exists and hashes to exactly the census's stated `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`, and `package.json` says `1.19.3`. So the "the bytes the `~/.local/bin/opencode` npx wrapper executes" claim at `:215`–`:216` is true *for the currently cached npx dir*; the registry's `latest` dist-tag is also `1.19.3`, and the wrapper's `--prefer-online` means a future publish can swap it under the census (recorded as residual risk, not a defect in this file).

**S6 — the round-47 substrate re-derivation is load-bearing, not laundered.** The round-14 OC-1..OC-6 rule block (`verifiers/verify_surfaces.py:366`–`:430`) matches the 1.19.3 dump on all 18 anchor families. Independently confirmed the two tightenings the census claims at `:226`–`:228`: the round-14 OC-3b regex (`\.instructions.{0,40}?startsWith\("https://"\).{0,40}?startsWith\("http://"\)`, from `29c17be`) hits **2** times on 1.19.3 (once in OC-3a's `for(let O of T.instructions)` loop, once in the real remote filter) while the tightened round-47 regex hits **1** — so the tightening is real and load-bearing. And the round-14 OC-4 anchor `<system-reminder>` really is a generic token (18 hits) while `fn("ReadTool.execute")` is unique (1 hit), so the OC-4 tightening is real too.

**S7 — the read-hook's "walks *inside* the instance directory" claim at `:238` is correct.** dump:443995: `while(G.startsWith(N)&&G!==N)` where `N=X.resolve(yield*J.directory)` (the instance dir) — the walk ascends *within* the instance dir and stops at it, i.e. it does not reach the project root. This is the v2.0.26 difference the census claims at `:236`–`:238` and it holds.

**S8 — the gates pass at 7ad7fad and the round-47 ledger is genuinely outside their scope.** `verify_surfaces.py` exit 0, 7/7 PASS (`opencode extraction 9/9 declared class(es) from 7/7 rules`). `check_substrate_pins.py` exit 0, 3/3 pins. The 12 ledger ids are all present in the census file and all 12 are ledger rows (coverage 12/12 both directions) — the ledger is complete as a *list*. And the § B′ table sits inside `## Class inventory` (lines 65–286) so `table_parity`/`literal_parity`/`kind_parity` do cover its id/literal/kind columns.

---

# Mutation test of the round-47 additions (what the gates do NOT catch)

I mutated the census in the scratch clone and re-ran `verify_surfaces.py`. **Every mutation exits 0 with 7/7 PASS** — i.e. the ledger's count column and the § B′ dump-line cites and the § B′ prose counts have **no machine gate at all**:

| # | mutation | verify_surfaces.py |
|---|---|---|
| M1 | ledger `:315` `priority array 1` → `priority array 7` | exit 0, 7 PASS |
| M2 | ledger `:316` `` `disableClaudeCodePrompt` 3 `` → ` 99` | exit 0, 7 PASS |
| M3 | § B′ `:249` `dump 443993` → `dump 999999` | exit 0, 7 PASS |
| M4 | § B′ `:256` `dump 444228` → `dump 444999` | exit 0, 7 PASS |
| M5 | ledger `:315` `priority array 1` → `priority array 99` | exit 0, 7 PASS |
| M6 | ledger `:317` `` `CONTEXT.md` 1 `` → ` 0` (id silently retired) | exit 0, 7 PASS |
| M7 | § B′ `:251` "1 occurrence of `CONTEXT.md`" → "7 occurrences" | exit 0, 7 PASS |
| M8 | § B′ prose "18 hits" → "3 hits" | exit 0, 7 PASS |

This is **consistent with the census's own design** — `verifiers/verify_surfaces.py` reads only the `## Class inventory` section (`:507`–`:526`) and the § B′/ledger material lives under `## Superseded class rows and the round-47 opencode ledger (not inventory)` (`:287`, outside the section) — but it means the *new* round-47 numeric claims are reader-checked only. The census's § Honest ceiling (`:358`–`:412`) documents the residual for the *inventory* table's `governed by`/`evidence` columns (`:403`) and does **not** name the round-47 ledger's count column or the new dump-line cites. That omission is the mechanism behind F1: the one place a wrong number can hide is the one place no ceiling names.

Repro for the F1 mutation class (the ledger's own count command catches what `verify_surfaces.py` cannot):

```
$ python3 -c 'import sys;d=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))' \
    /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings 'priority array'
0
```

---

# Residual risk / verification gaps (what I did NOT check)

1. **Runtime behavior.** Everything above is strings-level. Whether `Instruction.systemPaths`, `Instruction.resolve`, or `InstructionContext.observe` actually *fires* in a live opencode 1.19.3 session is undecided by this evidence — the census's own ceiling says so (`:350`–`:356`). I did not launch opencode, and per the lane contract I did not execute the `~/.local/bin/opencode` wrapper.
2. **The `<system-reminder>` count 18 vs 8 close-tags.** 18 opening `<system-reminder>` and 8 `</system-reminder>` — the census states 18 (the open-tag count) and my count matches, but I did not audit whether the 10 unmatched openers are template placeholders or a real imbalance.
3. **omp-side rows.** My scope was § B′ + the round-47 ledger (both opencode). I did not re-derive the § A / § A2 / § A3 omp rows, the omp `18.12.5` counts, or the omp callee allowlist.
4. **`corpus/knowledge/opencode-extraction-round14.md`.** I read its anchor table to establish the round-14 anchor set (18 families) and confirmed its 2026-10-14 erratum correctly scopes it as historical. I did not re-run its own drop-one matrix or check whether its "live: 7/7 PASS" figure is still current.
5. **`verifiers/surfaces-baseline.json` `assembled` field.** Its `$comment` says "assembled 2026-09-28T21:02" while enumerating round-47 additions; I read the opencode entries (10 in the baseline, of which 9 are live § B′ ids and 1 is the retired `api-entries`) but did not audit the 32 omp entries or the `reason` fields.
6. **The `S012`–`S015` / `Q19` / `M20`–`M22` frontier rows and `corpus/README.md` / `corpus/lessons/round-47.md` content** are other lanes' scope; I touched `corpus/lessons/round-47.md:56`–`:58` only to confirm the C1-ledger pointer, and `corpus/README.md:40`/`:76` only as context.
7. **The `waves/round-47/build` wave-1 evidence** (e.g. `C1ClassOpencode.md`, `C1OpencodeProvenance.chain.json`) — I did not re-derive their numbers; my measurement is independent of them (I read the dump directly).
8. **Non-`opencode` opencode-1.19.3 subsystems** (skills loading, MCP instructions, `<available_references>`) — the census lists these in § D as non-classes; I did not re-verify their non-class status.
9. **`OPENCODE_DISABLE_CLAUDE_CODE` / `_PROMPT` env→flag wiring.** dump:447067 shows `disableClaudeCodePrompt:h.all({broad:k("OPENCODE_DISABLE_CLAUDE_CODE"),direct:k("OPENCODE_DISABLE_CLAUDE_CODE_PROMPT")})` — the census's `disableClaudeCodePrompt` gate reading is consistent, but I did not trace whether `t.disableClaudeCodePrompt` (the config service) and the RuntimeFlags value are the same field at runtime.
10. **The npm `latest` dist-tag is `1.19.3` today**, so the census's substrate claim holds now; a future publish moves it (wrapper uses `--prefer-online`). I did not pin the registry state.

---

# Bottom line

The **load-bearing numeric claims of § B′ and the round-47 ledger are correct on the frozen substrate**: 24/24 evidence-cell spans present, 15/15 ledger anchors exact under the ledger's own count command, 9/9 prose counts exact, 15/15 cited dump line numbers correct with the spans at exactly those lines, dump provenance byte-identical to `strings -n 4` of the pinned binary, and the round-14 OC-1..OC-6 anchor set fully present with both round-47 tightenings independently confirmed load-bearing.

Three calibration defects and one carried prose defect stand:

- **F1** `…:315` — the ledger states count `1` for a non-literal anchor the documented count command scores `0`. One-character-class fix: replace `priority array` with `y=["AGENTS.md",`.
- **F2** `…:224` — the "counts: the round-47 ledger" pointer is wrong for 11 of 18 round-14 anchor families.
- **F3** `…:221`–`:222` — "Every v2.0.26 anchor is absent" is contradicted by 4 surviving anchors, one of them (`/instructions/entries`) acknowledged 21 lines later in the same section.
- **F4** `…:249` — the priority list is walked by `findUp`, not `globUp` (carried from round 14).

And the structural finding: the new ledger's count column and the new dump-line cites have **no machine gate** (M1–M8 all exit 0), and the § Honest ceiling does not name them — which is precisely why F1 is invisible to `verify_surfaces.py`.
