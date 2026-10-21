verdict: BROKEN — OC-1 (verify_surfaces.py:370-372, 447-455) kills corrupt/drop of its `["AGENTS.md"`/`"CONTEXT.md"` anchors and derives planted names correctly, but its second declared anchor `disableClaudeCodePrompt` is dead logic (the `gated` guard at :450 is a tautology) and first-match `search()` lets a decoy array shadow real drift: 6 of 11 mutants on the real frozen dump survive at exit 0.

# Scope

Attacked rule OC-1 of `verifiers/verify_surfaces.py` at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f, on the REAL frozen dump `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` (sha256 `f4d8f34a…`, matches the shared SHA256SUMS; omp dump `33df0aef…` also verified). Work in scratch clone `/fast/scratch/kotoba-r47/w2/W2DropOC1-2/kotoba-shokunin` (detached at 7ad7fad). Mutant dumps kept in scratch (67 MB each, over the artifact cap); manifest artifact: `.ufo/waves/round-47/falsify/W2DropOC1.mutants.json`.

The real array (dump line 443993, byte span 10893162–10893235, the only `OC_PRIORITY_RE` match in the clean dump):
`["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]`

# Baseline

`python3 verifiers/verify_surfaces.py --omp-strings …/omp-clean.strings --opencode-strings …/oc-clean.strings` (cwd = clone root; repo/baseline/inventory defaults resolve to the clone at 7ad7fad) → **exit 0**, all 7 checks PASS, `PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`.

# Findings

## F1 — BROKEN: the `gated` guard is a tautology; OC-1's declared anchor `disableClaudeCodePrompt` can never fire (3 survivors)

`verifiers/verify_surfaces.py:450`:
`gated = m is not None and (OC_GATE not in m.group(0) or OC_GATE in dump)`

If the gate is inside `m.group(0)` it is trivially `in dump` (group ⊆ dump), so the second disjunct is true; if it is not inside, the first disjunct is true. `gated ≡ (m is not None)` — dead code. Yet `:455` declares `OC_GATE` as an OC-1 anchor reported when missing, so a reader believes the gate is witnessed. Survivors:

