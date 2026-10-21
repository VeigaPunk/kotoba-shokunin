verdict: the round-47 ground is sibling-shared in exactly two places — the host substrate identity (kumitate records `omp/18.12.3`; kagi records `opencode 1.18.31` at `~/.opencode/bin/opencode`, a path that no longer exists) and checklist execution (kagi and kumitate each ship a frozen checklist grammar) — while the instruction-surface extractor, the agentskills.io/Claude-docs rows, and the description validator are kotoba-only. Proposal: C1's evidence gains a dated, report-only three-row substrate-identity handoff; no sibling edits, no new gate.

# Connector — sibling overlap on round-47 ground (L2 floor)

Base: `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (verified: `git rev-parse HEAD` → that sha, exit 0; `git status --porcelain -- SKILL.md PROVINCE.md verifiers/ corpus/SOURCES.md LOG.md` → empty, exit 0). Kotoba paths below are relative to the lane root and at BASE. Sibling paths are in their own repos at read time (2026-10-21), not at kotoba's BASE.

## Axes (named)

| axis | round claim | what this report touches |
|---|---|---|
| freshness (8.0) | C1 — re-derive instruction surfaces, re-pin omp 18.12.5 / opencode 1.19.3 | shared host-identity records in kumitate and kagi; path move invisible to sha/mtime |
| operability (8.5) | C2 — `description` XML-tag check + drop `<skills>` | no sibling owns the rule; two sibling checklist-execution precedents constrain the design; box-map/floors traps |
| calibration (8.5) | C3 — fail-closed erratum registry + corpus index | kumitate `anchor-truth` is the fleet precedent for pinned recorded absences |
| adjacency (8.0) | PROVINCE/sibling routing | this report is routing evidence only |

## Evidence

### 1. Substrate identity is recorded in three lanes; the pin instrument is kotoba-only

kotoba owns the only executable pin:

- `verifiers/check_substrate_pins.py:61-63` — `BINARIES` maps `opencode` to the literal `/home/vgpnk/.opencode/bin/opencode`; `:75` is the pin set; `verifiers/baseline.json:5,9` hold `omp_binary_sha256` / `opencode_binary_sha256`.
- C1 will re-pin those values and the extraction rules in `verifiers/verify_surfaces.py`.

The same host facts are asserted elsewhere:

| lane | file:line | asserted fact | state now |
|---|---|---|---|
| kumitate | `kumitate-shokunin/corpus/SOURCES.md:17` (S004) | `omp --version` → `omp/18.12.3`, status mined, recheck `on-release` | live `omp --version` prints `omp/18.12.5` (exit 0) |
| kumitate | `kumitate-shokunin/corpus/knowledge/omp-task-contract.md:2` | verified-at `…; host omp/18.12.3` | false at read time |
| kumitate | same file `:3` | recheck command `omp --version` → `omp/18.12.3 (2026-10-19)` | the command now prints 18.12.5 |
| kagi | `kagi-shokunin/corpus/knowledge/handler-trust-boundary.md:8` and `:276` | `opencode 1.18.31 binary ~/.opencode/bin/opencode`; "an upgrade can move any of these — re-probe before citing" | path ABSENT; no 1.18.31 binary there |
| kagi | `kagi-shokunin/corpus/knowledge/config-layering.md:4` | `opencode 1.18.31` as the source basis | same |
| kagi | `kagi-shokunin/SKILL.md:233`, `kagi-shokunin/corpus/knowledge/drift-gate.md:161` | the path is explicitly excluded as "not lane-owned bytes", unpinned | correct: no kagi gate breaks |
| kotoba (self) | `corpus/knowledge/opencode-offer-trace-round8.md:5-8`, `:130` | `~/.opencode/bin/opencode` (185,030,784 B, mtime 2026-09-14, BuildID `c30f169b…`) | path ABSENT |
| kotoba (self) | `corpus/knowledge/opencode-extraction-round14.md:1-8`, `:98` | dump sha `d9123b9b…`, "opencode v2.0.26"; historical by its own errata | path ABSENT |
| kotoba (self) | `corpus/knowledge/claude-md-surface.md:9`, `SKILL.md:431` | occurrence counts / substrate line at `~/.opencode/bin/opencode` | path ABSENT |

Measured identities (commands in §Verification): omp `18.12.5`, sha256 `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`; opencode `1.19.3`, sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`, 186,013,824 B, at `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`.

