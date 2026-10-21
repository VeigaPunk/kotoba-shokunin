verdict: all four SHONEN boxes stay [~]; every cited pointer resolves at BASE c61a973, but box 1 is pinned to a pre-BASE SKILL.md (055d3b9), box 2's PROTOCOL reference resolves only outside the repo, box 3's B1/B2 defects are fixed in text, and box 4's PROVINCE.md:21 goes stale when C1 lands.

# Round-47 SHONEN evidence pointers (scoped)

Lane: ShonenEvidence (leaf, no dispatch). Target: `SHONEN.md` four boxes. BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. `SHONEN.md` was NOT edited (`git status --short SHONEN.md` empty; sha256 `f012cd2f…`). No marks written.

## Box-by-box

Marks stay `[~]`: no non-author verifier exists or is planned in-round (plan `plans/round-47.md`, Waves section).

### Box 1 — SKILL.md decision tables, error patterns, checklists, cited sources (SHONEN.md:5-6)
- Strongest pointer: `.ufo/round-46/scouts/B2.md:44` (Box 1 recount). Resolves.
- Re-measured at BASE:
  - `SKILL.md:55-74` anatomy table: 7 data rows (9 `|` lines minus header and separator). Matches.
  - `SKILL.md:153-168` decision table: 5 data rows. Matches.
  - Checklist boxes: `SKILL.md:179-253`=15, `:254-299`=9, `:300-330`=9, `:331-350`=8, total 41. Matches; `verify_skill_checklist.py` `checklist.box_map_complete` also reports 41 boxes.
  - Sources (`SKILL.md:369-525`): 39 bullet entries at BASE, against B2's 38. Counterexample; the difference may be counting convention (the leading `corpus/SOURCES.md` bullet and the grouped `bailian-web-search`/`bailian-gen` line) or content drift. Not resolved.
- Pin staleness: B2 pins SKILL.md sha `0404fdc0…` (I confirmed this equals `git show 055d3b9…:SKILL.md`). At BASE SKILL.md is `c8b245b7…`, 525 lines (B2 says 521). The B2 pointer is therefore not a BASE pin.
- Round-47 change: C2 edits SKILL.md frontmatter (drops `<skills>` from `description`), so SKILL.md bytes change. The box's substance (tables, checklists, sources) is not changed by the round's claims. Effect: the pointer needs a re-pin after landing, not a re-verdict.

### Box 2 — end-to-end domain task executed and logged in LOG.md (SHONEN.md:7-8)
- Strongest pointer: `corpus/knowledge/cold-run-round11.md:1-30` (header `NON-AUTHOR cold run` at line 3; §1 reachability qualifier). Resolves.
- Counterexample on its own evidence: the file itself says the §1 sha256 gate values (`631569277d…`, `2f07179c…`) are content hashes of an untracked file, so "not independently checkable today" (file text, §1). The gate is therefore lane-attested only.
- Dangling-in-repo reference: SHONEN.md:8 says "lane evidence per PROTOCOL Promotion gates". `PROTOCOL.md` is NOT in the repo (`git ls-files | grep -i protocol` returns only `.ufo/round-37/evidence/a1-adjudication-protocol.md`). It resolves only at the fleet root: `/home/vgpnk/Projects/shokunin/PROTOCOL.md:59` (`## Promotion gates`). The governance gate's `LOG.md:311` `../PROTOCOL.md` reference depends on the same parent directory.
- LOG cross-reference: `LOG.md:287-294` and `:342` cite the round-11 cold run. Resolves.
- Round-47 change: none to the box's substance. C3 changes `corpus-integrity`'s index (adds `corpus/lessons/round-46-verifier-spotcheck.md`), so that verifier's red→green story is about a different round's artifacts; the round-11 pointer itself is unchanged.

### Box 3 — instructions executable by an agent without oral context (SHONEN.md:9-10)
- Strongest pointer: `corpus/lessons/round-8-aggregator-box3-coldrun.md:36-41` (B1, B2 rows; verdict `[~]` at :41). Resolves.
- Defects in SHONEN.md:10 ("both fixed in round 13") checked against current text:
  - B1 (newest `<skills>` recipe): fixed in text. `SKILL.md:96-97` now says "mtime order is not a selection rule". Resolved.
  - B2 (unlabelled mutating `fault_injection_corpus.sh`): fixed in text. `SKILL.md:497-500` says "**Mutating — not a smoke check**". Resolved.
  - Round-13 landing commit not checked; `LOG.md` round-13 entry not read.
- Round-47 change: no fresh non-author re-run is planned, so the box stays `[~]`. C2 and C3 change outputs of the commands that `SKILL.md` cites (`verify_skill_checklist.py` governance gate goes from FAIL to PASS if C3 lands). Re-run needed for any future mark.

