# RuleTameshi — routed defect D3 fact base (tameshi pin vs tip)

**Result: `adjacent` holds under precedence (a) and under (b) as written.** No tameshi scope surface
claims to write or audit another lane's SKILL.md, prompts or AGENTS.md-class files. `contested` is
reachable only under a maximally literal reading of (b) that counts kagi's SKILL-checklist gate as a
"kotoba-core instrument", which the kotoba side does not say.

Scope read: `/home/vgpnk/Projects/shokunin/tameshi-shokunin` at pin
`3b20f073c7305a582562cd323982991464c324f3` and at tip `2227d8338c02aa9a5fd7d95c1a41b76865ad7647`
(branch `HEAD`); kotoba at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. No writes outside this report.
No installs. Prose lines, not symbol contracts: no language server applies, so quotes are literal
`grep`/`sed` reads and carry no semantic-proof claim.

## 1. Does tameshi claim to write or audit other lanes' SKILL.md, prompts or AGENTS.md-class files?

**No, on every committed scope surface.**

- The lane's declared domain is the method, not any sibling's text: `PROVINCE.md:3` — "**Domain:**
  verification-fixture craft — the reusable method of honest checks: hermetic suites, mutation
  testing, fail-closed arms, verdict-line discipline, no-permissiveness audits, before/after proof."
- The refusal is explicit and names the object class: `PROVINCE.md:14-17` — "every lane's gate
  remains its own; tameshi owns only the reusable craft … Never edits a sibling's gate code
  (read-only probes; recommendations travel in round reports)." `PROVINCE.md:20` — "**Out of
  province → report, never absorb.**"
- The prompt surface is absent, not merely refused: `grep -c prompt SKILL.md` = 0 (exit 1). The
  words prompt, AGENTS.md do not appear as a tameshi object anywhere in `SKILL.md`, `PROVINCE.md`
  or `corpus/` outside quotations of a sibling's own files.
- Read-only is restated in the instrument contract: `SKILL.md:864-865` — "**Read-only** — target sha
  before = after and the sibling tree stays porcelain-clean"; `SKILL.md:1545` — "Do not rerun a
  sibling's gate to obtain closure evidence."; `SKILL.md:1690-1692` — "no sibling gate is registered
  or executed by this lane".

**What it does do with a sibling artifact, exactly.** Core admits *gate scripts* as read-only primary
surfaces: `PROVINCE.md:28-36` — "the six recorded mutation legs' gates as read-only primary
surfaces — … kagi `corpus/surface-census.sh` and `corpus/checklist-run.sh`, …". Purpose is
measurement (kill rate), service form, owner-side absorption: `corpus/knowledge/fleet-kill-rate-ledger.md:272`
— "service form, targets read-only, predictions pre-registered before each run"; `:276` — "**no** —
recommendations only; owner = kagi".

