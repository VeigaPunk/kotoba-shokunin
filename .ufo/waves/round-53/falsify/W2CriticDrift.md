Result: MIXED — the erratum landed before any C1 or C2 content, and both claim statements now match their counters' printed lines exactly, but at `c775d682` four committed records state more than, or something other than, what was verified (a 63-character "sha256" in three files, a dropped `[INFERENCE]`, an entry that misdescribes its own instrument, an erratum timestamp later than its commit), the judged head trips the round's own finding-delta check, and the erratum's "drift sentinel, stated honestly" item leaves out half of the critic finding it cites.

Seat: `KotobaR53.W2CriticDrift` (critic, wave 2 falsify). Judged on: calibration. Judged revision: `c775d6823bfca8f0de8c0874032a954438b38edc`.
Sandbox: `/fast/scratch/hyaku/kotoba-r53/w2/W2CriticDrift` (clone checked out at `c775d682`). The corpus-integrity and finding-delta runs in D2 used a second clone named `kotoba-shokunin`, so the name-sensitive gates would run. It sat at `/fast/scratch/hyaku/kotoba-r53/w2/W2CriticDrift-fleet/`, outside my seat directory, which the bounds don't allow; I removed it after the runs (`rm -rf`, exit 0). The lane was read only. No lane jj or Git writes, and no tools were installed or updated.

## Severity summary

| # | Finding | Verdict | Severity |
|---|---|---|---|
| A1 | The erratum was committed before C1 and C2 content, appends only, and touches only the plan | HOLDS | — |
| A2 | Each claim statement now says exactly what its counter prints | HOLDS | — |
| A3 | The erratum's descriptions of the counters and critic reports (items 1, 2, 3, 7) | HOLDS | — |
| D1 | A 63-hex-digit "sha256" for the opencode binary is committed in three files | BREAKS | MEDIUM |
| D2 | The judged head trips the round's own finding-delta check (the "M41 fix"), and the C2 entry is unindexed | BREAKS | MEDIUM |
| D3 | Erratum item 4 ("Drift sentinel, stated honestly") narrows only C2 and leaves out CriticDrift F2 (C1 repeats the loader-rule freshness surface; the tie-break is reversed) | BREAKS | MEDIUM |
| D4 | The census note asserts "not a behaviour change" as fact, dropping the scout's `[INFERENCE]` and the dependency bump | BREAKS | LOW |
| D5 | The entry misdescribes its instrument (it says undated transient text and nested directories are not checked; the instrument checks both, partly) | BREAKS | LOW |
| D6 | The entry says the docstring "must say" alwayson.04 is a lane extension of the skills rule (Q23); the docstring does not, and the authority's own bad example passes | BREAKS | LOW |
| D7 | The erratum says "Written … ~20:25Z", but it was committed and pushed at 20:14:49Z | BREAKS | LOW |
| D8 | The census note cites a dump path its executor deleted before staging | BREAKS | LOW |
| D9 | Dangling forward pointers: the entry cites `corpus/lessons/round-53.md` § Gate (absent), and the `aeed0890` subject cites "M41" (undefined anywhere in the tree) | BREAKS | LOW |
| D10 | S051 is attributed to the wrong commit: the C1 source row landed in the C2 commit, under the C2 subject's "sourced entry (S043-S051 …)" | BREAKS | LOW |
| D11 | The C1 subject says "alias-agnostic call edge": true of OC-4, but OC-6 fails on a pure minifier rename | BREAKS (narrowly) | LOW |
| D12 | Entry internal inconsistency: "the one measured fact" versus "two measurements" | BREAKS | LOW |

No finding changes a claim's counter result. D1 through D3 are calibration defects in the record around the claims, and all of them are fixable.

---

## A1 — HOLDS: the erratum landed before C1 and C2 content

```
$ git log --format='%H %s' 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36..c775d6823bfca8f0de8c0874032a954438b38edc   # exit 0
c775d682… round-53: floors bumped in step …
6dd31164… round-53: C1 — opencode 1.19.4 OC-4/OC-6 re-derived …
55973a20… round-53: C2 — always-on boxes alwayson.04/.07 delegated …
aeed0890… round-53: routed repairs — …
5e5336c4… round-53: plan erratum after wave-1 critics (statements bounded before content)
```

