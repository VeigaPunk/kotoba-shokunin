Result: HOLDS — every M58–M64 and Q41–Q45 evidence pointer resolves and says what its row claims; both re-runnable demonstrations reproduce byte-for-byte; M62/Q45's "not yet shown able to fail" is honest; three LOW wording/calibration findings, none breaking a row's core claim.

Seat: KotobaR57A3.A3ReviewMistakes (reviewer, leaf). Lane read-only except this report. Sandbox clone: sandbox — no commits made; working clone at 07c33d73ddce769d9cea2846a6313164401b5478 (/fast/scratch/hyaku/kotoba-r57a3/A3ReviewMistakes), used only to execute `.ufo/waves/round-57/build/check_report_hashes.sh` and to read counter bytes. No tool installs or upgrades (python3, git, curl, grep preinstalled; nothing needed).

## 1. Re-runs (assignment-mandated)

### M58 scan — python one-liner, lesson `corpus/lessons/round-57.md:68`, run verbatim (cwd /tmp, GIT_* unset)

```
40c2b5eb
41c2f484
7639deba
exit=0
```

Matches the lesson's recorded output (`40c2b5eb`, `41c2f484`, `7639deba`, `exit code: 0`) exactly. The one-liner's code does what the row claims: skips lines containing `sandbox` (case-insensitive), skips tokens introduced by `sha256`, verifies 7–40-hex candidates with `git rev-parse --verify -q <h>^{commit}` against the lane, prints the survivors.

Cross-check with the round's own tool, executed from the sandbox clone:

```
$ bash <sandbox>/.ufo/waves/round-57/build/check_report_hashes.sh \
    /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    /home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md
/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md:14: 40c2b5eb
/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md:14: 41c2f484
/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md:14: 7639deba
exit=1
```

Matches Q41's recorded claim (QUALITY.md:52: "exit 1 on the round-56 report: 40c2b5eb, 41c2f484, 7639deba"). Fleet report :14 carries all three hashes and no `sandbox` word (the scan's output proves the line-level skip did not fire).

### M61 grep — lesson :85, run verbatim

```
$ grep -c 'Kill only by the PIDs you started' \
    /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-56/build-spec.json
0
exit=1
```

Matches the lesson's recorded block (`0`, `exit code: 1`). The claim "the cap is independently visible on bounds line 6" also verified: `.ufo/waves/round-57/bounds.md:6` carries "Kill only by the PIDs you started … at most 4 concurrent processes and 120 s wall time".

### M63 greps — lesson :102, re-run over the round-56/57 context files

```
round-57/controls-call.json: 0   (exit 1)   <- the M63 instance
round-57/w0-call.json:       1   (exit 0)
round-57/build-spec.json:    1   (exit 0)
round-57/build-dispatch.json:1   (exit 0)
round-56/build-spec.json:    0   (exit 1)
round-56/controls-call.json: 0   (exit 1)
```

Frozen receipt `.ufo/waves/round-57/r7-bound-grep.txt` (04:37:44Z) agrees line for line (r56 build-spec/falsify-call/controls-call = 0; r57 bounds.md = 1, controls-call = 0, build-spec = 1, build-dispatch = 1). M63's mechanism verified on the file itself: controls-call.json mentions `bounds.md` once (by reference), carries the lower-case summary "kill only by the PIDs you started" once, and has no "4 concurrent processes" text — exactly the row's "named `bounds.md` and summarised the kill bound in lower case".

Falsify-wave contexts (lane-root attempt-1 files and a3 attempt-3 files): `Kill only by the PIDs you started` count = 2 in each of falsify-spec.json, falsify-taskcall-sent.json, falsify-dispatch.json and the a3 copies (inline, `bounds.md` mentioned 0 times — carried by content, not reference); a3/falsify-dispatch.json also carries "4 concurrent processes" once. M63's fix's first half ("every later context inlines `bounds.md`") is realized in substance.

## 2. Pointer-by-pointer audit (all resolve; all say what the row claims)