### Box 4 — no cross-domain bleed; PROVINCE.md still accurate (SHONEN.md:11-12)
- Strongest pointer: `.ufo/round-46/scouts/w2-connector.md:12-22` (Adjacent list) and `PROVINCE.md` `## Adjacent`. Resolves: all 10 sibling `*-shokunin/PROVINCE.md` paths exist (chousa, kumitate, kengaku, tameshi, kotodama, mado, revenger, mori, kama, kasegi), checked from `/home/vgpnk/Projects/shokunin`.
- Every backticked `*.md|*.py|*.json|*.sh` path in `PROVINCE.md` resolves at BASE (19 paths checked).
- Staleness counterexample: `PROVINCE.md:21` (Frontier) reads "omp 18.12.3 substrate drift (surfaces 5/7, pins 1/3) and the frontmatter `description` XML-token rule". Same text in `corpus/README.md:74`. The host now has omp 18.12.5 (`omp --version` → `omp/18.12.5`, exit 0; frozen snapshot sha `fdbc8136…` matches plan). `~/.opencode/bin/opencode` is absent. So the Frontier line is already stale against the host and becomes wrong for the repo once C1 re-pins and C2 lands the XML-tag check. Integrator must update PROVINCE.md:21 and corpus/README.md:74 at landing. Not an edit I made.

## Commands run (exit codes; all read-only, `PYTHONDONTWRITEBYTECODE=1`, `python3 -B`)

Production repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`:
- `python3 -B verifiers/verify_skill_checklist.py --json` → exit 1. 9/10 PASS. Only FAIL: `governance.citation_resolves`, detail `LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve`. Saved: `ShonenEvidence.skill-checklist.json`.
- `python3 -B verifiers/verify_corpus_integrity.py --json` → exit 1. DRIFT: `corpus.index.tracked_files` observed 59 vs expected 58; `corpus.index.unindexed` observed 1 (`corpus/lessons/round-46-verifier-spotcheck.md`). Saved: `ShonenEvidence.corpus-integrity.json`.
- `python3 -B verifiers/verify_corpus_independent.py --json` → exit 1. DRIFT: `corpus.index.unindexed` = 1 (same file). Saved: `ShonenEvidence.corpus-independent.json`.
- `git status --short SHONEN.md` → empty (exit 0).
- `git ls-files | grep -i protocol` → exit 0, one hit (`.ufo/round-37/evidence/a1-adjudication-protocol.md`).
- `git show 055d3b9a3f7eb28d13452a0d26853ef4feabf2ae:SKILL.md | sha256sum` → `0404fdc0…` (equals B2 pin).

Scratch clone `/fast/scratch/kotoba-r47/ShonenEvidence/kotoba-shokunin` (detached at BASE):
- `python3 -B verifiers/verify_skill_checklist.py --self-test` → exit 0.
- Earlier run in clone dir named `lane` (not `kotoba-shokunin`): `trigger.name_directory` FAIL. Also `trigger.citation_resolves` and `governance.citation_resolves` FAIL because `../` citations resolve only from the fleet root. Counterexample: these checks are checkout-location-sensitive. Discarded; production-repo result is the one reported.

Environment: `omp --version` → `omp/18.12.5`, exit 0. `sha256sum /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5` → `fdbc8136…`. `/home/vgpnk/.opencode/bin/opencode` → No such file.

Tooling installed/updated: none.

## Artifacts written (build dir only)
- `.ufo/waves/round-47/build/ShonenEvidence.skill-checklist.json`
- `.ufo/waves/round-47/build/ShonenEvidence.corpus-integrity.json`
- `.ufo/waves/round-47/build/ShonenEvidence.corpus-independent.json`
- This report: `.ufo/waves/round-47/build/ShonenEvidence.md`

## Counterexamples and open items
1. Box 1 Sources count: 39 at BASE vs 38 in B2 (pin 055d3b9). Unresolved.
2. Box 1 pin: SKILL.md sha and line count changed since B2 (`0404fdc0…`/521 vs `c8b245b7…`/525).
3. Box 2 reference: "PROTOCOL Promotion gates" resolves only outside the repo (`/home/vgpnk/Projects/shokunin/PROTOCOL.md:59`).
4. Box 2 gate: the round-11 sha256 gate is not independently checkable (per the file's own §1 note).
5. Box 4 staleness: `PROVINCE.md:21` and `corpus/README.md:74` describe omp 18.12.3 drift; host and round-47 plan are at 18.12.5.
6. Governance gate at BASE: FAIL at `LOG.md:2111` (absent runner `.ufo/round-45/drafts/v10/post-r44-hunt.py`). Matches the plan's C3 claim; C3 should land a fail-closed erratum for this line.
7. Checkout-location dependence of `trigger.name_directory` and `citation_resolves`/`governance.citation_resolves` (see scratch run).

## Not checked
- Post-landing state of C1/C2/C3 (no patch applied in this lane; nothing re-run after changes).
- `verify_surfaces.py`, `check_substrate_pins.py`, `verify_harness_claims.py`, `compare_harness_independent.py` (outside this box scope).
- `fault_injection_corpus.sh` (mutating; not run).
- Round-13 landing that SHONEN.md:10 cites (LOG.md round-13 entry not read).
- Full content of `PROTOCOL.md` promotion gates (only the heading at :59 and :74 read).
- Full `cold-run-round11.md` and `round-8-aggregator-box3-coldrun.md` bodies beyond the cited lines.
- Whether `SHONEN.md` boxes are consistent with `SCORECARD.md` (not in target).
