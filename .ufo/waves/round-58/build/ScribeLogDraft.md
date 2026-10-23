Result: DONE — drafted the Round-58 LOG entry skeleton with frozen evidence, planned dispositions, and explicit placeholders for the two current-revision measurements.

## Behavior
Prepared a verbatim proposed LOG entry below. It distinguishes frozen census facts and observed control evidence from the unfinished current-revision C1 measurement and C2 record-only sweep. The C2 withdrawal is explicit; no C2 claim is stated.

## Gates
- C1 frozen predicate: `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` exits 0 iff F >= 4 and G >= 3 (plan `:69-71`; counter `verifiers/check_command_files.py:208-213`). The six-of-seven eligible census and targets were frozen after Q45 census (`plans/round-58.md:52-71`; counter `:33-42`).
- C2 was withdrawn before data after `CtlC2SourceGrep` met the frozen predicate with a self-source text check (`plans/round-58.md:86-95`; `.ufo/waves/round-58/controls/CtlC2SourceGrep.md:1-15`). The routed behavioural-arm repair remains defect work; `check_sweep_mutants.py` is record-only, never a C2 claim (`plans/round-58.md:75-97`).

## Touched surfaces
Only this assigned report was written: `.ufo/waves/round-58/build/ScribeLogDraft.md`. `LOG.md` and product files were not edited.

## Out of scope and verification
No shell command, counter, test, build, formatter, or source-fetch command was run by this seat; no tool was installed. The two counter commands below are draft text for the L1's final revision, not execution evidence. No landing hash, final measurement, or completed build-wave disposition is asserted beyond the frozen plan.

## Findings and provenance
- Round-57 style and precedent: `LOG.md:2488-2503`. Round-57 closure says M68 / `A3MutCorrectionSweep` had 7 of 11 mutants survive and routes the arms to round 58: `corpus/lessons/round-57-verifier-spotcheck.md:208-218`; the Round-57 LOG's corresponding record is `LOG.md:2500-2502`.
- Census and held ground: `plans/round-58.md:52-71`; frozen counter spec `verifiers/check_command_files.py:33-42,104-115`. Six of seven clients are eligible; `.codex/prompts` and `.github/prompts` each have one base hit; `.claude/commands`, `.gemini/commands`, `.cursor/commands`, and `.opencode/commands` have zero base hits; Copilot CLI's shared Claude Code path is disqualified by E5.
- Frontier motivation: `corpus/README.md:150-159` records the Round-57 plugin and command-extraction frontiers; `plans/round-58.md:24-30` identifies custom command files as a different frontier area.
- C1 controls: do-nothing `CtlC1DoNothing.md:1-5`, junk `CtlC1Junk.md:1-5`, and off-topic `CtlC1OffTopic.md:1-5` did not reach the predicate. Fabricated quotations had B=6/6 without a fetch but fetched F=0, K=6, G=0, exit 1 (`CtlC1Fabricated.md:1-7,20-25`). Shared-label worlds stayed below target; the reported false Copilot attribution was F=1, K=1, G=0 (`CtlC1SharedLabel.md:1,21-30`).
- C2 control evidence: `CtlC2SourceGrep.md:1-15`; it met the predicate via source-text checks before behavioral arms, so Erratum 1 withdrew C2 (`plans/round-58.md:86-95`). Frozen expected base record is 4 of 11 mutants killed, 5 of 5 equivalents surviving, exit 1 (plan `:83-85`; task context).
- Routed dispositions reproduced from `plans/round-58.md:9-20`; landing was not verified by this seat: R1 planned re-label `check_infoless_fences.py` as a probe with the withdrawal reason; R2 planned append-only README correction naming S086–S088; R3 planned behavioural-arm repair in `check_correction_sweep.py` as defect work despite C2 withdrawal; R4 plan adds a successful-`main()` arm to `check_plugin_manifests.py` self-test, and the new C1 counter's frozen spec includes one from birth; R5 planned correction of the lowercase dead paths at `SKILL.md:514-515`; R6 the census was frozen before targets; R7 C2 redesign carried, not attempted, and the plan requires the kill-by-PID bound in every wave context plus a grep of the `context` field; R8 band-10 attribution at `SCORECARD.md:29` assigned to the operator, outside this lane.