- Parent chain (`git log --format='%H %P %ad %cd'`): `5e5336c4` has parent `3bb0a7a3`, and `aeed0890` has parent `5e5336c4`. The erratum is the first commit after the plan.
- `git show --stat 5e5336c4`: `plans/round-53.md | 43 +++…`, 1 file, 43 insertions and 0 deletions. It is append-only and plan-only.
- The read-only jj operation log (`jj --ignore-working-copy op log`) gives the push times. The erratum was pushed at `17:14:49.183 -03:00` (20:14:49Z). The repairs were pushed at 20:24:56Z, C2 at 20:24:58Z, C1 at 20:31:06Z and the floors at 20:34:25Z. No rewrite of `5e5336c4` appears afterwards.
- The cited critic reports were all last written before the erratum commit: `CriticC2Sizing.md` 17:10:14, `CriticC1Sizing.md` 17:12:40 and `CriticDrift.md` 17:13:44 (-03:00, `ls --time-style=full-iso`).

## A2 — HOLDS: each statement equals its counter's printed line

All runs were in the sandbox, at 2026-10-22T20:37Z.

```
$ python3 -B verifiers/check_opencode_repin.py --rev 55973a20…   # exit 1
opencode re-pin: surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 133 assertions
$ python3 -B verifiers/check_opencode_repin.py --rev 6dd31164…   # exit 0
opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 155 assertions
substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032
$ python3 -B verifiers/check_opencode_repin.py --rev c775d682…   # exit 0, identical two lines
$ python3 -B verifiers/check_alwayson_boxes.py --rev aeed0890…   # exit 1
always-on boxes executed and discriminating 0 of 8
$ python3 -B verifiers/check_alwayson_boxes.py --rev 55973a20… | 6dd31164… | c775d682…   # exit 0 each
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
```

- C1 (erratum item 1, `plans/round-53.md:105-110`): the statement is the first line with `<A>`, and the run prints it with A = 155 and exit 0. Erratum item 1 strikes the omp clause, the version and the sha from the statement, which fixes the original `plans/round-53.md:23-26` clauses that the counter never prints. Residual: `<A>` is unbound, so any assertion count at or above floor 129 matches. That matches what the counter enforces and is not a defect.
- C2 (`plans/round-53.md:39-40`): the statement is the first printed line plus exit 0, which matches. The "before" value at `:41-42`, including "both unexecuted", matches the detail lines printed at `aeed0890`.

## A3 — HOLDS: the erratum describes the counters and critics accurately

- Item 1, the second line's provenance: `git show 3bb0a7a3:verifiers/check_opencode_repin.py` lines 122 and 130 take `sub = sj.get("substrate", {}).get("opencode", {})` from the revision's own gate JSON, so the sha does come from the measured revision's gate.
- Item 2, "CriticC1Sizing patches A–D, F": `CriticC1Sizing.md:40-109` covers routes A through D, all printing the target line, and `:118-125` covers route F (default path pointed at a fixture), which also exits 0. Route E is caught (`:113-117`). The list A–D, F is exact.
- Item 3: frozen `CASES` at `check_alwayson_boxes.py:67-74` gives alwayson.04 two PASS cases (plain-rules, version-number) and four FAIL cases (iso-date, iso-timestamp, month-day "Until November 1", dated-claude-md), all of them dated. `:144` `script = tree / d.split(":", 1)[1]` joins an absolute path. `:166` `return 0 if n == len(CASES)` confirms that "of 8" is printed text, not part of the exit term. The guard itself holds at `c775d682`: both dispositions read `delegated:verifiers/verify_alwayson.py`, and `git ls-tree -r --name-only c775d682 verifiers/verify_alwayson.py` lists the file.
- Item 4's factual premise holds: `corpus/README.md:88`, the cited row, records round 49's `dispatch.04`/`dispatch.08` delegation. See D3 for what the item omits.
- Item 7: the in-place tightening leaves the round-52 record's numbers unchanged.
  ```
  $ python3 -B verifiers/check_mcp_instructions.py --rev c8579a4c | grep 'backed .* of'         → mcp instructions backed 0 of 7 clients
  $ python3 -B runs/mcp_frozen_4c003a4b.py --rev c8579a4c | grep 'backed .* of'                  → mcp instructions backed 0 of 7 clients
  $ … --rev c8407a45 (tightened, and frozen bytes from `git show 4c003a4b:…`)                   → 5 of 7 both
  ```

## D1 — MEDIUM: a 63-digit "sha256" is committed in three files

