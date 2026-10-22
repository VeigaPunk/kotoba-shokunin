# RowKama — falsify report, round 49 (C1 census row `kama`)

VERDICT: FAILS for the row's classification basis (item 3) and the PROVINCE.md boundary sentence (item 5). HOLDS for the commit (item 1), the verbatim scope quote (item 2), and both mechanical cells (item 4). HOLDS-BOUNDED for the branch cell (item 1): `master` contains the pin, but the pin is no longer the tip.

Judged bytes: kotoba `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`; kama pin `c808ba07f09c4be55413d3d6516c542ab69b64f8`. Attacked: census line 70, `PROVINCE.md:44` (c48793), `.ufo/waves/round-49/build/CensusKama.md`. Axis: adjacency.

## Findings, most severe first

**F1. `adjacent` is not derivable from the rule as written (item 3).**
- Adjacent arm holds on literal text: `corpus/knowledge/cross-lane-scope.md:29` (the split), `:32` (rule), `:41`; `MINT.md:42` ("kotoba | prompt & skill craft | instruction surfaces, not services"); `.ufo/waves/round-11/advice/SiblingOverlap.md:70` (kama's own "Kotoba owns ... declared model selection in agent definitions").
- Contested arm also holds on literal text, and the row never mentions it. Contested means scope surfaces "writing or auditing other lanes' SKILL.md, prompts or AGENTS.md-class files". Committed kama text that meets that wording:
  - `SKILL.md:20-21` (current Domain bullet) scopes "baseURL values declared by consumer configs ... agent frontmatter". kotoba's own Core claims "Agent-definition ... craft" (c48793 `PROVINCE.md:13`).
  - `corpus/knowledge/consumer-registry.md:91-92` (rows 2-3) audits `agents/janitor.md:5,20-21` (prompt text "there is no fallback") and `distiller.md:5,7`.
  - `consumer-registry.md:111-112` (rows 22-23) records `kengaku-shokunin/SKILL.md:322-323` as a kama endpoint-consumer row with a verdict.
  - `consumer-registry.md:325-326` greps the opencode agent dirs and `~/.agents/` ("skills + godspeed-core + AGENTS.md").
  - `SKILL.md:94-103` (dated 2026-09-28 example) says "verify each" for the agent-file pins.
- The rule has no precedence. `none` means "neither of the above", so both arms can hold at once.
- The seat's reasons for not contested (CensusKama.md:38-44) use qualifiers the rule lacks: "craft verdict", "never writes", "builds no instrument ... quality", "owns a half". Its own fallback (CensusKama.md:42-44) would make kama `none` if a verdict were required, which contradicts the adjacent arm, since that arm needs no verdict.
- Census Limits (census lines 131-133) names this failure mode. The seat never cited `consumer-registry.md`: grep of CensusKama.md for `registry` hits only the ls-tree listing (line 57).

**F2. The seat's stated basis has two false premises (CensusKama.md:27-41).**
- (a) "kama reads agent-definition files as a *config* surface" (CensusKama.md:28, present tense). Kama's committed bytes say the files are gone: `PROVINCE.md:11` ("`agents/janitor.md:21` (file deleted)"; "Historical, no longer live pins"); `corpus/README.md:51-55` ("As of the 2026-10-14 re-census all three files are deleted or emptied"); `LOG.md:249-252` (`~/.config/opencode/agents/` "are gone"); `registry/history/DELTA.md:15-18` (janitor-agent and opencode-distiller row-absent); `registry/endpoint-consumers.tsv` holds three rows, none an agent file.
- (b) "Its only cross-lane SKILL.md touch is a host-path fact check ... (MINT.md:24)" (CensusKama.md:40-41). `MINT.md:24-27` is passive ("was also found absent") and names no actor. Rows 22-23 and the sweep at `:325-326` are cross-lane touches the seat did not cite.
- Effect: the split at `cross-lane-scope.md:29` names agent files that kama's own PROVINCE and LOG say are gone. The function split (instruction wording versus endpoint truth) still stands. The row does not say the named artifact is retired.

**F3. The PROVINCE.md boundary sentence misquotes its cited split (item 5).**
- Row (`PROVINCE.md:44` at c48793): "kotoba owns the instruction surface and its model wording, kama verifies the endpoint".
- Cited line (kama `cross-lane-scope.md:29` at c808): "**Kotoba** owns the instruction/agent surface and its model/fallback wording; **kama** owns independent verification of the target endpoint."
- Dropped: "agent" and "fallback". The fallback wording is what the cited line covers (janitor no-fallback, distiller cascade). The sentence narrows kotoba's surface.
- Holding: commit matches census line 70; cited line 29 exists and is the row; "local model serving and endpoint health" matches `SKILL.md:3` and `PROVINCE.md:3-4`.
- The guard does not read boundary text. `_check_province` (guard lines 509-550) compares lane set, classification and commit only. Mutation M3 (owner reversed) passes.

**F4. The guard passes false values in four cells (items 1, 4).**
- `check_census` reads `branch`, `names kotoba`, `arbitration` and `path` for non-emptiness only (guard lines 383-386).
- M1 (kama branch `main`, names `yes`, arbitration `yes: kumitate`) → exit 0, "rows 20 verified 20; province rows 20 matched 20".
- `plans/round-49.md:22-23` says the entry carries "whether the sibling's description carries an arbitration clause". No committed instrument checks that cell.
- The quote check works. M2 (`&` changed to `and`) → exit 1, "FAIL row 8 (census line 70) (lane kama): quote not found at SKILL.md:8 (+/-2 lines)".

**F5. Branch cell: `master` holds as ancestry only; the seat's pin evidence is stale (item 1).**
- `git -C kama rev-parse master` → `1560e4d83f42b04f40336357de6f9637eafa0f4b`, exit 0. `rev-parse HEAD` → same, exit 0. CensusKama.md:11-13 ("master = c808ba07") was true when read; it is not now.
- `git -C kama log --first-parent --format='%h %s' master` puts `c808ba0` at position 8, behind seven newer commits (1560e4d, a46a618, c0a9b02, 46be41c, fa3b62a, 5c95c8f, 46fb04b).
- The row's facts survive a re-pin. Among the classification surfaces, only SKILL.md changed after the pin (`git -C kama log --format='%h %s' c808..master -- PROVINCE.md SKILL.md corpus/knowledge/cross-lane-scope.md MINT.md registry AGENTS.md` → fa3b62a, c0a9b02). Its hunks start at old lines 185, 186, 664, 683, 867, 972, 986 (`git -C kama log -p --format='--- %h' c808..master -- SKILL.md | grep '^@@'`). None touches lines 1-31.

**F6. Evidence errors in CensusKama.md (the row's support, not the row itself).**
- "kotoba's current one-liner" (CensusKama.md:44-46) is base a5adc146 text, not current; c48793 replaced it. At a5adc146 the kama text is line 34; line 33 is kasegi (`git -C kotoba show a5adc146:PROVINCE.md | cat -n | sed -n 30,36p`, exit 0). kama's `overlap-scan.tsv:17` cites line 33: off by one.
- `grep -i -c kotoba` on MINT.md hits lines 20 and 42, not "lines 20-21". Case-sensitive `kotoba` hits in cross-lane-scope.md are lines 6, 32, 41; the seat's "13, 14, 29" are the capitalized hits.
- Owns row 2 is cited as "a historical agent file" without "(file deleted)" (PROVINCE.md:11).

## Items that hold
- Item 1, commit: `git -C kama rev-parse --verify c808ba07f09c4be55413d3d6516c542ab69b64f8^{commit}` → exit 0. `log -1` → 2026-10-22T06:38:45-03:00, "round-25: amendment 3...".
- Item 2, quote: `git -C kama show c808…:SKILL.md | cat -n | sed -n 6,10p` → line 8 is "Local model serving & endpoint health. This lane answers exactly one question:" (exact; offset 0 in the ±2 window). The quote stops at the colon. The falsifiable boundary is line 9 ("**is the thing at this baseURL the model this config believes it is, right now.**"). The cell is correct but omits the boundary question.
- Item 4, mechanical: description `SKILL.md:3` is one line (verbatim, CensusKama.md:19-21). Whole-token, case-insensitive count of each of the 20 sibling names and `kotoba` on that line: 0 for all 21. Both `names kotoba = no` and `arbitration = no` re-derive.
- Lane set: `ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l` → 21 (20 siblings + kotoba). The guard's lane-set check passes (exit 0).
- Skill file: `git -C kama ls-tree -r --name-only c808… | grep -E '(^|/)SKILL\.md$'` → `SKILL.md` only, exit 0.

## Residual risk and gaps
- Kama sweeps used `git grep` at the pin: kotoba mentions in 30 files (most under `.ufo/`); agent-config paths (`.config/opencode/agents`, `.agents/`) in 12 non-`.ufo` files (command in Evidence). A broader term sweep (agent, AGENTS, SKILL, frontmatter, prompt template over scope surfaces) matched many more files; I read its high-yield hits, not every one. I did not read `corpus/lessons/round-*-verifier-spotcheck.md` (own-lane verifier logs about kama's own dispatch prompts, outside "other lanes'") or every SCORECARD hit.
- Kotoba side: only `PROVINCE.md:44` and the census name kama in the committed tree (`git grep -n -i kama c48793 -- . ':(exclude).ufo'`).
- The contested-literal reading is my judgment; I did not establish the census author's intent.
- Kama's `tools/` and `tests/` do not reference agent files, `.agents`, AGENTS.md or SKILL.md. I did not read every tool body for writes.
- The guard's `--self-test` was not run (out of scope). The tip was not re-derived; the census pins c808.

## Fixes (for the integrator)
1. Either add a tie-break to the rule (for example: contested requires a craft verdict or write on another lane's SKILL.md, prompts or AGENTS.md-class files; endpoint-pin inventories are not contested) and record `consumer-registry.md:91-92, 111-112, 325-326` as considered; or reclassify.
2. Restore the cited split in `PROVINCE.md:44` ("instruction/agent surface and its model/fallback wording") and add the 2026-10-14 retirement marker.
3. Record the branch cell as "master (ancestor of tip)" or re-pin; add an ancestry check and content checks for `branch`, `names kotoba`, `arbitration` to the guard, or stop claiming those cells are guarded.
4. Correct CensusKama.md per F2 and F6.

## Evidence (commands, exit codes)
- `git -C kama rev-parse master` → 1560e4d…, exit 0; `git -C kama rev-parse HEAD` → 1560e4d…, exit 0.
- `git -C kama rev-parse --verify c808…^{commit}` → exit 0.
- `git -C kama log --first-parent --format='%h %s' master` → c808ba0 is 8th, exit 0.
- `git -C kama show c808…:SKILL.md | cat -n | sed -n 1,16p` → exit 0.
- `git -C kama ls-tree -r --name-only c808… | grep -E '(^|/)SKILL\.md$'` → `SKILL.md`, exit 0.
- Name loop: `grep -oiwE -- <name>` for the 20 sibling names and `kotoba` on SKILL.md:3 → 0 each.
- `git -C kama grep -l -i -E '\.config/opencode/agents|\.agents/' c808… -- . ':(exclude).ufo'` → 12 files, exit 0.
- `git -C kama grep -n -i -E 'agents/|\.agents|AGENTS\.md|SKILL\.md|opencode' c808… -- tools tests` → no output, exit 1.
- `git -C kama grep -l -i -I kotoba c808… | wc -l` → 30, exit 0.
- Scratch clone of kotoba at c48793. Guard: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → "rows 20 verified 20", "province rows 20 matched 20", exit 0.
- M1 (census-A: branch, names, arbitration mutated) → exit 0. M2 (census-B: quote `&`→`and`) → exit 1. M3 (PROVINCE-A: owner reversed) → exit 0. Copies in the scratch `mut/` directory.
- `git -C kama log --format='%h %s' c808..master -- PROVINCE.md SKILL.md corpus/knowledge/cross-lane-scope.md MINT.md registry AGENTS.md` → fa3b62a, c0a9b02, exit 0.

Scratch: `/fast/scratch/hyaku/kotoba-r49/falsify/RowKama/`. The only lane write is this report. Tooling: none installed or upgraded (git, python3 and grep were already present).
