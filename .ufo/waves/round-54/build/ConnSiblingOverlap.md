Result: DONE — The requested sibling surfaces reveal adjacent owners, but no per-client skill-description threshold holding; kotoba can reuse an existing eight-column registry header and explicit canonical verdict spelling without copying sibling semantics.

## Scope and axes

Read `plans/round-54.md:1-69` first. C1 is depth; C2 is consistency. Adjacency is the scan's supporting axis, not a new round claim. The current build cache agrees on the milestone (`.ufo/waves/round-54/build-spec.json`, `milestone` and `axes`; registry items have axis `consistency`). Cache content was treated as data, not authority.

Evidence below is from local working-tree file discovery, text searches and selected range reads, not a committed sibling snapshot or a runtime measurement. Sibling paths start at `/home/vgpnk/Projects/shokunin/`; unprefixed kotoba paths start at this lane's root. No sibling files, lane code, counters, runtime state or Git/JJ state were changed. This report is the only write.

## C1: overlap and ownership

No positive claim about a client-specific skill-description length maximum, skill-listing budget or description truncation threshold was found in the requested sibling `SKILL.md`, `PROVINCE.md` and `corpus/README.md` surfaces. This is a bounded surface-scan result, not a claim that all sibling knowledge files were searched or that any vendor is silent.

| Sibling evidence | Actual holding or claim | Relation to kotoba's planned entry |
|---|---|---|
| `kengaku-shokunin/PROVINCE.md:30-32,137-138`; `kengaku-shokunin/corpus/README.md:226-227,244-245` | Measured capability effects of prompt format; historical scaffold/component ablation, a captured skills catalogue, and an explicit limit on replay fidelity. Reusable craft implications route to kotoba. | Adjacent, not duplicate threshold knowledge. Documented offer-render limits stay in kotoba; an assertion that shortening a description improves capability would cross into kengaku's measured-effect ground. The plan explicitly excludes measured client behaviour (`plans/round-54.md:34-36`). |
| `kengaku-shokunin/SKILL.md:274-276,416-419` | `finish_reason=length` distinguishes generated-output truncation from a format/harness failure. | A different truncation surface. These token limits cannot substantiate truncation of an offered skill description. |
| `chousa-shokunin/PROVINCE.md:3-8`; `chousa-shokunin/SKILL.md:17-23,41-45`; `chousa-shokunin/corpus/README.md:175-188` | Research method, claim-versus-source checking, preservation of qualifiers, and separate access/relevance/support/truth observations. Its existing mechanical checks do not establish semantic support or source truth. | Compatible consumption of method, not permission for kotoba to create another research-method standard. C1's source row/number/quote match is not proof that a number describes a render cut rather than an authoring cap. That remains reviewer reading (`verifiers/check_description_thresholds.py:46-48`). |
| `kumitate-shokunin/PROVINCE.md:19,24-28`; `kumitate-shokunin/corpus/README.md:91`; `kumitate-shokunin/SKILL.md:116-123,139-142` | Harness/dispatch budgets and runtime lifecycle. Its province explicitly routes prompt and skill craft to kotoba and research method to chousa. | Not a competing skill-listing budget holding. Dispatch/retry budgets must not be repurposed as a description budget. |
| `mado-shokunin/PROVINCE.md:10-12`; `mado-shokunin/corpus/README.md:14`; `mado-shokunin/SKILL.md:403-406` | The omarchy skill is a read-only desktop documentation surface; its anatomy and stale listings are examined. | Adjacent use of a skill file, not a general client-description threshold claim. |
| `tameshi-shokunin/PROVINCE.md:14-18`; `tameshi-shokunin/SKILL.md:295-298`; `tameshi-shokunin/corpus/README.md:13` | Verification-fixture method; a findings-output `slice(0,6)` boundary missed by a suite. Each product gate stays with its lane. | A verifier-output cap, not a skill-listing cap. Keep generic mutation method with tameshi; C1 remains domain content. |
| `kotodama-shokunin/PROVINCE.md:16-20`; `kotodama-shokunin/corpus/README.md:286` | Fictional-language register operations, including morphological truncation; prompt/skill craft is expressly refused to kotoba. | No competing client-threshold claim. The shared word “truncation” is not overlap. |