## Verbatim proposed LOG entry

```markdown
## 2026-10-23 — Round 58 (hyaku campaign, attempt 1): C1 depth custom command files by client (sourced, the learning claim); C2 operability withdrawn before data

- Plan and frozen counters `3de87aad` (C1 `check_command_files.py`, C2 `check_sweep_mutants.py`; base `f56f6e19`). Q45 census preceded target freeze: 6 of 7 clients eligible (F_max = 6), with 4 eligible tokens absent from the base tree (G_max = 4); frozen targets F ≥ 4, G ≥ 3. `.codex/prompts` and `.github/prompts` each had one base hit; `.claude/commands`, `.gemini/commands`, `.cursor/commands`, and `.opencode/commands` had zero. Copilot CLI was not eligible: its command reference reads `.claude/commands/`, and a Copilot row with that token would trigger E5 and disqualify Claude Code too.
- Frontier: *Custom command files* is a new area, distinct from round 57's plugin half of *MCP/plugin instruction surfaces* and *Command extraction*. The intended coverage is documented per-client command/prompt locations and what a file sets; client execution, argument-substitution behaviour, and precedence where a skill and command share a name remain outside the claim.
- Pre-data controls: C1 do-nothing, junk, and off-topic worlds stayed below target; the shared-label control's false Copilot attribution was F=1, K=1, G=0. Fabricated quotations produced B=6 of 6 without a page read, but with `--fetch` scored F=0, K=6, G=0, exit 1. C2 `CtlC2SourceGrep` met the frozen predicate by checking its own source for mutant texts; Erratum 1 withdrew C2 before data. This is not evidence of behavioral arms.
- C1 measured: `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` → `custom command files found on the live page <measured> of <measured>; new ground <measured>`, exit <measured> (frozen predicate F ≥ 4 and G ≥ 3).
- C2 record only: prior-round M68 / `A3MutCorrectionSweep` had 7 of 11 mutants survive. The behavioural arms in `check_correction_sweep.py` remain R3 defect work, but C2 is withdrawn. `python3 -B verifiers/check_sweep_mutants.py --rev <rev>` → `sweep mutants killed <measured> of 11; equivalents survived <measured> of 5`, exit <measured>; record only, not a claim. Frozen base record: 4 of 11 killed, 5 of 5 equivalents survived, exit 1.
- Routed defects (frozen-plan dispositions; implementation status not checked by this seat): R1 — re-label `check_infoless_fences.py` as `probe` with the withdrawal reason; R2 — append a corrected README note adding S086–S088 with their row roles; R3 — repair behavioural correction-sweep arms as defect work despite C2 withdrawal; R4 — add the successful-`main()` arm to `check_plugin_manifests.py` self-test (the new C1 counter carries one from birth); R5 — correct lowercase `/home/vgpnk/projects/` paths at `SKILL.md:514-515`; R6 — record the Q45 census before target freeze; R7 — carry, not attempt, C2 redesign, and inline/grep the kill-by-PID bound in every wave context; R8 — leave band-10 attribution at `SCORECARD.md:29` with the operator.
```

## Marker inventory for the L1
Seven `<measured>` occurrences, all intentionally left for the final-revision receipts:
1. C1 live-page F.
2. C1 denominator K.
3. C1 new-ground G.
4. C1 exit code.
5. C2 record-only mutant kills K.
6. C2 record-only equivalent survivors E.
7. C2 record-only exit code.

## Artifact path
`.ufo/waves/round-58/build/ScribeLogDraft.md`