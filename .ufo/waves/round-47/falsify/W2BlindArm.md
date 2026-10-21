verdict: PARTIAL — attacked C1's omp partial-blindness guard and class discrimination; literal 7/7 holds, comprehensive freshness does not follow.

## Scope and axes

Reviewed landed `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`, in canonical-layout scratch `/fast/scratch/kotoba-r47/w2/W2BlindArm/kotoba-shokunin`. Axes: freshness (detect changed/new loader classes), operability (fail usefully without rejecting healthy frozen input), calibration (state exactly what green checks establish). Recommendations only; no production edits, admission, integration, runtime launch, or canonical judgment.

## Measured coverage: 17 shape/anchor-backed ids; 25 literal-only ids

All 42 entries are loader kinds. `surfaces.literal_present` itself gives class-specific pair checks to only **8/42** ids: omp's eight `loader-group` rows. The other **34/42** receive substring checks there (`verifiers/verify_surfaces.py:563-590`). Across the *whole battery*, `opencode_extract` adds shape/anchor witnesses for all nine opencode ids, leaving **25/42 (59.5%)** ids with no class-specific dump witness. These 25 are all omp: 21 loader-literal plus four loader-config, comprising 17 governed and eight excluded entries. Thus the useful whole-battery split is **17/42 shape/anchor-backed versus 25/42 literal-only**, not 42 independently established loaders. Shape/anchor-backed does not mean runtime behavior proven: several OC rules witness dispersed tokens rather than derive a complete consumer path.

Frozen omp literal-only rows, grouped by tested substring (counts are Python `str.count`, not line counts or exact JS token counts):

| Substring | Occurrences | omp ids using that same test |
|---|---:|---|
| `rules` | 416 | cursor/rules; windsurf/rules; agents/rules |
| `instructions` | 432 | github/instructions |
| `.clinerules` | 7 | clinerules/.clinerules |
| `RULES.md` | 4 | omp-dir/RULES.md |
| `enabledProviders` | 3 | provider-gate/enabledProviders |
| `AGENTS.md` | 37 | agents-md-walkup/AGENTS.md; omp-dir/AGENTS.md; codex/AGENTS.md |
| `CLAUDE.md` | 15 | claude-dir/CLAUDE.md |
| `SYSTEM.md` | 27 | agent-system-prompt/SYSTEM.md |
| `plugins` | 561 | marketplace/plugin-rules; discovery/plugins |
| `prompts` | 491 | agents/prompts; github/prompts; codex/prompts |
| `skills` | 492 | agents/skills; discovery/skills-roots |
| `mcp.json` | 69 | discovery/mcp-configs |
| `settings.json` | 41 | discovery/settings |
| `extensions` | 550 | discovery/extensions |
| `commands` | 758 | discovery/commands |
| `managed-skills` | 10 | unknown/managed-skills |
| `agents` | 801 | unknown/subagent-roster |

The eight discriminated omp ids are exactly census `corpus/knowledge/instruction-surface-census-round13.md:73-80`. The 25 weakly discriminated omp declarations are at `:88-104` and `:263-270`. The nine opencode ids are the current baseline's opencode entries, covered separately by OC-1/OC-2/OC-3a/OC-3b/OC-4/OC-6; OC-5 is an additional path witness owning no id. `W2BlindArm.repro.txt` emits all 42 per-id measurements.

## Finding A: partial blindness remains outside the guard

**Evidence:** `verifiers/verify_surfaces.py:156-159` remains a callee-name allowlist. `:316-333` only scans that regex. The new blind arm at `:628-637` executes only for `not pairs`; it cannot notice an unknown registration when one or more known registrations survive. `:638-655` compares only already-extracted ids.

**Counterexample, reproducible:** append `BlindArmNew(u,"blind-arm","UNDECLARED.md");` to the frozen omp dump, leaving baseline and inventory unchanged. All seven checks PASS, verifier exit **0**, eight omp pairs. Control: append the identical call with `Fo` as callee instead; verifier exits **1**, nine omp pairs, with `1 loader class(es) undeclared in baseline: omp:blind-arm/UNDECLARED.md`. This is a synthetic extraction counterexample, not a claim that the frozen shipped artifact contains that loader or that the appended call executes.

**Strong counterexample against overstatement:** replacing current `lq(` call tokens with `BlindArmRenamed(` leaves six extracted ids. `no_uncovered_class` PASSes (`all 6 extracted loader class(es) declared`) and emits no blindness diagnostic, but `literal_present` FAILs the two known missing loader-group pairs; whole battery exits **1**. Therefore partial rename of an *already-declared loader-group* is not a whole-suite escape. The escape concerns unknown classes and non-pair-checked declarations, not every partial rename.

**Current-artifact control:** a generic-callee scan using the same argument/.md grammar found 11 occurrences, all `lq` (2), `Xl` (5), `Fo` (4). The allowlisted scan also found 11 occurrences, collapsing to eight ids. No currently unknown callee was discovered within this narrow grammar. This supports the repin as a repair of today's known registration subset; it does not validate future unknown shapes.

