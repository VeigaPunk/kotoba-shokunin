# ScoutDescConsumers — consumers of the SKILL.md frontmatter `description` (replacement C2)

Seat: scout, read-only. Base `072048fa8e8a52c707d25f7079772fa317244eb7`. Lane checkout at `ac8fc59` (spec commits only; `git diff 072048f HEAD -- SKILL.md verifiers PROVINCE.md corpus/knowledge/sibling-overlap-census-round49.md` is empty).
Sandbox: fleet-shaped `/tmp/k73fleet-ScoutDescConsumers.*` (symlinks + `git clone --shared` of the lane; trial commits only inside it; deleted at the end). Drafts: `.ufo/waves/round-73/w1/build/ScoutDescConsumers/` (`c1..c4.frontmatter.txt`, `gate_matrix.tsv`, `gate_matrix_runner.py`, `candidate_builder_c1_c3.py`).

## Verdict

1. Only **two gates read the description text** and both stay green on all four trial descriptions: `verify_skill_checklist.py` (five `trigger.*` boxes) and `check_sibling_census.py --skill`. 44 gate invocations at base and at each trial commit: **no exit code moved and no output line moved except the two printed description lengths** (plus host drift, below).
2. Keeping the frontmatter at 18 lines keeps every citation of a line **after line 18** valid, but it does **not** protect citations of lines **inside** the frontmatter: 31 bare `SKILL.md:N` tokens cite only lines ≤ 18. The only way to keep those pointing at the same text is to change **lines 4-5 only** and leave lines 6-18 byte-identical (candidate **c4**, below). c1-c3 re-wrap lines 4-18.
3. The old sentence cannot simply be prepended with a short one: keeping the old 151-char sentence's content after a new first sentence gives 1,058 (c1 first draft) / 1,046 (c2 first draft) characters, over the 1,024 cap. The trial descriptions drop content (listed per candidate).
4. Plan attack: the counter's R1 boundary (`. ` or `: ` + uppercase) is **not** the truncator the claim cites (`^.*?[.!?](?=\s|$)`, sentence kept if ≥ 40). Details in "Counter-spec findings".

## Consumer table

