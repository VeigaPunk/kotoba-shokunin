# LeverGuard — round-51 C2 counter build seat (patch3)

Result: `verifiers/check_overlap_levers.py` rebuilt against lane HEAD
`59903b2` per follow-up 2 + addenda 1–6, with in-step floor bump. `--self-test`
passes 51 of 51 assertions (exit 0); `--rev 43ca0bfb…` prints
`overlap levers backed 0 of 7 clients` (exit 1); the floors guard passes 12/12
(`overlap_levers observed=51 floor=50`, exit 0); the 14 MutLeverGuard survivor
mutants are all killed alone (each re-run against the new suite exits 1), and
the added CriticC2Landed worlds w1–w5 (w2d positive) hold. Patch:
`/fast/scratch/hyaku/kotoba-r51/build/LeverGuard/patch3.diff` (865 lines,
three files, against 59903b2: check_overlap_levers.py, check_assertion_floors.py,
floors-registry.json).

## What changed in this patch

Falsify follow-up 2 (MutLeverGuard m01–m18): every survivor gets an isolated arm —
section scoping (outside-section table), comment stripping (comment-hidden table
inside the section), header-name equality (wrong header rejected), held-by/effect/
kind/tier/cap/reviewed-list pinned literals, used-by bare-filename fallback kept
(positive arm), duplicate-source-row fixture fixed (trailing newline removed so
the duplicates gate is the deciding check), description filter given its own
decision path (term injected into the reviewed set), pinned clients literal, and a
temp-repo two-commit `--rev` reader arm. All 14 seat mutants re-run against the
new suite exit 1.

L1 addenda 1–6:
- effect vocabulary gains `removed in a scope`; opencode drops `deny`; Codex
  drops `enabled = false`; Copilot CLI drops `ignoredSkillsLocations`; Claude
  drops `disable-model-invocation: true` (per-client reviewed page prefixes added).
- REC page prefixes: row URL must be the reviewed page (`.md`/sub-path
  tolerated): SDK skills, CLI cli-command-reference, VS Code agent-skills,
  Claude skills, opencode skills, Gemini skills, Codex build-skills or
  developers.openai.com/codex/skills.
- Gate record = id under `### Admitted` inside `## Gate` only.
- Section ends at any level-1/2 heading; ``` and ~~~ fences at up to three
  leading spaces are skipped; table rows indented 4+ spaces are refused.
- Entry table gets the same comment/fence stripping before parsing.
- Quote cell: text between first `"` and last `"` before the location; `\|`
  unescaped; `|` tokens count toward the 25-word cap; live-page match after
  whitespace/emphasis/tag normalization (escaped-pipe arm included).
- REVIEWED_LEVERS now carries reviewed (held-by, effect) labels per term; the
  SKILL.md row's held-by/effect must equal them; swapped labels lose the client
  (arm added).

Self-test assertion count: 51 (control 1, pinned literals 7, original mutants 9,
fix mutants 8, worlds A–D 4, survivor arms 6, inner-quote arm 1, escaped-pipe
arms 4, deny world 1, swapped labels 1, tier-B 1, w1–w5 6).

## Verified behavior (commands with exit codes, clone at 59903b2)

- `python3 -B verifiers/check_overlap_levers.py --self-test` → `0 failures` /
  `51 assertions`, exit 0.
- `python3 -B verifiers/check_overlap_levers.py --rev 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`
  → `overlap levers backed 0 of 7 clients`, exit 1.
- `python3 -B verifiers/check_assertion_floors.py` → 12 PASS lines
  (`overlap_levers observed=51 floor=50`), exit 0; `--self-test` 150 assertions,
  exit 0.
- Mutant proof: 14 files (`mutproof/m01.py…m18.py`) each = the new script with
  the seat's single defect; each `--self-test` exits 1 (recorded in
  `/tmp/mutant_exits`: m01–m18 all 1).
- End-state consistency: after the content switches the L1 describes (CLI →
  `disable-model-invocation` with the escaped-pipe row; Claude → the `:393`
  quote; opencode → `opencode/autoinvoke`; labels per the reviewed map), a
  file-backed world prints BACKED ×7, `overlap levers backed 7 of 7 clients`,
  exit 0. Current HEAD content still carries the three removed terms, so the
  unswitched HEAD prints `backed 4 of 7` — expected until the Src content seats
  land the switches.

## Notes for the integrator

- The three removed terms and the CLI map are pinned literals; content seats must
  switch to the listed terms/quotes for 7/7 (the switch-world run confirms the
  end state).
- The reviewed label map is the semantic judgment frozen in code; the statement
  must present the (held-by, effect) labels as reviewer judgment.
- `--fetch` behavior unchanged; quotes with `|` or inner double quotes match live
  pages after normalization (escaped-pipe arm covers it).
- No tools installed; no labrat; no lane writes except this report. Patch3
  supersedes patch2.diff and patch.diff.

## Evidence

`git -C /fast/scratch/hyaku/kotoba-r51/build/LeverGuard/lane3 diff
59903b2637689739a5b9901956301da72d0effe1 >
/fast/scratch/hyaku/kotoba-r51/build/LeverGuard/patch3.diff` (exit 0), 865
lines, three files: check_overlap_levers.py (542 changed lines),
check_assertion_floors.py (8), floors-registry.json (2). sha256
`d0253cec…`.
