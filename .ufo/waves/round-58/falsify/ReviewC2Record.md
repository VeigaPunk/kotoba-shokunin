Result: HOLDS — at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` nothing presents the 11-of-11 R3 measurement as a claim or as proof of behavioural arms; every hit is labelled withdrawal reason, "record only, not a claim", a control-measurement artifact, or a counter self-test fixture, and the record itself reproduces exactly as recorded.

Scope: how withdrawn C2 is recorded at `46b4a706` — plan erratum, registry annotation, lesson M75 (+M73), Q46/Q47; plus a full-tree sweep for `11 of 11`/`killed 11 of 11` at that rev and independent re-runs of the counter in my own sandbox clone `/fast/scratch/hyaku/kotoba-r58/ReviewC2Record` (cloned from the lane, checked out at `3de87aad`; control world `c6b6f306` fetched from `/fast/scratch/hyaku/kotoba-r58/CtlC2SourceGrep`). Sandbox commit cited as sandbox `c6b6f306bb21e64be05a530bf3c01fd78577a9c0` (fetched into `/fast/scratch/hyaku/kotoba-r58/ReviewC2Record`). `date -u` at clone: `Fri 23 Oct 2026 08:34:43 AM UTC`.

## Independent re-runs (frozen counter `check_sweep_mutants.py` sha256 `f7664401…`, matches the control's pinned hash)

All runs `TMPDIR=$PWD/.my-tmp timeout 900 python3 -B verifiers/check_sweep_mutants.py --rev <rev>` from `/fast/scratch/hyaku/kotoba-r58/ReviewC2Record`:

| --rev | observed | exit | expected per the record | match |
|---|---|---|---|---|
| `f56f6e19` (base) | `sweep mutants killed 4 of 11; equivalents survived 5 of 5` | 1 | base record 4/11 + 5/5 exit 1 (`receipts/base-receipts.txt`, plan `Expected base: K = 4, E = 5, exit 1`) | yes |
| `3de87aad` (freeze) | `4 of 11; 5 of 5` | 1 | same base record | yes |
| sandbox `c6b6f306` (CtlC2SourceGrep shortcut world) | `11 of 11; 5 of 5` | 0 | control report `:102` → withdrawal basis | yes |
| `46b4a706` (content rev, R3 arms landed) | `11 of 11; 5 of 5` | 0 | `noharm-tip.txt` @ tip + uncommitted LOG line | yes |

`check_gate_registry.py --rev 46b4a706` → `gate registry rows conformant 32 of 32 lane verifiers; phantom 0`, exit 0 — the in-cell `claim withdrawn` annotation is conformant. `git diff 3de87aad 46b4a706 -- verifiers/check_correction_sweep.py` → `1 file changed, 66 insertions(+), 0 deletions` — insertion-only as `ExecC2Arms` reported (the new `ran: list[str]`/`expected_cases`/`sorted(ran)` guard present at `check_correction_sweep.py:175,273,341`).

## Findings

No defect on the named question. The erratum's premise reproduces: a self-test that greps its own source for the frozen mutant texts meets the predicate byte-for-byte (`11/11, 5/5, exit 0`), so K/E on the frozen fixed catalogue genuinely cannot distinguish the R3 behavioural arms from a label-keyed shortcut — withdrawal is correct and the "record only" framing on every surface is warranted, not merely claimed.

### LOW-1 — "pre-freeze" is a mislabel for the control wave (cosmetic; material claim still holds)

`plans/round-58.md:87` ("The pre-freeze control `CtlC2SourceGrep`") and `corpus/lessons/round-58.md` M75 ("the phase-4 pre-freeze control wave") call the controls pre-freeze, but the receipts could only exist after the freeze commit: `CtlC2SourceGrep.md` records the clone checking out `3de87aad` and its sandbox commit sits on top of `3de87aad`; commit order is `3de87aa` freeze (04:51Z) → `a39942c` erratum+receipts (05:07Z) → `46b4a70` content (05:20Z). The controls are **pre-data**, which is the materially correct basis for withdrawal ("C2 withdrawn before data" is everywhere accurate); "pre-freeze" is chronologically impossible as written. Related micro-deviation: the plan's two-step scheme names "freeze" as the commit carrying "control receipts"; receipts actually rode `a39942c` — still before any data, so no measurement integrity is implicated.

### INFO — `ExecC2Arms.md:1` Result line bare, but bounded by its own header

`Result: DONE — … the frozen counter now kills 11 of 11 mutants with all 5 equivalents surviving (exit 0)` reads, in isolation, like arms-proof; the same report headers the section `(C2 withdrawn; record only)` and states `:6` "measured by the frozen counter as a record, never as a claim". Any future summary that copies only the Result line would lose the bound — noted, not a defect at `46b4a706`. (Observed in passing: the landed diff is 66 insertions where the report says its patch was 51 — L1-integrated variation, insertion-only both ways; out of scope.)

## Complete sweep — every `11 of 11` hit at `46b4a706` and its label

`git grep -n "11 of 11" 46b4a706` over the full tree; `killed 11 of 11` subset listed. All labelled record/control/fixture — none a claim:

| hit | label |
|---|---|
| `plans/round-58.md:89` | quoted as the control's measured output; the withdrawal reason itself |
| `corpus/lessons/round-58.md:20` (Gate Rejected row) | "C2 withdrawn by erratum 1 before data; the registry row carries `claim withdrawn r58`" |
| `corpus/lessons/round-58.md` M75 | "the receipt above prints `killed 11 of 11; equivalents survived 5 of 5`, exit 0 on the shortcut world and `4 of 11`, exit 1 on the base" — named a shortcut artifact |
| `corpus/QUALITY.md` Q47 (`:58`) | cites `CtlC2SourceGrep` 11/11 5/5 exit 0 as the reason "the measure stays a record, never a claim" |
| `corpus/QUALITY.md` Q46 (`:57`) | the in-cell-annotation rule; cites M70/M77, `claim withdrawn r5` grep 0→2 |
| `.ufo/.../build/ExecC2Arms.md:1,114` | record line + "record, never as a claim" (`:6`) |
| `.ufo/.../build/CriticAxisFit.md:60` | control citation; `:63` "K/E cannot by itself establish behavioral repair" — the guardrail, heeded |
| `.ufo/.../build/CriticC2Redesign.md:15` | cited as the shortcut mechanism; redesign input only |
| `.ufo/.../build/ScribeQuality.md:65` | "record-only counter because C2 was withdrawn before data, not a C2 claim" |
| `.ufo/.../build/ScribeLogDraft.md:33` | record template with `<measured>` placeholders + "record only, not a claim" |
| `.ufo/.../controls/CtlC2SourceGrep.md:102` | the control run (reproduced above) |
| `.ufo/.../controls/CtlC2Snapshot.md:79` | `11/11; 0/5` exit 1 — predicate correctly rejected the snapshot shortcut |
| `.ufo/.../w0/ExecC2Counter.md:111,135,162` | counter self-test fixture runs (pre-withdrawal build artifact) |
| `verifiers/check_sweep_mutants.py:349`, `.ufo/.../w0/check_sweep_mutants.py:349` | `want = "sweep mutants killed 11 of 11; …"` — the counter's own fixture expectation, not a claim |
| `corpus/lessons/round-51.md:208` | unrelated prior-round hit (checklist 11/11 PASS) |

Requested-file breakdown: `SKILL.md` 0 hits (registry row `SKILL.md:465` carries `claim withdrawn r58 before data (plan erratum 1)`; `claim withdrawn r5` count = 2, matching Q46); `SCORECARD.md` 0 hits and no round-58 row at this rev; `LOG.md` 0 hits and no round-58 entry at this rev; `corpus/` hits only in `lessons/round-58.md`, `QUALITY.md`, `lessons/round-51.md` — all labelled above.

Out-of-rev note: the uncommitted working-tree `LOG.md`/`SCORECARD.md` round-58 drafts correctly label the 11/11 line "record only, not a claim" / "C2 withdrawn before data" — consistent with the audited records.

## Named-item verdicts

- **Plan erratum** (`plans/round-58.md:86-95`): accurate. "WITHDRAWN before any data" holds; control numbers reconcile with the reports (do-nothing/junk 4/11 5/5 exit 1 `CtlC2DoNothing.md:1`; snapshot 11/11 0/5 exit 1 `CtlC2Snapshot.md:1`; always-0 0/11 5/5 `CtlC2AllFail.md:234`; line-count 8/11 4/5 `:288`; case-count 4/11 5/5; always-1 could-not-evaluate exit 2 `:182`). Only the "pre-freeze" label (LOW-1).
- **Registry annotation** (`SKILL.md:465`): `gate` kind + in-cell `claim withdrawn r58 …` — the M77-corrected fix, conformant (32/32 verified above), matching Q46's rule and the r57 precedent at `:457`.
- **Lesson M75**: mined mistake is accurate and honestly bounded (fixed published equivalent set = a label; receipt quoted as "shown able to fail"). M73 explicitly: "C2 is withdrawn, so `check_sweep_mutants.py` is a record only, not a claim". M74 non-use is disclosed with a hash-mismatch reason.
- **Q47** (`corpus/QUALITY.md:58`): two-sided measure rule + generated-equivalents clause; cites the shortcut receipt as counter-example, consistent with everything above.

Residual risk: none blocking. If a later round's SCORECARD/round-report copies only the bare `kills 11 of 11 … exit 0` headline, the "record only" bound must travel with it (per `CriticAxisFit.md:75` — "do not claim K = 11 proves behavioral testing").

No tools installed or updated; no lane writes beyond this report; no paid calls, no `model` parameter, no `ask`; git in the lane read-only (`--no-optional-locks`); all execution inside `/fast/scratch/hyaku/kotoba-r58/ReviewC2Record` with `timeout` caps and at most one counter run at a time.