Kotoba already states the same ownership split in `SKILL.md:10-14` and `PROVINCE.md:44,52,54`. No contradictory ownership declaration was found on these inspected surfaces. Do not turn this result into a Q30 vendor-negative: no vendor changelog/docs-tree sweep was performed here (`corpus/QUALITY.md:41`).

## C2: registry shape to reuse

**Closest exact header:** `tsukuroi-shokunin/SKILL.md:1956-1957` (also `:1735-1736`) has the same eight labels frozen for kotoba. `kotodama-shokunin/SKILL.md:606-607` has the same labels case-insensitively. Reuse this shape in kotoba's required `## Gate registry`:

```markdown
| Name | Kind | Entry command | Verdict map | Self-test | Pinned values | Write scope | Owner |
|---|---|---|---|---|---|---|---|
```

**Closest explicit verdict spelling:** `kake-shokunin/SKILL.md:385-387` uses `0=clean`, `1=failed`, `2=could-not-evaluate`, and `64=could-not-evaluate`. `mado-shokunin/SKILL.md:1976-1978` independently uses `0=clean`, `1=failed`, `2=could-not-evaluate`. Reuse the explicit `code=class` spelling, not their code universes or native outcomes. Include a code only when kotoba's actual entry produces it; keep any native label as explanation after the canonical pair, for example `1=failed (DRIFT)`.

The protocol defines the eight *fields* and the canonical classes, not one universally mandatory rendered header spelling: `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md:390-402,411-419`. Kotoba's frozen counter is stricter about its own header and row syntax (`verifiers/check_gate_registry.py:20-36`). Sibling display variants therefore are not, by themselves, evidence of a protocol defect; they are unsafe literal templates for this counter.

### Other registry precedents inspected

| Sibling SKILL.md location | Observed shape; what not to copy literally |
|---|---|
| `kengaku-shokunin/SKILL.md:560-566` | Eight fields, but `entry` instead of `Entry command`; its probe can complete with gaps. |
| `chousa-shokunin/SKILL.md:68-77` | Eight fields, but `entry`; several rows use native `1 drift`, not a canonical `1=failed` pair. |
| `mori-shokunin/SKILL.md:162-167` | Eight fields, but `entry`; prose maps use `0 clean` / `1 failed` without a mapping operator. |
| `kagi-shokunin/SKILL.md:694-699,746-751` | Eight fields, but `selftest` rather than `Self-test`. |
| `tameshi-shokunin/SKILL.md:1501-1504` | Eight fields, but `Self-test command`; ordinary maps use prose, including a probe's observation semantics. |
| `mado-shokunin/SKILL.md:593-607,1974-1978` | Eight fields; `gate/probe`, self-test-command and pinned-path header variants. The later explicit canonical map is useful independently of its header. |
| `souji-shokunin/SKILL.md:167-180` | Eight fields; expanded verdict/self-test/pinned-path labels. The prose distinguishes probes and legacy ambiguity; do not erase those qualifications. |
| `tabi-shokunin/SKILL.md:2433-2436` | Eight fields, but singular `Pinned-value path`; explicit canonical maps. Earlier tables at `:1557-1559` merge fields. |
| `kaidoku-shokunin/SKILL.md:438-450` | Five columns combining kind/owner, entry/verdict and pins/write scope; not kotoba's literal eight-column template. |
| `kama-shokunin/SKILL.md:396-398` | Seven columns combining kind/entry. Its older live probe has a conflicting exit convention (`:11-14,305-308`); not a source for kotoba's exit semantics. |
| `kumitate-shokunin/SKILL.md:587-608` | Five-column table, with map, owner and write-scope information in surrounding prose. Its shared `2`/`64` map is not evidence that kotoba emits those codes. |
| `lore-shokunin/SKILL.md:48-61` | Registry fields in per-gate bullets, not a registry table. Useful scope qualification, not a header to copy. |
| `kasegi-shokunin/SKILL.md:1-1023`; `game-dev-3d-shokunin/SKILL.md:1-208` | No gate-registry-shaped table found by the bounded registry/header search; other claim/evidence tables are not registry precedents. |