- **M58.** `.ufo/reports/round-56/kotoba.md:14` — the three hashes, unlabelled ✓. `corpus/lessons/round-56-verifier-spotcheck.md:30-31` — "40c2b5eb, 41c2f484 and 7639deba are MISSING from the lane repo … sandbox commits under /fast/scratch/hyaku/kotoba-r56/ … The report's line 14 does not say they are sandbox commits" ✓; :219-221 (R1 finding) ✓. Fix pointers: `plans/round-57.md:83` ("R1 sandbox hashes are labelled in every wave context and in the report") ✓; `bounds.md:4` (sandbox label + clone path, never bare) ✓. Fix realized in this round's Corrections section (`corpus/lessons/round-57.md:57-60`: hashes labelled sandbox with clone paths and receipt lines). Shown-able-to-fail = the scan; re-run reproduces (§1) — real.
- **M59.** `corpus/lessons/round-56.md:22-25` — the quote-notes paragraph says "the project line `:323` holds no agent word" (S076) and calls S078's quote "a fenced example whose info string `text` stays" — the inaccuracies the row names ✓. `round-56-verifier-spotcheck.md:107-121` — S076 quote verbatim but user-level, better unshaped 23-word quote across `:320-323`; S078's `text` is the fence info string, not prose; ":121 Neither shaped quote changes G's substance" ✓ (the row's last clause is verbatim-supported). Fix pointers: :222-228 ✓; `plans/round-57.md:83-85` (R2 sentence) ✓. Fix realized: Corrections § (:44-52) corrects both notes, prefers `:320-323`, sources the SKILL.md:109 clause at `migrate-v1.mdx:486`, rows `r57-r2-s076-note`/`r57-r2-s078-note`/`r57-r2-skill-singular-agent` registered. Shown-able-to-fail ("the source re-open caught the note/source mismatch for both entries") — spotcheck text confirms — real.
- **M60.** `round-56-verifier-spotcheck.md:63-67` (case-folded base counts; `.claude/AGENTS.md`/`.codex/AGENTS.md` memory files; "true new ground is 5, so the counter understates G") ✓; :233-236 (R4 finding) ✓. Fix pointers: `plans/round-57.md:39` ("held ground is counted case-sensitively at path-segment boundaries (round-56 spot-check R4)") and :116 ("the held-ground test is case-insensitive at path-segment boundaries (G stays distinct casefold") ✓; `verifiers/check_plugin_manifests.py:960-979` = `held_in_text`, casefolded both sides with segment-boundary test, docstring naming `.claude/AGENTS.md` vs `.claude/agents` ✓. Shown-able-to-fail: `controls/CtlC1HeldVariant.md:65-72` — v2 re-score of the exact v1 worlds: "World A2 → `0 of 0; new ground 0`, exit 1; World B → `0 of 0; new ground 0`, exit 1" ✓ real. The row's caveat is accurate, not modesty padding: :69 attributes the closure to "the v2 path shape; duplicated tokens", not to the case-fold check, so "not an isolated demonstration of the case-fold check" is correct. The claimed self-test arms exist (`check_plugin_manifests.py:1681-1690`: case difference holds it; uppercase token held by lowercase base; case-insensitive match keeps segment boundary; memory-file analogue does not hold) and the row's "I did not execute that self-test" is disclosed.
- **M61.** `.ufo/reports/round-56/kotoba.md:36` ("killed three of `ExecCneShortcuts`' runs with `pkill -f` on the shared scratch root, and drove the host to load 96") ✓; `corpus/lessons/round-56.md:61-64` (M56 row, same facts, "captured-by: none") ✓; `round-56-verifier-spotcheck.md:241-246` — "M56's fix is not yet shown able to fail" ✓ exactly as the row cites it. Fix pointers: `bounds.md:6` ✓; `plans/round-57.md:85-87` (R7: bound in bounds.md, in every wave context, grep fails on the round-56 build context) ✓. Shown-able-to-fail = the §1 grep — real.
- **M62.** `plans/round-57.md:31-32` — frozen predicate "exits 0, which it does iff it prints `plugin manifests found on the live page F of K; new ground G` with F ≥ 5 and G ≥ 3"; :43 "clients outside the seven" ✓ (F ≥ 5 of seven clients). `.ufo/waves/round-57/C1-measure.txt` (05:01:30Z) — "plugin manifests found on the live page 4 of 4; new ground 4 … exit 1", counter sha256 `bf11a4efc1c7598…` matches the frozen v2 digest; the 4 backed rows are exactly Claude Code, Codex, Gemini CLI, Cursor ✓. Zero margin reported during the build wave: `build/CriticAxisFit.md:1,42,49` ("the zero-margin F>=5 configuration is undisclosed"; probes documented 2026-10-23T04:49–04:51Z), `build/ScoutPluginMcp.md:1,88` ("C1 sits at exactly F=5"; "F = 5 of K = 6 … no slack"), `build/CriticC1Rows.md:1,42` ("reachable honestly at exactly F=5 of 7 with zero slack") ✓ — all three named seats did report it. "Captured-by: none" is consistent with the pre-freeze wave's design (hollow-world reachability, per the plan's erratum text). Honesty of "not yet shown able to fail (no round-58 plan exists)": `plans/` contains round-47…round-57 plus two wwkd files, no round-58 ✓; `grep -c census plans/round-57.md` = 0 (no census recorded) ✓; Q45 (`corpus/QUALITY.md:56`) claims no able-to-fail demonstration ✓. The statement is honest and correctly scoped.
- **M63.** `.ufo/waves/round-57/r7-bound-grep.txt` ✓ (content above); controls-call.json mechanism ✓; "w0 and build contexts carry it verbatim" ✓ (1 hit each). Captured-by Q44 ✓ (Q44 exists, QUALITY.md:55, cites M61). Fix status: first half realized (falsify contexts inline the bound and the cap); second half ("the falsify call's grep is recorded in the report") not yet true — `.ufo/reports/round-57/` is absent/empty (ls prints nothing). See finding F2.
- **M64.** Gate Rejected rows 1–2 (`corpus/lessons/round-57.md:30-36`): C2 `check_infoless_fences.py` at `ee50d8fa` met 04:20Z–04:45Z; C1 v1 at `ee50d8fa` met 04:20Z–04:40Z — "both v1 counters … within 25 minutes" ✓ (25 and 20 minutes). Five seats: CtlC1RealNoForm, CtlC1HeldVariant, CtlC1DoNothingJunk, CtlC1Fabricated, CtlC1KeyedLabels all carry `## v2 re-score` sections ✓; none met v2 (RealNoForm 0 of 0; Fabricated 0 of 6; KeyedLabels 1 of 6; DoNothingJunk world D 1 of 7; HeldVariant worlds 0 of 0, adaptation 3 of 3 — see F1); "best hollow world `found 1 of 7`, exit 1" = CtlC1DoNothingJunk.txt:304 ("plugin manifests found on the live page 1 of 7; new ground 1", world D, sandbox b9765981… labelled with clone path at :285) ✓. "C2 withdrawn, redesign input `build/check_infoless_fences_v3.py`" — file exists ✓.

