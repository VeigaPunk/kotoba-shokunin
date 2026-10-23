# Round 58 — lessons (kotoba, hyaku campaign, attempt 1)

Plan `plans/round-58.md` (draft `8db20702`, freeze `3de87aad`, erratum 1 `a39942c9`). C1 (depth): custom command files by
client. C2 (operability) was withdrawn before data. Seat reports: `.ufo/waves/round-58/{w0,controls,build,falsify}/`.

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named)

- **S089 Claude Code** — https://code.claude.com/docs/en/slash-commands.md — accessed 2026-10-23T08:08:35Z (HTTP 200, 114,542 B, sha256 `6b070e87…`; seat `SrcClaudeCode`, census `CensusClaudeCode`) — `slash-commands.md:172`: "**Command files**: a Markdown file in `.claude/commands/` is the older format and still works."
- **S090 Codex** — https://learn.chatgpt.com/docs/custom-prompts.md — accessed 2026-10-23T08:07:59Z (HTTP 200, 3,357 B, sha256 `d6f7cf8d…`; seat `SrcCodex`, census `CensusCodex`) — `custom-prompts.md:62`: "Manage prompts by editing or deleting files under `~/.codex/prompts/`."
- **S091 VS Code** — https://code.visualstudio.com/docs/agent-customization/prompt-files.md — accessed 2026-10-23T08:08:16Z (HTTP 200, 13,729 B, sha256 `4ad1b2bc…`; seat `SrcVSCode`, census `CensusVSCode`) — `prompt-files.md:21-25` (table; pipes written `&#124;`): "that the Local harness uses for prompt files. &#124; Scope &#124; Default file location &#124; &#124;-------&#124;-----------------------&#124; &#124; Workspace &#124; `.github/prompts` folder &#124;"
- **S093 Gemini CLI** — https://geminicli.com/docs/cli/custom-commands.md — accessed 2026-10-23T08:08:24Z (HTTP 200, 12,129 B, sha256 `8f3295e8…`; seat `SrcGeminiCLI`, census `CensusGeminiCLI`) — `custom-commands.md:12-13`: "1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands are available in any project you are working on."
- **S094 Cursor** — https://cursor.com/docs/reference/deeplinks.md — accessed 2026-10-23T08:08:47Z (HTTP 200, 5,972 B, sha256 `7ceb6578…`; seat `SrcCursor`, census `CensusCursor`) — `deeplinks.md:54`: "Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory."
- **S095 opencode** — https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx — accessed 2026-10-23T08:08:26Z (HTTP 200, 7,242 B, sha256 `dda6bba0…`; seat `Srcopencode`, census `Censusopencode`) — `commands.mdx:21`: "Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`."

### Rejected (opened or built this round, not admitted)

- **C2 counter `verifiers/check_sweep_mutants.py` as a claim gate** — reject: control `CtlC2SourceGrep` (sandbox
  `c6b6f306` in `/fast/scratch/hyaku/kotoba-r58/CtlC2SourceGrep`) met the frozen predicate (`killed 11 of 11;
  equivalents survived 5 of 5`, exit 0) with a self-test that greps its own source for the published mutant texts and
  returns before any behavioural arm. C2 withdrawn by erratum 1 before data; the registry row carries `claim withdrawn r58`.
- **Copilot CLI `.claude/commands/` as its row token** — reject: the path carries Claude Code's marker and is Claude Code's
  folder; E5 would also disqualify the Claude Code row (`CensusCopilotCLI`, `SrcCopilotCLI`). The row names it in plain words.
- **Copilot CLI `com.github.copilot/commands/`** — reject: a CLI plugin namespace (no leading dot, a dot inside a non-final
  segment), not a user folder (`CensusCopilotCLI`, S028).
- **`.github/prompts/` for Copilot CLI** — reject: printed only on IDE prompt-file pages that never name Copilot CLI
  (`ScoutCopilotPrompts`); control `CtlC1SharedLabel` showed such IDE-scope text would be counted for Copilot CLI (F=1),
  so the row rule's scope judgment, not the counter, keeps it out.
- **opencode served page `https://opencode.ai/v2/docs/commands/` as the S095 URL** — reject: without `Accept:
  text/markdown` it serves HTML on which the frozen `found_on_page` returns False (`Srcopencode`); the pinned docs source
  carries the same sentence.
- **Cursor `.cursor/commands/[command].md`** — reject: printed only on a changelog page (`changelog/1-6`), which the row rule
  excludes (`CensusCursor`, `SrcCursor`).

### Rows touched (old → new)

- **S028** (Copilot CLI plugin reference) — re-opened 2026-10-23T08:08:39Z (HTTP 200, 47,200 B, sha256 `d0d362cc…`,
  seat `SrcCopilotCLI`); cited by the new entry for `cli-plugin-reference.md:456` "then commands (.claude/commands/), skills
  override commands"; `used-by` unchanged (append-only registry; the citation is recorded here).

## Mistakes

M70–M73 are the round-57 spot-check routes R1, R4, R5 and R3, drafted by seat `ScribeMistakes`
(`.ufo/waves/round-58/build/ScribeMistakes.md`) and checked by the L1; M75–M77 are this round's own. (The seat's M74
draft cites a sandbox hash that does not resolve to the lane commit it names — `07c33d73ddce769d9cea2844…` versus the lane's
`07c33d73ddce769d9cea2846…` — so it is not used.)