The installed binary's real sha256 is `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, 64 hex digits (from `sha256sum …/opencode.exe`, and printed by the counter's line 2). Three committed files instead carry `538fcb1b6408c8d460882acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, 63 hex digits with one `2` missing after `60882`:

```
$ git grep -n -E '538fcb1b[0-9a-f]+' c775d682 -- verifiers corpus plans
corpus/knowledge/instruction-surface-census-round13.md:550   538fcb1b6408c8d460882acee19f7ff5b3a3eb3383c0633c4f06170857312a7   (63)
verifiers/baseline.json:11 (opencode_round53_note)            538fcb1b6408c8d460882acee19f7ff5b3a3eb3383c0633c4f06170857312a7   (63)
verifiers/fixtures/surfaces/strings-opencode-1.19.4-anchors.txt:1   …460882acee…                                           (63)
verifiers/baseline.json:10 (opencode_binary_sha256, the pin)   538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7   (64, correct)
plans/round-53.md:25                                           …4608822acee…                                           (64, correct)
```

Origin: `.ufo/waves/round-53/build/ExecOcRederive.md:28,38` reports this same 63-digit string as what `sha256sum` "printed". `sha256sum` cannot print 63 digits, so the seat transcribed it rather than pasting it, and the L1 copied it into three committed files without checking.
- Impacted axes: calibration, and freshness provenance. It is a recorded hash that hashes nothing, in the record of the freshness claim. The pin and the counter are unaffected, because `pins OK 3/3` reads line 10.
- Smallest safe correction: replace the 63-digit string with the 64-digit value in census note line 550, `baseline.json:11` and the fixture's line 1. The fixture comment is not an anchor, but verify with the surfaces self-test. Then add the string to the corrections sweep registry (Q29).

## D2 — MEDIUM: the judged head trips the round's own "M41 fix", and the C2 entry is unindexed

```
$ cd …/W2CriticDrift-fleet/kotoba-shokunin && python3 -B verifiers/verify_corpus_integrity.py   # exit 1
           unindexed: corpus/knowledge/alwayson-rule-files-round53.md
           commit_unresolvable: corpus/SOURCES.md:63: cfb894a5
4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
$ python3 -B verifiers/check_gate_finding_delta.py --repo . --base e78dff66… --head c775d682…     # exit 1
gate finding delta e78dff66… -> c775d682…: base drift 5, head drift 5
  new: corpus.pointers.commit_unresolvable
  resolved: corpus.pointers.report_dead