## 3. Q rows (citation structure)

Q41→M58, Q42→M59, Q43→M60, Q44→M61, Q45→M62 (`corpus/QUALITY.md:52-56`). Every Q row cites exactly one M row; M63/M64 are captured by Q44/capture-wave respectively and need no Q row of their own. Q-row substantive claims spot-checked: Q41's tool-and-exit claim reproduced (§1); Q44's "prints 0 on the round-56 contexts" verified for build-spec, controls-call and (per frozen receipt) falsify-call; Q43's required self-test arms exist in the frozen counter (:1681-1690); Q42 was applied to this round's own quote notes (lesson :22-25, "each re-opened against the seat's fetched bytes by the L1, Q42") — but see F3.

## 4. Findings

### F1 (LOW, wording — M64 and Gate Rejected row 2): "best hollow world" superlative needs its tie-break stated

The five v2 re-scores contain a stronger-scoring adaptation than world D: `controls/CtlC1HeldVariant.txt:110` — "plugin manifests found on the live page 3 of 3; new ground 3" (:120 "[v2 best-world score: F=3 of K=3; G=3; predicate not met because F<5]"). It is not a hollow world — its tokens are the clients' own manifest paths (`.claude-plugin/plugin.json`, `gemini-extension.json`, `.cursor-plugin/plugin.json`) found on the client pages, i.e. real ground — so "best hollow world `found 1 of 7`" is defensible, but the lesson nowhere says why 3-of-3 is excluded. A reader auditing "best" against the receipts hits an apparent contradiction first. Substantive conclusion unaffected (both exit 1; no hollow world met v2).

Proposed old→new, `corpus/lessons/round-57.md:107-108` (M64):
- old: "(erratum 1), shown able to fail by the five seats' v2 re-scores (best hollow world `found 1 of 7`, exit 1); C2"
- new: "(erratum 1), shown able to fail by the five seats' v2 re-scores (best hollow world `found 1 of 7`, exit 1; the strongest adaptation overall, `found 3 of 3; new ground 3`, exit 1, used the clients' own manifest tokens and is real ground, not hollow); C2"