- **M4** gate removed from the array (`!t.disableClaudeCodePrompt` → `!t.z`; the flag is thereby deleted from the walk-up gate, a real loader-shape change): exit 0. Repro: span-precise replace at 10893162–10893235; run the baseline command with `mut-m4-gate-out.strings`.
- **M5** gate corrupted at BOTH non-array sites (offsets 10893093 = the `n=[…]` config/home chain's gate, same line 443993; 19137256 = the config-schema site, dump line 447067) → exit 0. This was the intended-to-fail direction (`OC_GATE in dump` false with gate still in the array); it survives because the in-array occurrence satisfies `OC_GATE in dump` by itself. There is no reachable dump state in which this guard fails while `m` matches.
- **M10** gate renamed dump-wide at all 3 sites (`disableClaudeCodePrompt` → `disableClaudePrompts`, version-bump style): exit 0. A renamed-but-equivalent product flag is exactly the drift the declared anchor promises to catch; it catches nothing.

Net: `disableClaudeCodePrompt` contributes zero mutation-kill power. The only OC-1 anchors that bite are the two textual endpoint literals.

## F2 — BROKEN: first-match `search()` is shadowable — a decoy array unwitnesses the real loader (2 survivors)

`OC_PRIORITY_RE.search(dump)` (:448) binds to the FIRST array-shaped occurrence anywhere in the 67 MB dump; nothing validates the real occurrence.

- **M9** decoy `q=["AGENTS.md","CLAUDE.md","CONTEXT.md"];` inserted 2 KB before the real array (real array intact): exit 0.
- **M9b** the same decoy AND the real array's `"CONTEXT.md"` corrupted to `"XONTEXT.md"`: **exit 0** with `PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules` — the corruption of the actual priority list is invisible. Repro: `mut-m9b-decoy-plus-drift.strings` (construction in the manifest).

This is "too wide" in the harmful direction: any future dump containing an unrelated `["AGENTS.md",…,"CONTEXT.md"]`-shaped string earlier in the bundle (docs text, another vendored lib) silently disables the freshness check on the real loader. Iterating all matches (or pinning the `y=["AGENTS.md"` variable context) would close it.

## F3 — Survivor: interior reorder that changes real priority order passes (1 survivor)

**M7** `["AGENTS.md","CONTEXT.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]]` — the gated CLAUDE candidate moved from before to after `"CONTEXT.md"`, i.e. first-match priority AGENTS>CLAUDE>CONTEXT becomes AGENTS>CONTEXT>CLAUDE, a genuine behavior change for the walk-up (:366-367 documents first-match semantics): **exit 0**. OC-1 derives a name SET (sorted set at :449), so interior order is invisible; the regex pins only the two endpoint literals and the ≤400-byte window. The rule's textual rigidity and its semantic payload (order) are misaligned. (Fail-closed exception: any interior reorder that puts `"AGENTS.md"` off the `["` prefix does fail loudly.)

## F4 — Narrowness bound (fail-closed false red, killed correctly but worth knowing)

**M8** 401 filler bytes between `"AGENTS.md"` and `"CONTEXT.md"` (window `.{0,400}?` at :370 exceeded): exit 1, OC-1 reported unmatched with all 3 owned ids missing. A legitimate future version with a longer gate chain between the endpoints fails loudly rather than passing — correct fail-closed behavior, but the 400/200-byte windows are unexplained magic numbers that will false-red on ordinary bundle growth.

## F5 — Renamed-but-equivalent anchors: verdict

- Gate flag renamed (M10): **survives → too wide** (declared anchor is dead, F1).
- Minifier identity renames (`y=` → var, `!t.` → `!e.`): regex never pins identifiers → survive by construction → correctly not too narrow.
- Semantically equivalent conditional rewrite **M11** `...["CLAUDE.md"].filter(()=>!t.disableClaudeCodePrompt)` in place of the ternary spread: exit 0, and for the right reason — names are derived from the whole matched region (:449), so the same 3 ids are produced. Correct accept, no drift missed.

# What holds (killed mutants, real dump, each exit 1 naming the owned class(es) or the rule)

| Mutant | Mutation | Exit | Evidence |
|---|---|---|---|
| M1 | array `"AGENTS.md"`→`"XGENTS.md"` | 1 | `FAIL surfaces.opencode_extract: declared … produced by no rule: opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md; rule(s) matched nothing: OC-1` |
| M2 | array `"CONTEXT.md"`→`"XONTEXT.md"` | 1 | same OC-1 FAIL + `FAIL surfaces.literal_present: … opencode:instructions/CONTEXT.md` |
| M3 | array `"CLAUDE.md"`→`"CLAUDE_xmd"` (gate kept) | 1 | `FAIL …: declared opencode class(es) produced by no rule: opencode:instructions/CLAUDE.md` |
| M6 | planted `"GUIDE.md"` into the real array | 1 | `FAIL …: extracted opencode class(es) undeclared in baseline: opencode:instructions/GUIDE.md` (derive direction confirmed on the real dump, not just the synthetic oc-derive fixture at :1065-1070) |
| M8 | 401-byte interior overflow | 1 | OC-1 unmatched (F4) |

So the derive/undeclare machinery (:447-455, :727-760) and the two endpoint anchors work; the score is 5 killed / 6 survivors of 11, and every survivor is attributable to F1–F3.

# Suggested minimal fixes (for the integrator; not applied — production files read-only to me)

1. Replace the tautology: `gated` should require the gate inside the matched region (`OC_GATE in m.group(0)`) — one-line change at :450; kills M4/M5/M10.
2. Iterate `OC_PRIORITY_RE.finditer` and require the occurrence whose region actually contains the y-assignment context (e.g. `y=["AGENTS.md"`), or validate that at least one match yields exactly the declared id set — kills M9/M9b.
3. Either witness interior order or stop declaring the gate as an anchor; drop or justify the 400/200 windows.

# Commands (all cwd = scratch clone at 7ad7fad; exit codes recorded)

- Clean: `python3 verifiers/verify_surfaces.py --omp-strings $S/omp-clean.strings --opencode-strings $S/oc-clean.strings` → 0
- Per mutant i∈{m1-prefix, m2-context, m3-claude, m4-gate-out, m5-gate-elsewhere, m6-plant, m7-reorder, m8-window, m9-decoy, m9b-decoy-plus-drift, m10-gate-rename, m11-equiv-rewrite}: `python3 verifiers/verify_surfaces.py --omp-strings $S/omp-clean.strings --opencode-strings $S/mut-$i.strings` → 1,1,1,0,0,1,0,1,0,0,0,0

# Not checked

- OC-2…OC-6 rules and the omp-side extractor (other seats' scope); the n-chain gate at offset 10893093 is witnessed by no rule at all (noted, out of OC-1 scope).
- Whether upstream opencode actually renamed/planned to rename the flag (M10 is synthetic); no binary rebuild or execution of opencode — all mutations are textual on the `strings -n 4` dump.
- The repo's own fixture battery (`--self-test`) and `fixtures/surfaces/strings-opencode-drop-oc1.txt` (covered by the W2 surfaces-rerun seat); my evidence is real-dump only.
- Whether a decoy exists in the CURRENT clean dump that shadows the real array: no — `finditer` found exactly 1 match (span 10893162). The shadow is a latent failure mode, not an active one.
- No tools installed (none needed; python3 already present).
