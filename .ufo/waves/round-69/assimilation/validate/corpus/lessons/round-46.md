# Lessons — round 46

Round: 46 (kaika, loop A position 10). Claims are pre-registered in
`.ufo/round-46/claims.json` (C1 depth, C2 operability, C3 calibration); this lesson
records the gate and the mistake classes, not claim verdicts. Evidence: `LOG.md`
§ Round 46 entries (`LOG.md:2001-2298`), WIP commit `36ab0d3` merged by
`78ee57e`, and the kaika W1 STATE dossier
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika-w1/kotoba-state.md` §4.
All pointers below were re-run by this scribe at HEAD `78ee57e`; scope is named per row.

## Mistakes

Every row is a class the lane has already paid for. `captured-by` names the criterion
that now catches it in `corpus/QUALITY.md`; `none → Qnn` means it was uncaptured at
HEAD and this round's bar is the first instrument.

| class | evidence pointer (command → output) | captured-by | fix |
|---|---|---|---|
| M1 Closed payload, surviving class (laundering arc) | `grep -ci 'held-out' SKILL.md` → 0; `grep -ci 'launder' SKILL.md` → 1 (prose only); MANIFEST kotoba rows 39–45 → `[39,40,41,42,43,44,45]`; `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-45/kotoba.md:12` → "14 of the 25 r41-open doors now reject exit 2, 11 [still open]" | none → Q01 | Name the *class* and the held-out hunt that failed to find a surviving shape; closing the declared payload is `improved-bounded`, not closed. |
| M2 Finite census sold as exhaustive | `SCORECARD.md:80` r41 annotation → "complete-census condition is UNMET"; `grep -c 'not demonstrably bounded' .ufo/round-46/scouts/C1.md` → 2; `grep -c 'duplicate-ID' .ufo/round-46/scouts/C1.md` → 2 ("still exits 0 on both frozen and candidate"); `.ufo/round-46/scouts/C1.md` sha256 `d20b34c96f5ede6c9c018ddf02f9b93d026b1922ab0fff4860c1946c65ab2be3` = LOG pin | none → Q02 | An exhaustive claim names the generator of the door space and the seed; a saved 46-arm set is a measurement, not a bound. |
| M3 Record-vs-tree drift (candidate verdict recorded as if landed) | `SCORECARD.md:33` → "verified on the **uncommitted candidate**"; `git show HEAD:verifiers/compare_harness_independent.py \| sha256sum` → `ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d` (the described bytes are committed at `36ab0d3`); `.ufo/round-46/drafts-report-skeleton.md:38` → "unproven / not improved" for the same work | none → Q03 | Every record names the commit that holds the bytes; "uncommitted" is a claim a reader verifies with `git show <ref>:<path>`. |
| M4 Dead recheck/source command | `test -e .ufo/round-45/drafts/v10/post-r44-hunt.py` → exit 1 (absent); `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-45/kotoba.md:29` → "recheck runs"; canonical clone, `python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json` → exit 1, 9 PASS / 1 FAIL `governance.citation_resolves` at `LOG.md:2111`; `grep -l 'recheck' verifiers/*.py` → no output (no instrument reads `recheck:` lines) | none → Q04 | Extend an instrument to resolve every `recheck:` command; pruning a runner must turn the gate red, not the citation silent. |
| M5 Fix that harms (no regression arm) | `SCORECARD.md:165` row 38 → "fix introduced a None-path crash + malformed-field arm survives: C2 fails as declared (harm)"; `SCORECARD.md:100` full round entry | none → Q05 | A fix ships its own regression arm before the claim is scored; a new crash class in the fix is harm, not partial progress. |
| M6 Seat denominator overstated | `git show b1be35f:.ufo/round-40/claims.json \| grep '"seats"'` → `"seats": 40`; `git ls-tree -r --name-only b1be35f -- .ufo/round-40/scouts/ \| wc -l` → 41; `SCORECARD.md:80` → "scout fragments, not proof of 41 declared/complete seats" | none → Q06 | A seat count is `completed/declared` from the claims file; a scout-file count is a different number and is labelled so. |
| M7 SHONEN canonical-form drift | `git show HEAD:SHONEN.md \| wc -l` → 50 for the 4-box template; worktree after L1 regeneration `wc -l SHONEN.md` → 12, `grep -c '^\- \[' SHONEN.md` → 4 (uncommitted at scribe time) | none → Q07 | Regenerate byte-for-byte from the canonical template before any next-round claim; one evidence line per mark. |
| M8 Fleet-root identity contamination | canonical clone at `78ee57e`: `head -1 ../LOG.md` → `# kotoba-shokunin — Iteration Log`; `head -1 ../SCORECARD.md` → `# kotoba-shokunin — Scorecard`; `grep -c kotoba ../SCORECARD.md` → 38 | none → Q17 | Cross-domain: a fleet-level guard that root LOG/SCORECARD first lines name the fleet/protocol lane; route to the integrator, never edit from a child lane. |
| M9 Gate regressions found a round late (substrate rebuild) | `python3 -B verifiers/check_substrate_pins.py` → exit 1, `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` (opencode PASS); `python3 -B verifiers/verify_surfaces.py --json` → exit 1, 5 PASS / 2 FAIL | none → Q09 | A substrate rebuild makes freshness red until the extraction is re-derived and re-pinned; "no rebaseline" is open debt, not a pass. |
| M10 README front-door marker/seed drift | `git show HEAD:README.md \| sed -n '6p'` → `**Domain:** >`; worktree `sed -n '6p' README.md` → the fixed domain line (L1, uncommitted); `grep -c 'README' verifiers/verify_skill_checklist.py` → 2, both docstring prose, no check | none → Q08 | Lint README header fields: reject a bare block-scalar indicator as the value; Domain equals the PROVINCE domain. |
| M11 Honest stops recorded correctly (preserve) | `LOG.md:971` "steered round 19"; `LOG.md:1088` "Round 20 … blocked before native dispatch"; `corpus/lessons/round-19-recensus.md:1`; MANIFEST r42 kotoba row `admitted: None`, notes "no dispatch" (the other r42 row is kotodama, `admitted: False`) | none → Q15 | Keep: an honest stop names its blocker and leaves axes unchanged; it is a valid round outcome. |
| M12 Non-author gate disagreements (preserve) | `ls corpus/lessons/ \| grep -E 'aggregator\|box3'` → 6 files (`round-1-aggregator-audit.md`, `round-4-aggregator-audit.md`, `round-5-aggregator-audit.md`, `round-6-aggregator-audit.md`, `round-8-aggregator-box3-coldrun.md`, `round-9-aggregator-corpus-verdict.md`); `SHONEN.md:7-15` carries the PROTOCOL.md:65 attribution note | none → Q16 | Keep the attribution discipline: `[x]` and verdicts from a non-author; disagreements recorded, not averaged. |
| M13 Structural frontmatter gate mistaken for semantic | `grep -n 'structural parse' verifiers/verify_skill_checklist.py` → line 76 "Limit: a structural parse, not semantic YAML validation."; `SKILL.md:15` description carries the literal `<skills>` token (peer-reported rule, not re-opened here; presence measured only) | none → Q08 | Add a semantic frontmatter lint (strict YAML + description tag rule) beside the structural parse. |
| M14 Unstable source during a measured run | `LOG.md:2043` concurrent join changed the comparator SHA mid-run, so its exit-0 "is explicitly not counted"; `LOG.md:2178` `T1-after-landing-13` "was excluded because comparator changed during its command"; `LOG.md:2201` preliminary N1 "explicitly superseded" while the manifest changed | none → Q10 | Record source sha256 before and after every measured run; a source that moves during the run invalidates the result, and the exclusion is disclosed. |
| M15 Evidence-tree bloat | `du -sh .ufo/round-46` → 52M; `git ls-files .ufo/round-46 \| wc -l` → 8050 vs `git ls-files .ufo/round-45 \| wc -l` → 403; `du -sh .ufo` → 122M, 9527 tracked files; Z1 recorded drafts growing 91 → 320 files inside the round (`LOG.md:2046,2052`) | none → Q11 | Keep only evidence cited by a claim/ruling; prune draft scratch after the counting bundle is named. |
| M16 Unprovenanced knowledge entries | `for f in corpus/knowledge/*.md; do grep -qE '^[[:space:]]*source:' "$f" && grep -qE '^[[:space:]]*verified-at:' "$f" && grep -qE '^[[:space:]]*recheck:' "$f" \|\| echo "$f"; done \| wc -l` → 32 of 34; `grep -lE '^[[:space:]]*source:' corpus/knowledge/*.md \| wc -l` → 2 | none → Q12 | New entries open with `source:`/`verified-at:`/`recheck:`; the admission bar (Q12) rejects a prose-only entry. |
| M17 Fix that silently narrows accepted input (false red) — found at landing | `.ufo/round-46/scouts/w2-reviewer.md` MED-3; repro `.ufo/round-46/evidence/w2/l1-matrix/med3/`: prose line `warn: saw {"a":1,"a":2} in log` before a valid payload → frozen `1101213a…` exit 0, committed `ccf41c23…` exit 2 `live: duplicate JSON member 'a'`; landing `778b367e…` exit 0, duplicate inside the selected payload still exit 2 | none → Q18 | the duplicate-member check runs on the selected payload only; regression arms `extract_json: duplicate-member prose fragment …` + `… inside the selected payload still rejects` (self-test 328 → 330) |
| M18 Lane seat reports a run result it did not observe | `corpus/SOURCES.md` S010 first read "--self-test and --json … both exit 0"; L1 re-run: `verify_skill_checklist.py --json` exit 1 (9 PASS / 1 FAIL at `LOG.md:2111`) in the worktree and the canonical clone | Q03, Q13 | corrected before commit; a seat's exit codes are re-run by the integrating L1 before they become a row |
| M19 Measuring against a carrier that live agents write | `.ufo/round-46/evidence/w2/l1-matrix/race-fresh2/results.json`: honest control frozen exit 0 then committed exit 2 `false blocker` seconds apart (`candidate_blocks` drifting); `.ufo/round-46/scouts/w2-reviewer.md` HIGH-3 (1127 → 1131) | Q10 | measure on a frozen carrier snapshot (`HOME=/var/tmp/kotoba-r46-home`, `cp -a` of the sessions dir, listing digest `4d715d65…`); a snapshot-pinned probe is the r47 fix |

Pointer corrections made while re-running the set: M7 and M10 still hold at HEAD bytes,
but L1's worktree regeneration (`SHONEN.md`, `README.md`) is uncommitted — the rows record
both states. M11's evidence is `LOG.md:971` / `LOG.md:1088`, not a `## Round 19` heading.
M4's live failure is at `LOG.md:2111` (the later I1 run cited 2112; measured 2111). M2's
C1 ruling was re-read by hash, not re-executed: that probe writes evidence into the tree,
outside this scribe's two-file write scope. M13's Psych `safe_load` sweep was not re-run
(peer report); only the gate-limit text and the `<skills>` presence were measured here.

## Gate

### Knowledge candidates

None admitted. The round's 1–3 claim cap is full with the pre-registered r46 claims
(`.ufo/round-46/claims.json`: C1 depth, C2 operability, C3 calibration), so no knowledge
candidate was opened or judged this round. `corpus/QUALITY.md` and this lesson are
file-contract conformance work, not axis claims. Any future candidate must still clear
`corpus/QUALITY.md` Q12–Q14 before admission.

### Sources

Rows written to `corpus/SOURCES.md` this round (contract v1 rule 1: each opened in-round by its author, the L2 seat `R46ExecSources-2`; fetch records `.ufo/round-46/evidence/w2/sources/fetch-log.json`). Considered: 30 ART-dossier draft rows + ~40 lead bullets; admitted as rows: 10 (9 `queued` A-tier, incl. 2 own-work); rejected: 1 (S011, community, C). Status changes old→new (logged per contract rule 2): S001, S002, S003, S008 `queued`→`mined`, used-by `—`→`SKILL.md` (§ Frontmatter craft portability floor, folded this round).

| id | URL | accessed (UTC) | fetched sha256 | quote (≤25 words) | location |
|---|---|---|---|---|---|
| S001 | https://agentskills.io/specification.md (reader text of https://agentskills.io/specification) | 2026-10-19T18:40:53Z | `4c649bdf0e0a51c9…` | "Keep your main SKILL.md under 500 lines. Move detailed reference material to separate files." | section 'Progressive disclosure', structure guidance (spec.md line 251) |
| S002 | https://agentskills.io/client-implementation/adding-skills-support.md | 2026-10-19T18:40:54Z | `9c0e85eed0c774d5…` | "Skill files authored for other clients may contain technically invalid YAML that their parsers happen to accept." | section 'Handling malformed YAML' (client.md lines 119-128) |
| S003 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | 2026-10-19T18:40:54Z | `727f3fa1168eb1c3…` | "Cannot contain XML tags" | field list under Skill structure, description rules (claude-bp.md line 155; name field repeats it line 162) |
| S004 | https://agents.md/ | 2026-10-19T18:40:55Z | `e3a5b9a4825ed894…` | "The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything." | FAQ 'What if instructions conflict?' in page body |
| S005 | https://spec.commonmark.org/0.31.2/ | 2026-10-19T18:40:53Z | `c85f56cc2101f761…` | "A code fence is a sequence of at least three consecutive backtick characters or tildes." | section 4.5 'Fenced code blocks', opening definition |
| S006 | https://www.rfc-editor.org/rfc/rfc8259.txt | 2026-10-19T18:40:54Z | `61a5378f4255c720…` | "The names within an object SHOULD be unique." | Section 4 'Objects' (rfc8259.txt lines 320-335); the next paragraph says non-unique names make receiver behavior unpredictable |
| S007 | https://docs.python.org/3/library/json.html | 2026-10-19T18:40:54Z | `ed1372c4c1afe21c…` | "Repeated names within an object are accepted, and only the value of the last name-value pair is used." | section 'Standard Compliance and Interoperability', bullets under 'In particular' |
| S008 | https://yaml.org/spec/1.2.2/ | 2026-10-19T18:40:55Z | `2fe1bf40792df22e…` | "Plain scalars must never contain the ": " and " #" character combinations." | section 7.3.3 'Plain Style', immediately before production ns-plain-safe |
| S009 | verifiers/compare_harness_independent.py --self-test (local run, exit 0) | 2026-10-19T21:42Z (run); file sha256 at HEAD ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d | `ccf41c23d2c76612…` | "self-test: 0 failure(s) over 328 assertions" | final stdout line of `python3 -B verifiers/compare_harness_independent.py --self-test` |
| S010 | verifiers/verify_skill_checklist.py --self-test and --json (local runs, both exit 0) | 2026-10-19T21:42Z (runs); file sha256 214ae44dcba45ba19656a0b2aa6c49900c618f6716a64fef0776f06437cfc8d0 | `214ae44dcba45ba1…` | "0 failure(s) over 1597 assertions" | final stdout line of --self-test; --json check checklist.box_map_complete reports '41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)' |
| S011 | https://agentman.ai/blog/build-your-first-agent-skill-skillmd-anatomy | 2026-10-19T18:40:55Z | `852eec7946f399f7…` | "must match the parent folder name exactly or the skill will not load" | frontmatter field-table paragraph; contradicts S002 'Lenient validation' (name mismatch -> warn, load anyway). Cross-check: `grep -ciE 'angle bracket' spec.md` -> 0 while the page credits an angle-bracket ban to the spec |

Correction before landing: S010's source cell first read "--self-test and --json … both exit 0"; the L1 re-ran both (`--self-test` exit 0, 1597 assertions; `--json` exit 1, 9 PASS / 1 FAIL at `LOG.md:2111`, worktree and canonical clone) and corrected the cell before commit; S011's `recheck` `none` (not a contract value) became `180d`.

L1 re-open (lane, not non-author) at 2026-10-19T22:04Z: S006 (`grep -c 'The names within an object SHOULD be unique' rfc8259.txt` → 1), S007 (python json page, "Repeated names within an object are accepted, and only the value of the last" + "name-value pair … is used" across one line break), S003 (`best-practices.md` lines 155 and 162 "Cannot contain XML tags") — 3/3 quotes present. Timestamp defect: S001–S008 `accessed_utc` read `18:40Z` while `date -u` placed the seat's work near 21:40Z (S009/S010 record `21:42Z`); the 18:40 values are local time (UTC−3) labelled `Z` — the date holds, the hour label is wrong.

### Spot-check

pending — non-author verification by the orchestrator after landing; agree/disagree recorded here by a later append