Same clarification applies to the identical phrase in the Gate Rejected row 2 flip cell (`corpus/lessons/round-57.md:35-36`).

### F2 (LOW, calibration — M63): no able-to-fail status, and the fix's second half is not yet realized anywhere

M62 explicitly admits "not yet shown able to fail"; M58–M61/M64 demonstrate theirs. M63 states neither. Its fix has two halves: "every later context inlines `bounds.md`" — realized (§1: falsify contexts carry the bound and the cap inline); "the falsify call's grep is recorded in the report" — not yet true: `.ufo/reports/round-57/` is absent/empty, so no committed record of the falsify-context grep exists (my §1 table is the first). Not a false claim (the row claims nothing), but the asymmetry with M62 is exactly the calibration pattern this round mined.

Proposed old→new, `corpus/lessons/round-57.md:103-104` (M63):
- old: "captured-by: Q44 (this\n  round) · fix: every later context inlines `bounds.md`; the falsify call's grep is recorded in the report."
- new: "captured-by: Q44 (this\n  round) · fix: every later context inlines `bounds.md`; the falsify call's grep is recorded in the report; not yet shown able to fail (no round-57 report exists yet)."

### F3 (LOW, wording — Gate § Quote notes, the round's own Q42 application): substring carve-out is not unique to S084

`corpus/lessons/round-57.md:22-24` says S079, S081, S084 and S085 are "one line each and unshaped (S084 is a contiguous substring: …)". Byte-verified against the pinned source: fetched https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx at 2026-10-23 06:58:18 UTC, HTTP 200, 60,780 B, sha256 `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` (matches the Gate row's `e505931a…`, 60,780 B). Line 21 of the fetched bytes is the recorded quote followed by four more words: "…like the local example above. To load published packages" — so S085 is also a strict substring of its line. "Unshaped" and "one line" hold (no bytes removed inside the quote; no folding); only the parenthetical's uniqueness is wrong. Sibling seat A3ReopenS079 reports the same for S079 (27-word line, 9-word quote) — not re-verified by me. No Q42 violation (a contiguous whole-sentence span needs no shaping and the note's shaping disclosures are otherwise accurate).

Proposed old→new, `corpus/lessons/round-57.md:22-24`:
- old: "S079, S081, S084 and S085 are one line\neach and unshaped (S084 is a contiguous substring: the list marker and bold label before it and the link after it are\nnot quoted);"
- new: "S079, S081, S084 and S085 are one line\neach and unshaped (S084 is a contiguous substring: the list marker and bold label before it and the link after it are\nnot quoted; S085 likewise a contiguous substring: its line continues `To load published packages` after the quote);"

## 5. Honesty verdict on the assignment's named case (M62/Q45)

"Flag every fix claimed able to fail that is not (M62/Q45 says it is not yet: is that stated honestly?)" — Yes, honestly stated and correctly scoped: no round-58 plan exists (`plans/` listing), no census command exists in the round-57 plan (grep count 0), Q45 makes no able-to-fail claim, and no seat output through this wave exercises the Q45 rule (a rule about the *next* freeze cannot have been shown able to fail yet). The only fix in M58–M64 claimed able to fail without demonstration would be none — M63 claims nothing either way (F2).

## 6. Residual risk and verification gaps

- The "~04:50–04:54Z" range in M62 is byte-evidenced only for CriticAxisFit (probes 04:49–04:51Z at CriticAxisFit.md:42); CriticC1Rows and ScoutPluginMcp print no fetch timestamps in their report heads. Consistent with the build-wave window; not separately verified [INFERENCE on the exact range].
- I did not re-verify S079's line length (F3's S079 clause rests on the sibling report) and did not re-open S080–S083/S084 quote shaping — owned by the dedicated re-open seats.
- HeldVariant's 3-of-3 adaptation being "real ground, not hollow" is my reading of its token provenance (tokens found on the client pages); its own report never labels that world hollow. If the L1 disputes it, F1's clarifying clause should be dropped rather than misapplied.
- M62's population claim ("the honest count is 4") is taken as consistent with the landed counter output (4 BACKED rows; VS Code/Copilot CLI/opencode rejected by token rules); the independent re-census is A3CriticTargetCensus's item, not mine.
- Process hygiene: all commands capped (≤120 s); no kills; one sandbox clone; no lane writes except this report; no pacman/uv/npm installs.