**Impacted axes:** freshness, calibration. Operability of the known-row reverse check survives.

**Smallest safe correction:** preserve the known-pair reverse check; label the blindness arm explicitly as zero-extraction-only. To claim partial-blindness detection, add a separately bounded candidate scan/audit tied to identified discovery helpers, with unknown candidate callee/shape reported for review and a planted-unknown-callee fixture. Merely appending more minified names is a repin, not an independence improvement. Do not blindly classify every generic JS call as a loader: that would trade freshness against false positives.

## Finding B: a real non-.md registration can change while all seven stay green

**Evidence:** only `loader-group` gets pair discrimination at `verifiers/verify_surfaces.py:578-585`; loader-literal/config use `literal in dump` at `:572`. The cursor declaration is census `:88` with literal `rules`; omp's .md-only regex is `verifiers/verify_surfaces.py:159`.

**Counterexample, reproducible:** in the frozen omp dump replace the third literal of both matching `Xl(u, "cursor", "rules"` / `Fo(u, "cursor", "rules"` registrations with `"disabled-rules"` (two replacements). All seven checks still PASS, exit **0**, eight omp pairs. This changes the class-specific discovery registration text without changing baseline/inventory; generic `rules` remains abundant, and even remains a substring of the replacement. It establishes failure to discriminate that registration, not proof that every independent cursor consumer is absent or that runtime behavior changed.

**Impacted axes:** freshness, calibration. The result is within the implementation's documented literal-only semantics, but cannot support a broader claim that the 25 declared classes were individually revalidated by this gate.

**Smallest safe correction:** make the result distinguish `8 pair-verified + 34 literal-present`, with the separate `9 opencode shape/anchor-backed` result, rather than reporting all 42 as simply 'verified'. Add context/registration witnesses and negative mutations for the 25 rows if claiming automated per-class freshness. An honest bounded ceiling is an acceptable tradeoff only for the canonical judge to accept; this report does not reject that tradeoff itself.

## Is C1's 7/7 honest?

**Yes as an observed number of passing check functions**, including the independent OC result `9/9 declared class(es) from 7/7 rules`; **no as a shorthand for complete loader coverage or 42 class-specific freshness proofs**. The frozen dumps produce exactly the advertised green result. Existing documentation already disclaims existential completeness (`verify_surfaces.py` module documentation; census `:364-377`), so this is not evidence of fabricated receipts. However the census ceiling at `:370-372` still says five opencode ids, while the current measured result is nine; `:375` describes 'parity both ways', which depends on the separate literal_present reverse arm, not no_uncovered_class alone. Those are calibration hazards when presenting the result without qualifications.

## Commands exercised and exits

1. `git rev-parse HEAD` in scratch — exit **0**, exact requested landing hash.
2. `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` — exit **0**, both binaries and both dumps `OK`.
3. Baseline CLI invoked via `v.run_capture` / `main`: `--repo <scratch> --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings --json` — verifier exit **0**, PASS **7**, FAIL **0**, 42 literal entries, eight omp pairs, nine opencode ids/seven rules.
4. `python3 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2BlindArm.repro.txt` — process exit **0**. Script invokes the actual CLI function with temporary mutated dumps; each verifier exit is reported separately:

| Variant | omp pairs | Verifier exit | PASS/FAIL |
|---|---:|---:|---|
| frozen baseline | 8 | 0 | 7/0 |
| unknown-callee new class | 8 | 0 | 7/0 |
| known-callee new class (control) | 9 | 1 | 6/1 |
| cursor registration literal changed (2 replacements) | 8 | 0 | 7/0 |
| partial current-callee rename (5 `lq(` tokens) | 6 | 1 | 6/1 |
| all current-callee rename (87 tokens, including non-.md calls) | 0 | 1 | 5/2 |

The zero-pair control names both `vacuity:` and `extractor blind: 33 declared literal(s) present`; that arm works for its actual zero-only scope.

5. Python in-process counting/generic-regex probes — completed normally: class-backed **17**, literal-only **25**, generic .md occurrences **11**, allowlisted .md occurrences **11**. Exact generic scan retained the verifier's first-argument/group/file grammar but replaced its callee alternation with `[A-Za-z_$][A-Za-z0-9_$]*`; this is not a complete JS parser.

Reproduction file is small, imports the scratch landing verifier, mutates only temporary dump files under the scratch parent, and deletes them on completion. No commits were needed because this verifier reads working files/dumps rather than committed-state corpus inputs. No tools installed or updated.

## Not checked

No default live binary resolution, wrapper execution, omp session, runtime prompt injection, full decompilation, additional JS shapes beyond the stated grammar, binary provenance beyond frozen SHA manifest consistency, substrate-pin gate, C2 checklist, C3 corpus/fault harness, source rows S012–S015, or frontier lesson admissions. No claim that dump mutations are executable patched binaries. Did not independently certify the historical narrative or all 25 manual source-to-consumer derivations. Report is lane-authored review, not non-author closure.