| consumer | what it reads | effect of a rewrite | observed |
|---|---|---|---|
| `verifiers/verify_skill_checklist.py` `trigger.frontmatter_parses`, `trigger.name_directory`, `trigger.literal_trigger_string` (needs literal `Triggers:`), `trigger.anti_trigger_clause` (vocabulary search AFTER all quoted spans are stripped, so a quoted trigger cannot satisfy or hide it), `trigger.no_xml_tag` (`<`/`>`) — code at `verify_skill_checklist.py:1385-1480` | parsed `name`, `description` | PASS at base and c1-c4; only the `description N chars` text moves (1019 → 1011/1023/1016/1003) | `PASS trigger.frontmatter_parses … description 1003 chars` (c4) |
| `verifiers/checklist-baseline.json` hashes | `text_sha256` of the 45 **body** checklist boxes (normalization: first line minus `- [ ]` marker, continuations joined) | not touched: frontmatter has no `- [ ]` lines | file keys: `schema,file,normalization,boxes,box_total`; gate green on c1-c4 |
| `verifiers/check_sibling_census.py --skill SKILL.md` (`description_of` at :380, `skill_description_failures` at :502; CLAUSE_SPLIT at :440; markers at :432) | description folded; G1 clause binding (each of the 9 `adjacent` lanes in a clause with `owns/own/owned/route/routes/routing/NOT/see above/as above/see also`), G4 `1..1024` chars | green only if the Sibling-boundary clauses survive and the sum stays ≤ 1024; clauses split at `;` and at `[.!?]` + whitespace + capital | `skill description names 9 of 9 non-none lanes` on base, c1-c4; length line 1019 → 1011/1023/1016/1003 |
| same gate, negative worlds (run by me) | `--skill` file in scratch | description cut to the first sentence: `names 0 of 9 … length 60 of 1024` exit 1; 30 chars of padding: `length 1034 of 1024` exit 1; removing `NOT` from the kotodama clause: still exit 0 (`owns` is also a marker) | `/tmp` scratch, exit codes recorded in this report only |
| `verifiers/check_description_thresholds.py` | the `### Description thresholds by client` **body** table in SKILL.md | none | exit 0 at base and c1-c4, identical output |
| `verifiers/check_province_core.py` | PROVINCE.md Core lines (no `SKILL.md` read; `grep -nE "SKILL|description"` finds only an argparse string) | none | exit 0, identical |
| `verifiers/check_gate_registry.py` | `## Gate registry` rows of SKILL.md | none | exit 0, identical |
| `check_overlap_levers.py`, `check_author_rules.py`, `check_correction_sweep.py`, `check_skill_precedence.py`, `check_instruction_authority.py`, `check_alwayson_boxes.py`, `check_routed_repairs{,_v2}.py`, `check_r63/r64_routed_repairs.py`, `check_callee_rename.py`, `check_mcp_instructions.py`, `check_explicit_invocation.py`, `check_skill_evals_v2.py`, `check_opencode_repin.py`, `check_substrate_repin_v2.py`, `check_sweep_mutants.py`, `check_gate_finding_delta.py --base 072048f --head <trial>`, `box_proof_case_deletion.py`, `verify_surfaces.py`, `check_substrate_pins.py` | body sections / other files | none | exit 0 on base and c1-c4 |
| `check_could_not_evaluate.py` (alone; contention made it time out in the 4-way matrix) | spawns the gates above on fixtures | none | `probes honoured 29 of 29; controls held 13 of 13; red anchors held 12 of 13` at base, c3, c4 (only the `measured <rev>` line differs); its own exit status not captured (the `echo exit=$?` line did not land in the log; unobserved) |
| `compare_harness_independent.py` | omp catalogue, not the lane's own file | none | exit 2 at base alone in 94 s; TIMEOUT 120 s in the c-runs (contention); not re-run alone for c-revs; no frontmatter read found |
| red at base for sandbox reasons (identical output at c1-c4): `r66 r67 r68 r69 r69v2 client_trust command_files hook_files plugin_manifests scoped_rules scoped_v31 scoped_v32 skill_evals sources_append_only corpus_integrity corpus_independent dispatch_prompts harness_claims` | `--fetch`-needing, host- or time-dependent | none | same exit code at base and c1-c4; `diff` of normalised output shows only host drift (below) |
| `verify_corpus_integrity.py:75` comment, `check_agent_definitions.py:1076` | comment citing `SKILL.md:588`; fixture string `b0b7140b:SKILL.md:2` | none (a comment and a grep-count fixture) | read |
| `verifiers/fixtures/compare-harness-independent/*/independent.json` `"fixture.derived.18": 1019` | synthetic counter 1..24 around 1019 | none: the number is a fixture counter, not the description length | `sed -n 40,56p` shows `1008…1024` ascending |
| `corpus/knowledge/render-mechanism-round7.md:21-23` | quotes the round-7 description (756 chars) | historic, pinned | no edit |
| `corpus/knowledge/sibling-description-rewrites-round8.md:51` | quotes the 814-char description, ellipsis branch | historic | no edit |
| `corpus/knowledge/sibling-overlap-census-round49.md:51` (`SKILL.md:10-12` at `a5adc146`), `:316` (`1,019 of 1,024`) | pinned-commit citation + a number | historic; census gate re-derives from pinned sibling commits, not from kotoba's live line numbers | gate green |
| `PROVINCE.md:57,59` (`SKILL.md:10-12` at `f3046466`) | pinned commit | historic by construction (names the commit) | no edit; gate green |
| `corpus/lessons/round-50.md:156`, `round-67-verifier-spotcheck.md:71`, `round-68.md:127` | state `1,019` | append-only records | no edit |
| `README.md`, `SHONEN.md`, `SCORECARD.md` | `README.md` does not quote the description (`grep -nE "frontmatter|description" README.md` empty); `SCORECARD.md:34` describes the round-50 adjacency claim | none | read |

## `SKILL.md:<line>` citations in the lane (`grep -rnoE "[A-Za-z0-9_./-]*SKILL\.md:[0-9]+…" -I . --exclude-dir=.git --exclude-dir=.ufo --exclude-dir=__pycache__`)