No gate spans the lanes:

- Fleet census `scripts/sources-census.sh:36-37` reports symbolic cadences (`on-release`) and "never judges [them] overdue". `validate kotoba-shokunin` → exit 0 (`ok`); `shared kotoba-shokunin` → exit 0, 0 rows.
- kumitate's own gate validates only the *recheck cell*: `kumitate-shokunin/scripts/sources-check.mjs:7` ("does not use the network"), `:21` (`RECHECK_INVALID` = bad date/cadence), `:308-309` (checks the string, never runs the command). `[INFERENCE]` kumitate's gate cannot see the 18.12.3→18.12.5 bump; I read the contract, I did not run its gate.
- kagi's gates exclude the path by design (`SKILL.md:233`), so the path's disappearance is not a kagi gate failure — it is a record of a vanished source basis.

Contested scope: the *host substrate version/path* fact is asserted by three lanes; the *pin instrument* exists only in kotoba. kotoba must not rewrite kumitate's S004 or kagi's source basis (`PROVINCE.md:23-30` routes kumitate/kengaku/tameshi as adjacent; kagi is named in `SKILL.md:10-13` as owning its own SKILL.md content). But the C1 re-pin is the fleet's only observation of the path move.

### 2. Instruction-surface extraction is kotoba-only; the runtime half is kengaku's

- Only kotoba has a `verifiers/` directory (`ls -d *-shokunin/verifiers` → one hit).
- kumitate's "surface" is a different object: `kumitate-shokunin/scripts/surface-probe.mjs:1-8` probes the ufo-sighting `surface --json` manifest and fleet-dispatcher status.
- kagi's "surface" is host config: `kagi-shokunin/corpus/surface-census.sh:2-24` censuses `~/.config/the-janitor/` assets/runtime artifacts.
- tameshi already reads kagi's gate as *the* fleet "surface-census" row (`tameshi-shokunin/corpus/knowledge/fleet-kill-rate-ledger.md:46`). A bare "surface census" in kotoba's round report will resolve to kagi's instrument in fleet search.

The one genuine adjacent half is kengaku's runtime capture: `kengaku-shokunin/corpus/knowledge/bench-arena-round7-scaffold-ablation.md:19` records the composed opencode system message — `<env>` + `<available_skills>` catalog, "94% of the ~12K chars is the skills catalog (18 skills)". That is exactly what `verifiers/verify_surfaces.py:30-45` documents it cannot see ("a compiled-in call shape proves the loader path exists in the binary, not that it fires at runtime or reaches a prompt"). C1's "7/7" is a static set-parity claim; kengaku's entry is the only fleet evidence about what reaches the prompt, and it predates both re-pinned binaries. Report the boundary; do not read C1 as runtime coverage, and do not re-derive kengaku's measurement.

### 3. The description rule and its sources are uncontested; the checklist registry is not

- agentskills.io / Claude-docs rows exist only in kotoba: `corpus/SOURCES.md:14-16` (S001 spec, S002 client implementation, S003 best-practices) plus `:24` (S011, rejected). A grep across all 21 lane `*/corpus/SOURCES.md` finds no other `agentskills.io`, `platform.claude.com`, `docs.claude.com`, `code.claude.com` row. Fleet `shared` mode confirms 0 shared URLs for kotoba (exit 0). No lane holds a competing S003.
- No sibling validates `description` semantics: kumitate validates knowledge-entry headers (`sources-check.mjs:12-20`), not SKILL.md; kagi binds SKILL.md checklist *items* (`checklist-run.sh:1-31`), not frontmatter.
- Tag scan: 18 of 21 lane directories carry a `SKILL.md` (three do not); only `kotoba-shokunin/SKILL.md:14` carries a tag-shaped `<skills>` in the frontmatter (inside the `description: >` fold opened at `:3`). The independent seat `C2FleetScan.md:1-3` found the same and notes 17 tag-free siblings. So C2's fleet blast radius at BASE is zero.
- But two sibling checklist-execution instruments exist, and they constrain the *design* (not the source):
  - kagi `corpus/checklist-run.sh:1-39` — `id/class/lead/check/expect_exit/expect_last/reason/note`, class `runnable|by-hand`, bijection over 16 items, `CHECKLIST_RATIO runnable=K/N` with a delegated/direct split (`corpus/knowledge/checklist-execution.md:1-50`).
  - kumitate `scripts/surface-probe.mjs:17-28`, `:946-1040` — frozen GFM grammar `— \`cmd\` → exit n + \`expected\``, `SKIP(self)`, `CHECKLIST: n/m`, hermetic selftest.
  - kotoba's instrument is a third shape: Python stdlib, box-map + `CHECK_IDS` (`verifiers/verify_skill_checklist.py:282-293`), fleet-scanned with foreign-file hint semantics (`:225-233`). Do not adopt either sibling grammar; do not fuse.