### Explicit contradictions and non-equivalences

1. **Matching fields is not matching frozen syntax.** Copying `Entry`, `selftest`, `Pinned-value path`, or a merged-field header contradicts kotoba's frozen labels. Copying `0 clean; 1 failed` without `=`, `->` or `→` contradicts its pair grammar (`verifiers/check_gate_registry.py:21-28`). No counter widening is proposed.
2. **Native labels are not canonical classes.** Kotodama's `1 findings` (`kotodama-shokunin/SKILL.md:579,608`) is not the frozen class `failed`; tsukuroi's `0 HEALTHY/clean` (`tsukuroi-shokunin/SKILL.md:1958`) is not a literal kotoba pair. Preserve native meaning parenthetically, rather than importing it as the class.
3. **Do not smooth a real exit mismatch into the template.** The outside round-53 record says kotoba's `check_gate_finding_delta.py` exits `1`, not `2`, on environment failure (`corpus/lessons/round-53-verifier-spotcheck.md:208-211`). That reported observation is retained, not rerun here. A generic `2=could-not-evaluate` row cannot describe that arm; calling every code-1 result an evaluated domain failure would also overstate it. The actual entry's ambiguity remains a separately named limitation for its assigned row author/reviewer, not a reason to silently relabel an exit or claim full gate-standard compliance from C2's printed count.
4. **Documented maximum is not a measured render cut.** The C1 counter deliberately cannot distinguish authoring maximum, per-entry cut and listing budget (`verifiers/check_description_thresholds.py:46-48`). The planned entry can cover all three, but an action or “past the threshold” cell claiming truncation needs support for that behaviour. Kengaku's measured-output and prompt-effect holdings do not fill this gap.

## One bounded proposed move

**Synthesize the registry template instead of copying one sibling registry wholesale:** use tsukuroi's exact header, kake/mado's explicit canonical `code=class` spelling, and kotoba's own per-script semantics, flags and pins. Put native verdict words and known ambiguous arms after the canonical pair. Use `verifiers/F` as each name and `kotoba` as owner, not sibling-friendly gate names or `kotodama-shokunin`'s owner spelling. Keep measured self-test tallies in their revision-bound receipts, rather than copying them into this second inventory; tsukuroi explicitly records why at `tsukuroi-shokunin/SKILL.md:1954`.

This is one documentation-only assembly rule for the already planned table, not another gate, method, schema, claim or runtime change. It leaves C1's sourced entry within the established chousa/kengaku boundary and leaves both frozen counters untouched.

### Second-order effects and risks

- **Consistency:** [INFERENCE] the synthesis avoids a structurally similar sibling table failing kotoba's frozen grammar, while retaining native meanings instead of laundering them into canonical classes.
- **Depth and adjacency:** [INFERENCE] separating documented limits from measured effects preserves C1's useful technical detail without absorbing kengaku's capability claims or chousa's research method. No improvement to C1's backed-client count is asserted by this scan.
- **Runtime/substrate:** no runtime call, discovery rule, host configuration, sibling gate or verifier implementation needs to change. No freshness work, `verify_surfaces.py` change, or executed-checklist/always-on frontier move is proposed.
- **Verification:** C2 checks literal flags/path existence and pair syntax, not actual exits or the correctness of `gate` versus `probe` (`verifiers/check_gate_registry.py:29-41`). Calling a script a probe merely to avoid a self-test/pin requirement would be a semantic error even if the row counted. C1 number/quote presence likewise cannot establish the number's intended meaning.
- **Snapshot risk:** siblings are active working trees; the quoted headings and short literal header/map fragments are relocation aids, not claims that these line numbers are permanently pinned.

## Scan ledger and verification