- **M70 `withdrawn-counter-kept-as-gate`** · `verifiers/check_infoless_fences.py` remained registered as a `gate` although C2 was withdrawn after hollow controls met its frozen predicate (`corpus/lessons/round-57-verifier-spotcheck.md:92-104,203-205`) · captured-by: the round-57 non-author verifier spot-check, routed defect R1 · fix: round 58 relabels the `SKILL.md` gate-registry row as `probe` and records the withdrawal reason (`plans/round-58.md:13`) · shown able to fail: the round-57 controls `CtlC2GeneratorKeyed`, `CtlC2DoNothingJunk`, and `CtlC2CharShortcuts` each reached `120 of 120`, exit 0, and `MutC2Counter` also met the predicate; the spot-check therefore withdrew the claim while the registry still called its counter a gate (`corpus/lessons/round-57-verifier-spotcheck.md:98-104,203-205`).

- **M71 `self-test-no-successful-main-path`** · the frozen round-57 C1 v2 self-test called `main()` only with an invalid revision, which returns before the real measurement path; it tested `predicate()` directly but never the final CLI return (`.ufo/waves/round-57/a3/falsify/A3CriticScorecardCalib.md:62-70`; routed R4: `corpus/lessons/round-57-verifier-spotcheck.md:210`) · captured-by: `A3CriticScorecardCalib` M05 / the round-57 non-author spot-check R4 · fix: add a successful-main-path arm to `check_plugin_manifests.py` and give the new C1 counter one from birth (`plans/round-58.md:16`) · shown able to fail: the existing pristine `python3 -B verifiers/check_plugin_manifests.py --self-test` passed with `0 failure(s) over 235 assertions`, while the recorded AST probe found only `main(['--rev', 'not-a-hash'])`; no successful-path mutant was run, so the mutation consequence is not demonstrated here ([INFERENCE] from the unexercised path).

- **M72 `dead-lowercase-home-path`** · the round-57 `SKILL.md` Sources inventory used `/home/vgpnk/projects/`, which does not exist on the host; the capitalized `/home/vgpnk/Projects/` is the live path (`.ufo/waves/round-57/a3/falsify/A3ReviewR2R6.md:27-30`; routed R5: `corpus/lessons/round-57-verifier-spotcheck.md:211`) · captured-by: `A3ReviewR2R6` F3 · fix: correct the dead lowercase paths to the live path (`plans/round-58.md:17`; target `SKILL.md:514-515` in the plan) · shown able to fail: `ls -d /home/vgpnk/projects` produced `No such file or directory` (`A3ReviewR2R6.md:29`).

- **M73 `correction-sweep-arms-weak` (R3; C2 withdrawn)** · four new self-test arms and three registry rows still let 7 of 11 mutants survive; all three weakened declarations and all four dropped arms survived (`corpus/lessons/round-57.md:169-173`; `.ufo/waves/round-57/a3/falsify/A3MutCorrectionSweep.md:39-55`) · captured-by: the round-57 `A3MutCorrectionSweep` mutation probe, routed defect R3 / M68 · fix: add behavioral arms to `verifiers/check_correction_sweep.py` (`plans/round-58.md:75-95`); C2 is withdrawn, so `check_sweep_mutants.py` is a record only, not a claim (`plans/round-58.md:86-95`) · shown able to fail: in the round-57 probe, each weakened-declaration mutant and dropped-arm mutant still let `--self-test` exit 0; the latter also reduced the assertion count from 18 to 17 (`A3MutCorrectionSweep.md:27-29,46-53`).

- **M75 `fixed-equivalent-set-is-a-label`** (the mined mistake) · C2's frozen counter judged discrimination by a FIXED,
  published set of five equivalent rewrites (`.ufo/waves/round-58/sweep-mutants.json`); a self-test that reads its own
  source, canonicalises exactly those two regex rewrites and checks the eleven mutant texts met the predicate
  (`controls/CtlC2SourceGrep.md`) · captured-by: the phase-4 pre-freeze control wave (Q37 class: a shortcut keyed on
  fixture labels) · fix: C2 withdrawn before data (erratum 1); redesign input `build/CriticC2Redesign.md`
  (measurement-time generated equivalents, parent-owned counts) · shown able to fail: the receipt above prints `killed 11
  of 11; equivalents survived 5 of 5`, exit 0 on the shortcut world and `4 of 11`, exit 1 on the base.
- **M76 `context-stale-after-freeze`** · the L1 wrote the control-wave context saying the C1 targets were still `None`
  after committing them as 4 and 3 at `3de87aad` (`.ufo/waves/round-58/controls-call.json`); five control seats reported the
  mismatch and scored the committed bytes · captured-by: the seats (each re-read the counter at the named revision) ·
  fix: a context names values by reading them from the committed file, never from the plan draft. Shown able to fail:
  `jq -r .context .ufo/waves/round-58/controls-call.json | grep -c 'still None'` prints 1.
- **M77 `routed-fix-premise-false`** · the plan routed R1 as "re-labelled `probe`" (`plans/round-58.md:13`), but
  `verifiers/check_gate_registry.py` rejects a `probe` row for a script with `1=failed` and a `--self-test` handler
  (`ExecR1Registry`: 30 of 32 under that relabel) · captured-by: the executor seat · fix: the in-cell `claim withdrawn`
  annotation (32 of 32); same class as M69 — check a routed fix against the gate that judges it before writing it into a
  plan.