C2 landing traps internal to kotoba's registry (not named in `plans/round-47.md:28-30`):

- the map is two-sided — unknown check id FAILs (`verify_skill_checklist.py:1085`), map entry with no live box FAILs (`:1121`), live box with no map entry FAILs (`:1129`), and `box_total` is a two-sided shrink floor (`:1070`, `verifiers/checklist-baseline.json:253` = 41; current dispositions 33 unexecuted / 8 executed). Adding an 11th id without a mapped box leaves it uncredited; adding a box requires a new `text_sha256` and a `box_total` bump.
- assertion floor — `verifiers/floors-registry.json:5` pins `checklist` at 1597; `verifiers/check_assertion_floors.py:121,142` enforce it. A C2 refactor that *drops* self-test assertions reds the floors gate; adding assertions is safe (lower bound) but the floor must not be left below the observed count only accidentally — the registry's own BUMP-IN-STEP rule governs any move.
- foreign-target scope — kotoba's frontmatter disclaims sibling content (`SKILL.md:10-13`), and `:225-233` says foreign-file FAILs are hints, not verdicts. If the new check runs unconditionally on `--skill` targets, the first sibling to add a tag gets a FAIL in a file kotoba says it does not own. Scope the check to the pinned target, or keep the hint rule.

### 4. Erratum registry: kumitate's anchor-truth is the fleet precedent (and the boundary)

`kumitate-shokunin/scripts/anchor-truth.mjs:1-52` pins one expectation per anchor in `.ufo/pins/anchor-truth.json`: `expect: true | unchecked | debt:false | debt:dead`, findings `DEBT_STALE` (a recorded debt now reads true), `DEBT_GREW`, `CHECKED_SHRANK`, `PIN_REGRESSION`; `TRUTH: FAIL-CLOSED` on pin trouble. Structurally this is the same class as C3's "pinned, fail-closed erratum registry for recorded absences" (`LOG.md:2111`, where the line records a runner's absence and the governance citation gate cannot resolve it). kagi's `corpus/claim-ledger.sh:1-35` is a third calibration registry (command + expected exit + expected last line).

Contested scope, stated: these are three different registries for three different subjects. Importing kumitate's `debt:*` model into kotoba's citation gate would create two definitions of "recorded absence" across the fleet and make each gate read the other's debt as its own. C3 may cite the model as precedent; it must keep the registry scoped to kotoba's own `LOG.md`/`SCORECARD.md` citation subjects, as the existing check already is (`verify_skill_checklist.py:215-219`: governance resolution is a HEAD-navigability check for repo-root files).

### 5. Mutation evidence: tameshi already carries kotoba as U8

- `tameshi-shokunin/corpus/knowledge/fleet-kill-rate-ledger.md:127` — "kotoba `verifiers/*` — file existence is O, their gate-ness is U until a survey admits them"; `:233` — U8 names kotoba among sightings with unresolved gate-ness.
- The ledger's rate contract: composition-bound (`:27-29`), and a post-hardening re-run is a "directed repair, not an independent rate" (`:36`); tameshi never patches a sibling gate (`:35-38`).
- Round 47 already produced lane-authored numbers: `C1MutationSurfaces.md:4,56` (6/10 = 60%) and `C1MutationPins.md:1` (5/10). Both are correctly labelled "lane-authored mutation evidence only". Keep that label in any integrated text: a bare "kill rate" would be read as a fleet row under the ledger's composition rule, and the composition (10 single-edit mutants over extraction / pin checks) is not the ledger's four sweep compositions.