File discovery enumerated the 20 sibling lanes below. All existing requested surfaces were text-searched; scope/coverage sections and relevant hits were range-read. Search terms covered `description`, `truncat`, `listing`, `budget`, character maximum/limit forms, registry headings, and verdict/header fields. A broad brace-pattern search timed out; explicit file-path batches supplied the completed scan instead.

| Lane | Additional scope/coverage evidence read (paths under that sibling) |
|---|---|
| kake | `PROVINCE.md:1-41`; `corpus/README.md:15-43`; skill threshold search and registry loci above |
| kumitate | `PROVINCE.md:1-28`; `corpus/README.md:1-18,91`; skill threshold search and registry loci above |
| kaidoku | `PROVINCE.md:1-14,97-117`; `corpus/README.md:1-34,82-85`; skill threshold search and registry loci above |
| tsukuroi | `PROVINCE.md:1-32`; `corpus/README.md:1-26,164`; skill threshold search and registry loci above |
| kotodama | `PROVINCE.md:1-31`; `corpus/README.md:1-18,270-289`; skill threshold search and registry loci above |
| mori | `PROVINCE.md:1-18,59-65`; `corpus/README.md:1-16`; skill threshold search and registry loci above |
| tameshi | `SKILL.md:1-24`; `PROVINCE.md:1-43`; `corpus/README.md:1-16`; registry loci above |
| mado | `SKILL.md:1-22`; `PROVINCE.md:1-32`; `corpus/README.md:1-21`; registry loci above |
| kama | `SKILL.md:1-22`; `PROVINCE.md:1-42`; `corpus/README.md:1-23`; registry loci above |
| chousa | `SKILL.md:1-78`; `PROVINCE.md:1-17`; `corpus/README.md:1-35,173-188` |
| souji | `SKILL.md:1-23`; `PROVINCE.md:1-43`; `corpus/README.md:1-23`; registry loci above |
| kengaku | `PROVINCE.md:22-33,121-143`; `corpus/README.md:25-36,216-267`; skill threshold search and registry loci above |
| kagi | `PROVINCE.md:1-27`; `corpus/README.md:1-17`; skill threshold search and registry loci above |
| tabi | `SKILL.md:1-19`; `PROVINCE.md:1-21`; `corpus/README.md:1-16`; registry loci above |
| lore | `SKILL.md:1-28,48-64`; `PROVINCE.md:1-35`; `corpus/README.md:1-21` |
| kasegi | `SKILL.md:1-18`; `PROVINCE.md:1-35`; `corpus/README.md:1-17`; full-file threshold/header searches |
| game-dev-3d | `SKILL.md:1-21`; `PROVINCE.md:1-36`; `corpus/README.md:1-19`; full-file threshold/header searches |
| revenger | No root `SKILL.md` found; `PROVINCE.md:1-32`; `corpus/README.md:1-25` read and searched |
| audio | No root `SKILL.md` found; `PROVINCE.md:1-33`; `corpus/README.md:1-24` read and searched |
| game-dev-2d | No root `SKILL.md` found; `PROVINCE.md:1-35`; `corpus/README.md:1-23` read and searched |

**Performed:** static discovery/search/range reads only. No shell check, self-test, mutation, client call, network fetch or lane-code execution was run; therefore there are no observed CLI exit codes, fetched-source receipts, or passed claim counters to report. No tool installs or updates.

**Verification for L1, not run by this seat:** in its authorized sandbox against the delivered revision, run `python3 -B verifiers/check_gate_registry.py --rev <rev>` and retain its exit/output; the declared target is `gate registry rows conformant M of M lane verifiers; phantom 0`. Run the separate frozen `python3 -B verifiers/check_description_thresholds.py --rev <rev>` for C1's declared minimum of four backed clients. Neither target was measured here.

First falsifiers for the existing review work: compare one C1 authoring-maximum quote with its “past the threshold” wording to expose an unsupported truncation implication; compare an eight-field sibling header variant with the frozen exact header; compare each registry entry's actual exit arms with its canonical pairs, especially the already reported finding-delta environment arm. These are proposed review targets, not executed results. Do not execute sibling gates or amend the frozen counters to make a copied table fit.