**The one SKILL.md relation is kagi's, observed, not claimed.** kagi's gate reads kagi's own
checklist: `corpus/knowledge/gates-survey-kagi.md:230-231` — "`checklist-run.sh:11-21` claims a
bijection between 16 `SKILL.md` items and 16 `checklist.tsv` rows." The sweep never exercised that
read path: `corpus/knowledge/mutation-case-kagi-checklist.md:47` — "**Suite (O).** `bash "$MUTANT"
--selftest`, 34 cases"; `:50` — "the selftest builds every fixture under `mktemp -d`"; `:347` —
"**U1** — suite-only scope: the 15 mutants were adjudicated by `--selftest`". So the instrument ran
over a gate script and its selftest fixtures; it did not run over, mutate, or audit kagi's SKILL.md.

**kotoba's own instruments are explicitly outside the queue, not claimed:**
`corpus/knowledge/fleet-kill-rate-ledger.md:125-130` — "**Boundary — sightings and adjacent
machinery, not queued** … kotoba `verifiers/*` — file existence is O, their gate-ness is U until a
survey admits them"; `:233-234` — "**U8** — sightings (kake, kama, kotoba) have unresolved
gate-ness; their admission state is U until a survey admits them."

## 2. Does either side state a split covering the same artifact or function?

**Yes, on kotoba's side only; the split is by function, not by artifact.**

- kotoba `PROVINCE.md:55` (committed at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`) — "verification-fixture
  craft and mutation testing; tameshi owns the fixture method; kotoba owns the SKILL-checklist
  instrument (kotoba base `PROVINCE.md` § Adjacent; tameshi corpus `fleet-kill-rate-ledger.md:125-128`);
  open: tameshi's Core names kagi's `corpus/checklist-run.sh`, which reads kagi's SKILL.md checklist —
  recorded for the integrator, not ruled here".
- The base statement the row cites: kotoba `PROVINCE.md:32` at `a5adc146` — "tameshi —
  verification-fixture craft and mutation testing." Listed under "## Adjacent — Sibling-owned ground
  (report, don't absorb)".
- kotoba's Core claims the instrument side of the same function: `PROVINCE.md:12-14` — "`SKILL.md` —
  trigger/frontmatter craft …"; "Agent-definition, always-on (AGENTS.md-class) and dispatch-prompt
  craft …"; "Executable instruments over those surfaces — `verifiers/verify_skill_checklist.py`,
  `verifiers/verify_surfaces.py`, …".
- tameshi states no split over that function. Its nearest text is the boundary note above (kotoba
  `verifiers/*` not queued, gate-ness unknown) and `PROVINCE.md` Adjacent — "report, never absorb:
  every sibling gate's code and product clauses (owner lane)".

Shape of the gap: the split divides "fixture method" from "SKILL-checklist instrument". It does not
name kagi's `corpus/checklist-run.sh`, so it does not textually resolve whether mutation-testing a
*third lane's* SKILL-checklist gate stays under "fixture method". tameshi's own boundary note puts
kotoba's instruments out of the queue; nothing on either side assigns kagi's gate.

## 3. Did anything relevant change between the pin and the tip?

**No scope-relevant change.** Pin is an ancestor of the tip (`git merge-base --is-ancestor` exit 0).

- `corpus/knowledge/fleet-kill-rate-ledger.md` is byte-identical at both revisions: blob
  `bd6aae4e8d4afed21b2645dcb0e35af7b1648e33` at pin and at tip, so the 125-128 boundary note and the
  U8 sighting line are unchanged.
- `git diff --stat pin tip -- . ':(exclude).ufo'` → 17 files, 1284 insertions, 34 deletions. Relevant
  ones are count and anchor maintenance only: `PROVINCE.md` +13 (round-26 append: the ninth recorded
  leg is kumitate `scripts/cite-check.mjs`, "probed read-only as a kumitate `scripts/*` primary
  surface"); `SKILL.md` +54 (leg count 8 → 9, anchors `mutate-and-run.sh:597-620` → `:603-629`, one
  new `tools/mte-interop.py` table row); new notes
  `corpus/knowledge/mutation-case-kumitate-cite-check.md`, `corpus/knowledge/oracle-anchored-survivors.md`,
  `corpus/lessons/round-25*.md`, `corpus/lessons/round-26*.md`.
- Nothing added mentions kotoba or a sibling SKILL.md as an object. `grep -n "kotoba\|SKILL.md"` over
  the new notes returns one hit pair, and both are tameshi's own file:
  `corpus/lessons/round-25.md:124-126` — "input drift of 17 SKILL.md sections … SKILL.md itself is
  unchanged" (tameshi's own cold-read monitor over tameshi's own sections).
- The only new external-source work is method-level: `oracle-anchored-survivors.md` cites S012, S090,
  S091 and classifies survivors against "specification-anchored" expectations. No sibling artifact.

## 4. Ruling under each candidate precedence

**(a) A stated split covering the same function decides `adjacent` — holds.** A split is stated on
kotoba's committed scope surface (`PROVINCE.md:55`, confirmed in the blob at the lane commit) and
divides exactly the function at issue: tameshi owns the fixture method, kotoba owns the SKILL-checklist
instrument. The pin comparison is real (pin `3b20f07`, quoted statement at
`fleet-kill-rate-ledger.md:125-128`). Ruling: `adjacent`.

**(b) Any claim over kotoba-core instruments decides `contested` — does not trigger as written.** The
kotoba-core instruments are the eight verifiers named at `PROVINCE.md:14`, and tameshi's only
statement about them is an abstention: existence observed, gate-ness unknown, "not queued"
(`fleet-kill-rate-ledger.md:125-128`, `:233-234`). No claim, so no `contested`.

**Residual, recorded not resolved.** The literal-function reading stays open: kagi's
`corpus/checklist-run.sh` *is* a SKILL-checklist instrument and tameshi's Core names it. A rule that
treats "kotoba owns the SKILL-checklist instrument" as covering every lane's SKILL-checklist gate
would make the row `contested` with no new tameshi text; settling it needs a precedence rule between
instrument ownership and mutation-testing measurement, which neither surface states.

## Evidence (commands, exit codes)

- `git -C tameshi rev-parse HEAD` → `2227d8338c02aa9a5fd7d95c1a41b76865ad7647` (exit 0).
- `git -C tameshi merge-base --is-ancestor 3b20f07 2227d83` → exit 0.
- `git -C tameshi rev-parse 3b20f07:corpus/knowledge/fleet-kill-rate-ledger.md 2227d83:…` → both
  `bd6aae4e8d4afed21b2645dcb0e35af7b1648e33` (exit 0).
- `git -C tameshi diff --stat 3b20f07 2227d83 -- . ':(exclude).ufo'` → 17 files, 1284 insertions,
  34 deletions (exit 0).
- `git -C tameshi show 3b20f07:corpus/knowledge/fleet-kill-rate-ledger.md | sed -n '118,140p'` → the
  125-130 boundary note quoted above (exit 0).
- `grep -c prompt tameshi/SKILL.md` → `0` (exit 1); `sed -n '862,868p;1541,1556p;1684,1694p'`
  tameshi/SKILL.md → read-only, no-rerun, no-sibling-gate quotes (exit 0).
- `sed -n '12,20p;27,36p' tameshi/PROVINCE.md` → refuses and Core quotes (exit 0).
- `git -C kotoba rev-parse HEAD` → `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` (exit 0).
- `git -C kotoba show f3046…:PROVINCE.md | sed -n '28,60p'` → line 55 tameshi row, verbatim (exit 0).
- `git -C kotoba show a5adc146:PROVINCE.md | grep -n "tameshi —"` → `32:` (exit 0).
- `git -C kotoba status --porcelain PROVINCE.md SKILL.md` → empty (exit 0); working tree matches the
  commit for both files.
- `sed -n '1,16p' kotoba/SKILL.md | grep -c tameshi` → `0` (exit 1); kotoba's description does not
  name tameshi.
- `grep -rn "kotoba" tameshi/SKILL.md tameshi/PROVINCE.md tameshi/corpus/` → 3 hits, all the ledger
  sighting/boundary lines; `grep -n "kotoba\|SKILL.md"` over the round-25/26 lessons and the two new
  notes → 2 hits, both tameshi's own SKILL.md (exit 0).

## Unresolved

- Whether kagi's `checklist-run.sh` counts as a "kotoba-core instrument" under (b): depends on a
  precedence rule neither lane states.
- kagi's own scope surface was not read at a pin: the round-8 pin `7e5ec98b9e1d0afa` and kagi HEAD
  `fecee87` are quoted from tameshi's committed note, not re-verified; whether the tip's round-27
  commits (`2227d83`) had landed when kotoba's census pinned tameshi at `3b20f07` is also open — the
  census records only its own pin.