## Contradictions (stated, not scored)

1. **C1 can be fully green while kumitate's recorded `omp --version` output stays false.** C1's acceptance counts verifier exits and re-verdicted classes; C3's axis is "records match repo state". No gate spans the lanes, so the two axes disagree in opposite directions on the same substrate change. This is not a reason to edit kumitate's row; it is a reason to name it.
2. **C2's fleet scan proves the rule is not a fleet problem.** Zero of 17 siblings carry a tag; the gain is kotoba's own executed check, not alignment. Any sentence claiming the rule "brings the fleet into conformance" is false at BASE.
3. **The opencode version record is not monotone**: 1.18.23/1.18.25/1.18.31 at round 8 (`opencode-offer-trace-round8.md:7-8`), `v2.0.26` at round 18 (`opencode-extraction-round14.md:1-5`), `1.19.3` now. `[INFERENCE]` whether this is a renumber, a different distribution, or a mis-read `--version` is unknown; the handoff must record raw observations and not tell a version story.
4. **`PROVINCE.md:21` and `corpus/README.md:74` still say "surfaces 5/7, pins 1/3"** while `before/verify_surfaces.override-oc.json` reports 4 pass / 3 fail and `before/check_substrate_pins.py.out` says `DRIFT 3/3 pins failed`. ConnProvinceFrontier (`ConnProvinceFrontier.md:44-46`) and ConnQualityCriteria (`ConnQualityCriteria.md:133`) already own this staleness; I confirm it and do not re-propose it.

## Proposed move (one, bounded)

**Give C1's evidence a dated, report-only "substrate identity handoff" block — three rows, no new gate, no sibling edits.** It is a compatible synthesis with ConnQualityCriteria's Q19 ("carried records expire with their anchor", `ConnQualityCriteria.md:82,133`) extended from Frontier rows to the *substrate anchor*, and with ConnProvinceFrontier's treatment of the round-46 figures as historical (`ConnProvinceFrontier.md:107`).

Shape (in the C1 report and the round-47 append-only `LOG.md` entry only):

| lane | record (path:line) | asserted identity | observed now (timestamp + sha) | owner action |
|---|---|---|---|---|
| kumitate | `corpus/SOURCES.md:17`; `corpus/knowledge/omp-task-contract.md:2-3` | `omp/18.12.3`, `on-release` | `omp --version` → `omp/18.12.5`, sha256 `fdbc8136…` | owner re-opens S004; kotoba does not edit |
| kagi | `corpus/knowledge/handler-trust-boundary.md:8,276`; `config-layering.md:4` | `opencode 1.18.31` at `~/.opencode/bin/opencode` | path ABSENT; npx ELF `1.19.3`, sha256 `179ca421…` | owner re-probes under its own "re-probe before citing" clause |
| kotoba (self, historical) | `corpus/knowledge/opencode-offer-trace-round8.md:5-8,130`; `opencode-extraction-round14.md:1-8,98`; `claude-md-surface.md:9`; `SKILL.md:431` | BuildID `c30f169b…` / dump `d9123b9b…` at the old path | path ABSENT; identity as above | entries stay verbatim (historical); the handoff row names them |

Why this and not the alternatives:

- It improves **freshness** (the re-derivation now includes *path identity*, which sha/mtime cannot express: `check_substrate_pins.py` reports `UNREADABLE` today and the re-pin will erase that signal by naming the new path) and **calibration** (the records that cannot be fixed in-lane are named, not silently left), and harms **operability** and **adjacency** by construction (append-only prose, dated, owner-decided).
- Rejected: absorbing the description rule as a fleet gate (would judge sibling SKILL.md content kotoba explicitly disclaims at `SKILL.md:10-13`, for zero current gain — 17 tag-free siblings); importing kumitate's `anchor-truth` debt semantics into C3 (two registries, two definitions of absence); minting a kotoba kill rate (tameshi owns composition-bound rates; the round's numbers are correctly lane-authored, keep them so).