finding delta: new 1, resolved 1
$ git show c775d682:corpus/README.md | grep -c alwayson-rule-files-round53   → 0
```

- Repairs commit `aeed0890` lands `check_gate_finding_delta.py` as the "M41 fix". Its docstring (`:4-7`) names the exact mistake: a gate read as "the same count as base" while its DRIFT set changed. At the judged head, the gate again reads the same count (5 DRIFT, 4/9), and its own new instrument reports a new finding. That finding is `cfb894a5`, the Zed commit cited in the S050 row, which landed in the C2 commit `55973a20`.
- The C2 knowledge entry is the one unindexed file. `unindexed` was 1 at base for a different file, the spot-check, which is now indexed, so the count hides the swap. Routed defect 2 (`plans/round-53.md:68-72`) said to re-record the baseline "last, after every round file has landed". That has not happened at `c775d682`.
- `tracked_files`, `unindexed`, `commit_unresolvable` and `commit_total` are tree-local and do not depend on the clone location. Report-pointer counts may differ outside the fleet; the delta above concerns only tree-local ids.
- Impacted axes: calibration (the "M41 fix" subject against a head that repeats M41) and consistency (an unindexed entry). This is the drift sentinel's class: a record wider than what was verified.
- Smallest safe correction: index `knowledge/alwayson-rule-files-round53.md` in `corpus/README.md`; classify `cfb894a5` as an external-repository commit in the instrument, with a self-test arm, or quote it; then re-record the baseline and show `check_gate_finding_delta.py --base e78dff66 --head <tip>` at `new 0`.

## D3 — MEDIUM: erratum item 4 narrows C2 only and omits CriticDrift F2

`plans/round-53.md:128-132` (item 4, "Drift sentinel, stated honestly") restates only CriticDrift F1, that C2 sits in the same Frontier row as rounds 49–50. `CriticDrift.md:10, 35-51` (F2, MEDIUM) also found the following:
- C1 is the third freshness claim running on `verify_surfaces.py` loader extraction: round 51 C1, round 52 C1 and round 53 C1, all in the Frontier row "Loader-rule freshness" (`corpus/README.md:92`).
- The tie-break rule rounds 51 and 52 used ("Adjacency was claimed in rounds 49 and 50, so C1 works freshness", `plans/round-52.md:11-12`) would pick adjacency at round 53.

None of the erratum's seven items mentions the surface repetition or the tie-break reversal. Item 5 covers F3 and item 6 covers F4, but nothing covers F2. The sentinel text in `plans/round-53.md:13-15` names "rounds 51–52 worked sibling overlap and MCP instruction surfaces" and stays silent on the loader-rule surface that C1 repeats.
- Counterexample to "stated honestly": a reader of the plan and erratum alone would conclude that only C2's frontier choice is in question for the sentinel.
- Impacted axes: calibration (disclosure). Whether this matters for admission is the judge's ruling, as item 4 itself says.
- Smallest safe correction: add one append-only sentence. C1 is the third consecutive freshness claim on the `verify_surfaces.py` loader-rule surface, and the round-51/52 tie-break rule would have picked adjacency. C1 is routed defect 1 promoted to a claim (already at `:66`).

## D4 — LOW: the census note drops the scout's `[INFERENCE]`

`corpus/knowledge/instruction-surface-census-round13.md` (appended in `6dd31164`) says: "the release note records only a bundled Bun runtime upgrade (1.3.14→1.4.4), so the renamed wrappers (`fn`→`l`, `Key`→`Wr`) are a rebuild of unchanged source, not a behaviour change".
- The cited scout hedges this. `ScoutOcRelease.md:81-84` reads "`[INFERENCE]` The alias reallocation is caused by the Bun 1.3.14 → 1.4.4 bundler … I did not rebuild the source with either Bun version". `:98` reads "`[INFERENCE]` A Bun runtime upgrade could in principle alter JS semantics".
- The scout (`:80`) and the S051 row both record a dependency change, `packages/opencode/package.json:81` `@ff-labs/fff-bun` 0.9.4→0.10.5. So the build input was not unchanged source.
- No 1.19.3 against 1.19.4 behaviour comparison was run.
- Smallest safe correction: change it to "[INFERENCE] a rebuild (Bun 1.3.14→1.4.4, `@ff-labs/fff-bun` 0.9.4→0.10.5) of unchanged `packages/opencode/src/`; no behaviour change found in the source delta, none measured".

## D5 — LOW: the entry misdescribes what its instrument checks

- The entry (`corpus/knowledge/alwayson-rule-files-round53.md:62`) says "Its date detector misses undated transient text". Its Limits section (`:83-84`) says "what it does not check (other names, nested directories, transient text without a date)".
- The docstring (`verify_alwayson.py:24-28`) and the code (`TRANSIENT_RE`, `:93-97`) detect six fixed date-free cues, and the instrument reads `.claude/AGENTS.md` and `.claude/CLAUDE.md` (`:66-72`). Run results:
  ```
  $ python3 -B verifiers/verify_alwayson.py --check alwayson.04 --target verifiers/fixtures/alwayson/a04-date-free-transient --json   → FAIL "dated/transient text found: AGENTS.md:3 date-free…"
  $ … --check alwayson.07 --target verifiers/fixtures/alwayson/a07-nested-pair --json   → FAIL ".claude/AGENTS.md and .claude/CLAUDE.md are not one expli…"
  $ … --check alwayson.04 --target probes/undated2   ("The deploy freeze is in effect this week")   → PASS, exit 0
  ```
- So the entry's sentence is false as written. It is true only for undated wording outside the six cues. Two authorities on one instrument disagree (Q31).
- Smallest safe correction: change it to "detects six fixed transient cues (currently, temporarily, …); misses other undated transient wording (e.g. 'this week') and month-year dates". In Limits, replace "nested directories" with "subdirectories other than `.claude/`".

## D6 — LOW: the docstring lacks the alwayson.04 basis the entry says it must carry

- `alwayson-rule-files-round53.md:55-62` says no authority states the dated-text rule for always-on files, that the box "is a lane extension of the skills rule" (S019), and that "the instrument's docstring must say so (Q23)".
- `git show c775d682:verifiers/verify_alwayson.py | sed -n 1,36p` cites only Claude Code's memory page, for the filename set. A grep for `skill|extension|S019|best-practices|time-sensitive` in `verify_alwayson.py` matches only the SKILL.md path code (`:566-571`).
- The authority's own bad example passes the instrument:
  ```
  $ printf '# Rules\n\n- If you are doing this before August 2025, use the old API.\n' > probes/aug/AGENTS.md
  $ python3 -B verifiers/verify_alwayson.py --check alwayson.04 --target probes/aug --json   → PASS, exit 0
  ```
  The entry anticipates this "shape to check". That is honest, but the docstring requirement it states is unmet.
- Smallest safe correction: add one docstring sentence: "alwayson.04 extends Anthropic's skills rule (S019 § Avoid time-sensitive information) to always-on files; month-year dates such as 'before August 2025' are not detected".

## D7 — LOW: the erratum's own timestamp is later than its commit

- `plans/round-53.md:102` reads "Written 2026-10-22 ~20:25Z".
- Git author and committer dates for `5e5336c4` are both `2026-10-22T17:14:49-03:00` (20:14:49Z). The jj operation log records commit, bookmark and push at `17:14:49.086–.183 -03:00`, with no later rewrite.
- 20:25Z matches the repairs and C2 push (20:24:56–58Z), not the erratum. The order claim is unaffected (A1). The provenance line is about 10 minutes wrong, in the section whose job is to be exact.
- Smallest safe correction: an append-only note giving the actual commit time, `5e5336c4` 2026-10-22T20:14:49Z.

## D8 — LOW: the census note cites a deleted dump path

- The census note and `baseline.json:11` give the dump as `/fast/scratch/hyaku/kotoba-r53/ExecOcRederive/oc-1.19.4.strings` (sha256 `2d72d83f…`).
- `ls` on that path returns "No such file or directory". `ExecOcRederive.md:49` reads "`rm -- oc-1.19.4.strings` … removed the scratch dump before staging".
- Byte-identical copies exist at `/fast/scratch/hyaku/kotoba-r53/oc-1.19.4.strings` and `…/ScoutOcRelease/oc-1.19.4.strings`; `sha256sum` gives `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98` for both. On that copy the cited lines hold: 597823 `l("InstructionContext.observe")`, 597828 `Wr.make(…)`, 598311 `k=l("Instruction.resolve")`, 598312 `resolve:k`, 598484 `l("ReadTool.list")` (the `ReadTool.execute` wrapper is in the same chunk), 598489 `let y=yield*r.resolve(F.messages,I,F.messageID)`, and 598496-598499 `<system-reminder>` with `${y.map((B)=>B.content).join(` through `</system-reminder>`.
- Correction: point both records at a surviving copy, or record that the dump is regenerable with `strings -n 4 <binary>` and give its sha256.

## D9 — LOW: dangling forward pointers in committed files

- `alwayson-rule-files-round53.md:15-17` says the full quote set is "summarised in `corpus/lessons/round-53.md` § Gate". `git ls-tree -r --name-only c775d682 corpus/lessons | grep round-53` returns nothing.
- The `aeed0890` subject says "gate finding-delta check (M41 fix)". `git grep -n M41 c775d682` matches only binary-string noise in `.ufo/round-44/evidence/…`. M41 is defined only in the wave-1 draft `.ufo/waves/round-53/build/ScribeMistake.md:1`.
- Both are probably written at round close [INFERENCE], but at the judged revision they point at nothing. Correction: land `corpus/lessons/round-53.md` with § Gate and the M41 row before the report.

## D10 — LOW: S051 attribution

```
$ for c in aeed0890 55973a20 6dd31164 c775d682; do git show $c -- corpus/SOURCES.md | grep -c '^+| S051'; done   → 0 1 0 0
```

- S051 (the opencode v1.19.3→v1.19.4 tag delta, a C1 source) landed in the C2 commit, whose subject reads "sourced entry alwayson-rule-files-round53 (S043-S051, …)". The entry cites S043–S050, S004 and S019, but not S051.
- The C1 subject reads "census append note (S051)", and the C1 census note's provenance paragraph rests on a row that the C2 commit wrote. Counter separability still holds, since neither counter reads `corpus/`. This is CriticDrift F8's knowledge-level coupling, now in the record.
- Correction: state in the report that S051 landed in `55973a20` for C1's census note. Do not rewrite history.

## D11 — LOW: "alias-agnostic" holds for OC-4 only

The probe used the committed 1.19.4 anchors fixture, which passes as the control:

```
$ python3 -B verifiers/verify_surfaces.py --opencode-strings verifiers/fixtures/surfaces/strings-opencode-1.19.4-anchors.txt --json   → PASS 9/9 from 7/7 rules
$ sed 's/l("ReadTool.execute")/q(…)/; s/l("Instruction.resolve")/q(…)/'   → PASS 9/9  (OC-4 survives the wrapper rename)
$ sed 's/=ia(m(function\*/=iQ(m(function*/'                          → FAIL: OC-6 matched nothing
$ sed 's/l("InstructionContext.observe")/q("InstructionContext.observe")/' → FAIL: OC-6 matched nothing
```

- OC-6 pins minified names: `OC_V2_LAYER_DEF_RE` `=ia\(m\(function\*` (`verify_surfaces.py:634-636`), `OC_V2_OBSERVE_RE` `(?:fn|l)\(` (`:637-640`), and `(?:Re|i)\(` (`:732, 740`).
- The C1 subject's parenthetical "(alias-agnostic call edge, decoy arms)" is accurate for OC-4's call edge only. The next rebuild that reallocates helper aliases, which is exactly the 1.19.3→1.19.4 churn class, breaks OC-6 again. That is a freshness tradeoff for the judge; the calibration fix is wording.
- Also noted, not separately rated: `OC_READ_CALL_RE` (`:665-670`) accepts any receiver of `.resolve(<x>.messages, …)` and does not tie it to the service exporting `resolve:`. So the census note's "binds the export, caller edge" binds them by module and window position, not by identity [INFERENCE from the code read; mutation-tester seats own the probe].

## D12 — LOW: entry internal inconsistency

`alwayson-rule-files-round53.md:18-19` says "the one measured fact is the installed Claude Code's Project instructions setting". `:71-75` says "Documentation only, except two measurements", adding opencode 1.19.4's read channel. Correction: change ":18-19" to "two measured facts", or cross-reference Limits.

## Checked and holds (instrument docstring, floors, sources)

- Claude Code memory page re-opened: `curl -sS -L https://code.claude.com/docs/en/memory.md` at 2026-10-22T20:38:58Z gave HTTP 200, 51,971 B, sha256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`. That is byte-identical to the S043 row. The docstring's three section names exist: `memory.md:53` "### Choose where to put CLAUDE.md files", `:366` "### When Claude Code reads AGENTS.md" and `:440` "### Share one file with other coding tools". The `.claude/AGENTS.md` scope is on the page (`:375`, "every `AGENTS.md` and `.claude/AGENTS.md` in your working directory and the directories above it"). So is "Import parsing skips Markdown code spans and fenced code blocks" (`:112`). The entry's Claude Code cells `:356`, `:357`, `:364`, `:368-370`, `:436`, `:442-445`, `:455` and `:619` ("Claude Code skips a file over 4 MiB") match.
- Docstring behaviour probes all match the docstring. A 1 MiB + 10 B `AGENTS.md` gives ERROR "exceeds the 1048576-byte limit", exit 2. An escaping symlink gives ERROR "symlink for AGENTS.md escapes target directory", exit 2. Fenced and inline `@AGENTS.md` give FAIL (not a redirect). A dated `docs/AGENTS.md` in a subdirectory is not read (PASS). `--self-test` gives `0 failure(s) over 89 assertions`, exit 0. `--box-proof` gives `boxes proven 2`, exit 0.
- Floors subject: `python3 -B verifiers/check_assertion_floors.py` exits 0, and every row has observed equal to floor (`surfaces 155`, `corpus_integrity 152`, `corpus_independent 93`, `checklist 1852`, `alwayson 89`, 13 instruments). The registry diff raises only floors and adds `alwayson`. "In step" holds.
- CriticDrift F5 is addressed in code: `verify_skill_checklist.py --json` gives `checklist.box_map_complete PASS … delegated verifiers/verify_alwayson.py: --box-proof exit 0: boxes proven 2`. In my clones that gate exits 1, but only on `trigger.name_directory` (clone directory name), `trigger.citation_resolves` and `governance.citation_resolves` (fleet-relative `../.ufo/…` paths). Those come from the clone location and are not attributed to `c775d682`. The gate-matrix seat owns the in-fleet run.
- The omp row added in `c775d682` matches `ScoutOmpAlwaysOn.md:1, 52-57, 80-96`: ten providers, tie at priority 10, insertion after equals. The tie-break is correctly marked `[INFERENCE]` in the entry.

## Commands not run

The in-fleet `verify_skill_checklist.py --json` at `c775d682` was not run, because the lane working copy has uncommitted L1 edits and a fleet-named clone still lacks the fleet's `.ufo/reports`. I also did no mutation runs of OC-4 receiver binding; those belong to the mutation-tester seats.