- 151 tokens in total; 37 carry a path prefix (sibling lanes' files: `kagi-shokunin/SKILL.md:3`, `../kumitate-shokunin/SKILL.md:…`, `sekhmet-l3/…`) and are not this file.
- **114 bare tokens in 46 files cite this file.** 31 cite only lines ≤ 18; **83 cite at least one line after line 18** (36 files: corpus 54, plans 10, LOG.md 9, SCORECARD.md 5, verifiers 2, considerthese 2, SHONEN.md 1). Of the 83: 8 name a line beyond the live 568-line end (e.g. `:600`, `:604`, `:596`; already dead), 75 land within the live file.
- Of the 83, 23 sit on a line that also carries a commit sha (pinned); 60 do not. The 60 are almost all records (lessons, plans, LOG) written when the file was longer; the only non-record ones are `SCORECARD.md:28,31,32,253`, `SHONEN.md:6`, `verifiers/check_sibling_census.py:280` (docstring example `SKILL.md:42`) and `verifiers/verify_corpus_integrity.py:75` (`SKILL.md:588`, a recorded dead path).
- A frontmatter kept at exactly 18 lines (`git diff --numstat 072048f <trial> -- SKILL.md` must show equal added/deleted: c1 `14 14`, c2 `15 15`, c3 `15 15`, c4 `2 2`) leaves all 83 after-18 tokens untouched. **No gate reads their line content**: `trigger.citation_resolves` / `governance.citation_resolves` check that the token resolves (path exists), and both stay PASS.
- **Citations of lines inside the frontmatter (the real exposure).** Present-tense with no commit pin: `corpus/knowledge/erratum-absorption-round62.md:39` and `corpus/lessons/round-62.md:43` (`SKILL.md:14`: "tameshi owns the fixture and mutation method"). Already stale before this round and recorded as such: `corpus/lessons/round-46.md:31` (`:15`), `round-47.md:21` (`:15`, "the token sat on `:14`"), `considerthese/2026-10-20.md:56`, `2026-10-21.md:29,53` (`:14`, the `<skills>` token, long gone), `considerthese/2026-10-22.md:25` (`:6-7`, `:14-17`). Pinned: `PROVINCE.md:57,59`, `sibling-overlap-census-round49.md:51`, `round-49-verifier-spotcheck.md:79,176` (`SKILL.md:10-12` at a commit); `round-50-verifier-spotcheck.md:93,106` (`:9-17`, `:16-17` at `2abd290`).
- Candidate c4 (lines 6-18 byte-identical, `python3` check `ls[5:18]==new[5:18]` printed `True`) keeps `:14`, `:10-12`, `:14-17`, `:9-17`, `:16-17` pointing at the same text. c1-c3 re-wrap lines 4-18, so `:14`, `:10-12` point at other text; the two unpinned present-tense ones (`erratum-absorption-round62.md:39`, `lessons/round-62.md:43`) would then mis-point — they are append-only records, but a correction note would be needed.

## Three trial candidates (+ one) — first sentence, lengths

Description folded; lengths from `python3` over the committed trial `SKILL.md` (sandbox branches c1..c4; frontmatter lines 1-19 kept). The first sentence is counted with its terminating period (the base's 151 includes it).

| id | first sentence | chars | quoted trigger (in `Triggers:`) | whole words | description length | what the rest loses | frontmatter lines |
|---|---|---|---|---|---|---|---|
| c1 | `Skill and prompt craft: "write a skill", "audit this skill".` | 60 | `"write a skill"`, `"audit this skill"` | `skill`, `prompt` (lowercase) | 1,011 | second sentence becomes `Audits and rewrites SKILL.md, AGENTS.md and dispatch prompts for trigger fidelity.`: drops "writes", "system prompts", "decision density" | 18 (numstat 14/14) |
| c2 | `Audit or write a skill or prompt: "skill file", "write a skill".` | 64 | `"skill file"`, `"write a skill"` | `skill`, `prompt` | 1,023 | `Audits and rewrites SKILL.md, AGENTS.md, dispatch and system prompts for trigger fidelity.`: drops "decision density" | 18 (15/15) |
| c3 | `Write and audit skill and prompt files: "SKILL.md", dispatch prompts, AGENTS.md.` | 80 | `"SKILL.md"` | `skill`, `prompt` | 1,016 | `Audits and rewrites them for trigger fidelity and decision density.`: keeps density, drops "system prompts" | 18 (15/15) |
| c4 | `Skill and prompt craft: "write a skill", "audit this skill".` + line 5 `Audits, writes, rewrites SKILL.md / AGENTS.md / dispatch & system prompts.` | 60 | `"write a skill"`, `"audit this skill"` | `skill`, `prompt` | 1,003 | only lines 4-5 change; drops "trigger fidelity and decision density" from the old sentence; lines 6-18 byte-identical | 18 (numstat 2/2) |

Real truncator (python port of `previewSkillDescription`; first `[.!?]`+whitespace inside the first 99 characters, ≥ 40 kept; the port reproduces the base render `Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts /…` (94 chars) recorded in `sibling-description-rewrites-round8.md:51`): c1 and c4 render `Skill and prompt craft: "write a skill", "audit this skill".` (60); c2 renders its 64-char sentence; c3 renders its 80-char sentence. All four render without ellipsis and carry a quoted trigger.

Case note: the base's `Prompt & skill craft` carries a capital `Prompt`. Each candidate has lowercase `skill` and lowercase `prompt` inside the first 99 characters, so R2 holds whether the counter's whole-word match is case-sensitive or not. (An earlier c1 with `Prompt and skill craft` held `Prompt` only; I replaced it.)

## Gates that stay green (all four trials), and what moved

Matrix: `.ufo/waves/round-73/w1/build/ScoutDescConsumers/gate_matrix.tsv` (44 gate invocations; base, c1, c2, c3 full; c4 all except `could_not_evaluate` and `compare_harness_independent`, run alone as noted above). Runner: 4 concurrent processes, 120 s each, `python3 -B verifiers/<gate>` from the sandbox at the trial checkout, `--rev <trial sha>` where the gate takes one.

Green at base and unchanged on c1-c4 (exit 0): `verify_skill_checklist`, `check_sibling_census --skill`, `check_description_thresholds`, `check_province_core`, `check_gate_registry`, `check_overlap_levers`, `check_author_rules`, `check_correction_sweep`, `check_skill_precedence`, `check_instruction_authority`, `check_alwayson_boxes`, `check_routed_repairs`, `check_routed_repairs_v2`, `check_r63`, `check_r64`, `check_callee_rename`, `check_mcp_instructions`, `check_explicit_invocation`, `check_skill_evals_v2`, `check_opencode_repin`, `check_substrate_repin_v2`, `check_sweep_mutants`, `check_gate_finding_delta`, `box_proof_case_deletion`, `verify_surfaces`, `check_substrate_pins`.
Red at base for reasons independent of the description (same exit code and same normalised output on c1-c4): the `--fetch`/host-dependent list in the table.
Moved: two printed lengths only (`description N chars` in `trigger.frontmatter_parses`; `skill description length N of 1024` in the census gate).
Host drift seen, not the description: `verify_harness_claims` "newest catalogue" timestamp / session-file count moved between runs; `verify_corpus_integrity` printed `unresolvable=3` in the first base run and `0` in later runs, and a second base run (same sandbox, later) also printed `unresolvable=0` — fleet commits landing between runs.

## Counter-spec findings (attacks on the frozen predicate; do not reinterpret, fix the counter's reading before data)

1. **R1 boundary is not the truncator's.** Addendum: boundary = `. ` or `: ` followed by an uppercase letter. Truncator (`corpus/knowledge/render-mechanism-round7.md`, `SKILL.md:535`): `^.*?[.!?](?=\s|$)` over the first 99 chars, kept if ≥ 40. A colon is no boundary in the router; `!` and `?` are; a capital after the period is not required. The base reads 151 under both, so the do-nothing control is unaffected. A world with `Prompt craft: Audits …` is cut at the colon (12 chars) by the counter and not by the router. Decide the rule in the counter docstring and print both.
2. **Terminator inclusion:** 151 (base) includes the period; state it in the docstring (±1 matters at the 40 and 99 edges).
3. **Case of `skill`/`prompt` in R2** is unspecified; the candidates above hold under either reading. A shortcut world with `Prompt` capital only discriminates.
4. **Description cap**: the 1,024 cap is hit before any other constraint; any candidate that keeps the old 151-char sentence's body and adds a ≥ 60-char sentence is over by ~34-49 characters (observed: 1,058 and 1,046 on the first c1/c2 drafts).
5. R3 passes with only `names 9 of 9` + length; it cannot see a change of the Triggers list or the Anti-triggers clause. The counter prints the first sentence but not the Triggers list; a trial that deletes the Triggers list passes R3 unless the census clause binding fires (neg1 shows only a cut-to-first-sentence world fails R3).

## Must-fix list (L1)

1. Pick **c4's shape** (replace lines 4-5 only) or accept re-wrapped lines 4-18; if the latter, append correction notes for the two unpinned present-tense `SKILL.md:14` citations (`corpus/knowledge/erratum-absorption-round62.md:39`, `corpus/lessons/round-62.md:43`), do not edit them.
2. Keep the description ≤ 1,024 characters with the whole old second half intact (c4 leaves 21 characters of headroom; c2 only 1).
3. Do not touch `PROVINCE.md`, the census doc, the round-50/67/68 lessons: their `1,019`/`SKILL.md:10-12` strings are commit-pinned records; append a new dated line if the new numbers must be recorded.
4. Fix the counter's R1 boundary and terminator wording and the R2 case rule before freeze 2 (findings 1-3).
5. Re-run `check_sibling_census.py … --skill SKILL.md` and `verify_skill_checklist.py` on the landed tree; they are the only two gates that read the text.

## Tools / state

- No installs. Scratch: `/tmp/k73-scd-*`, `/tmp/k73fleet-ScoutDescConsumers.*`, `/tmp/k73-cites.txt`, gate-created `/tmp/kotoba-r56-cne-runs-{57pewtcc,edabqfos,7112jdka}` — deleted at the end. Fleet repo, lane files and lane index untouched (git writes only inside the `--shared` clone).
- Unobserved: exit status of `check_could_not_evaluate.py` run alone; `compare_harness_independent.py` on c-revs alone; `check_assertion_floors.py`, `check_tip_battery.py`, and any gate's `--self-test` (not run; none opens the lane's SKILL.md frontmatter by grep).