Acceptance for the move:

1. The C1 report (or its LOG entry) carries the three rows with the commands' *raw* outputs, each stamped at observation time, and the two sha256 digests.
2. Every row says "observed; owner decides"; no sibling file is written by kotoba.
3. No new corpus file is created (so `verify_corpus_integrity.py`'s index/tracked-file counts are not perturbed by this move); the block lives in the append-only LOG entry and the C1 report.
4. The C1 claim text calls the subject "instruction-surface (loader-class) census", never bare "surface census", to avoid resolving to kagi's gate in fleet search.

## Risks

- **Read as absorption.** Mitigate with the owner-action column and the explicit no-edit statement; the rows cite commands, not conclusions.
- **The observation itself can age.** omp can move again; the timestamp + sha are the discriminator. Do not restate the version without them.
- **A fourth record.** Keeping the block in LOG/report prevents a new registry that itself goes stale; if the L1 wants it machine-readable, it should be an input to the existing erratum registry (C3), not a second file.
- **The `[INFERENCE]` on kumitate's gate** is a read of its contract, not a run. Its owner should probe it; kotoba must not claim the probe.
- **C2 sequencing.** The new check id, box map and floors floor are three linked edits. If C2 lands the id first and the box second, one intermediate commit fails `box_map_complete` or leaves the check uncredited; the plan's acceptance (`plans/round-47.md:28-30`) names neither `box_total` nor the floors registry.

## Verification (commands run; exit codes)

| command | exit | key output |
|---|---|---|
| `git rev-parse HEAD` (lane) | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `git status --porcelain -- SKILL.md PROVINCE.md verifiers/ corpus/SOURCES.md LOG.md` | 0 | empty |
| `python3 -B verifiers/check_substrate_pins.py` | **2** | `DRIFT 3/3 pins failed: omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256`; opencode pin `UNREADABLE` |
| `python3 -B verifiers/verify_surfaces.py --json` | **2** | `error: opencode binary not found: /home/vgpnk/.opencode/bin/opencode` |
| `omp --version` | 0 | `omp/18.12.5` |
| `sha256sum /fast/scratch/kotoba-r47/shared/bin/{omp-18.12.5,opencode-1.19.3}` | 0 | `fdbc8136…98e7e`, `179ca421…3ab7ee9` |
| `test -e /home/vgpnk/.opencode/bin/opencode` | 1 | ABSENT |
| `sha256sum /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode` | 0 | `179ca421…`, 186,013,824 B |
| `bash scripts/sources-census.sh validate kotoba-shokunin` (fleet read-only) | 0 | `kotoba-shokunin  ok  …/corpus/SOURCES.md` |
| `bash scripts/sources-census.sh shared kotoba-shokunin` | 0 | 0 rows |
| tag scan over every lane `SKILL.md` frontmatter | — | only `kotoba-shokunin/SKILL.md:14` (`<skills>`) |

No tool was installed or upgraded. No subagent was spawned. No write outside this report.

## What I did NOT check

- I did not run kumitate's `sources-check.mjs`, kagi's gates, or tameshi's survey; the "cannot detect" claim is a contract read, marked `[INFERENCE]`.
- I did not execute `~/.local/bin/opencode` (contract) and did not verify the npx package's version string from the binary; `1.19.3` comes from the npx directory name, the wrapper's `package="opencode-ai"` line, and the frozen snapshot name.
- I did not open kengaku's archived capture (`/tmp/bench-r7/...` is ephemeral); I relied on `corpus/knowledge/bench-arena-round7-scaffold-ablation.md:19`.
- I did not scan lane corpora outside `corpus/SOURCES.md` and `corpus/knowledge/*.md` for agentskills/Claude-docs references, and did not check `chousa`'s research corpus for duplicate source rows.
- I did not test C2's foreign-target behaviour empirically; I read the code path and fixture labels (`verify_skill_checklist.py:1945-1951`).
- I did not read the integration spec or any L1-only artifact; `plans/round-47.md` is the only plan read.
- I did not verify the `PROVINCE.md:21` / `corpus/README.md:74` numbers against the *round-46* run that produced them; I only compared them to round-47 `before/` outputs.
