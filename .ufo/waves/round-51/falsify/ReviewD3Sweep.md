Verdict: FAILS. At the pinned revision 59903b2637689739a5b9901956301da72d0effe1, one stale hit has no bound: `corpus/knowledge/sibling-overlap-census-round49.md:212` says the Claude Code subagent page's remedy for overlap "is craft", but that page documents a removal lever (`permissions.deny` with `Agent(name)`). The two routed sites (SKILL.md, `corpus/README.md:72`) are fixed and bounded.

Scope: judged at 59903b2 as assigned. Lane HEAD is now 533ff20 (one commit after the pin). The working tree has uncommitted edits to SKILL.md, the lever entry, PROVINCE.md, corpus/README.md and verifiers/verify_surfaces.py; I did not judge them. At 533ff20, census line 212 and entry line 64 are unchanged.

## Findings, by severity

### P1 — census :212 is live, unbounded, and contradicted by its own source
- Pinned text (`sibling-overlap-census-round49.md:212`): "Its remedy for overlap is craft: 'Make each description specific enough to route to the right subagent' (`sub-agents.md:1293`)." It is the S026 example inside round-50 finding 4 (`skill-selection-rules-round50.md:42-45`).
- Fetched `https://code.claude.com/docs/en/sub-agents.md` on 2026-10-22T15:22:38Z: HTTP 200, 110,784 B, sha256 `89aa73eb3f28e274650634620113a19585dd09b7f40be3dd16d584800cb60aed`, matching the census recheck prefix.
- The page documents a removal lever. Line 729: "You can prevent Claude from using specific subagents by adding them to the `deny` array" (15 words), format `Agent(subagent-name)`, example at line 734. Line 515: "To block specific agents while allowing all others, use `permissions.deny` instead." (link markup removed).
- Bound check against the three required bounds: eight pages, no (one page); author-written, no (subagents); finding 4 superseded, no. The lever entry says "This entry supersedes finding 4" (`skill-overlap-levers-round51.md:10`), but its table has seven skill rows and no subagent row, so the S026 instance is superseded by nothing.
- Round-50 corrections (census `:301-311`) name the "only arbitration" and "keyed on the skill name" sentences only, not `:212`.
- No round-50 seat text quotes the deny lever (see evidence item 5).
- Build disagreement: `.ufo/waves/round-51/build/D3Sweep.md` lists `:212` under "Checked, not hits" as page-scoped. Page scope is not one of the three bounds, and the page contradicts the sentence.
- Fix, not applied: add a marked correction to the census quoting sub-agents.md:729, or add a subagent row with its own source and recheck. The second needs a scope change, so it is for the lead.

### P2 — `skill-overlap-levers-round51.md:64-65` overclaims with "only lever"
- Pinned text: "rewriting the description is the only lever that keeps both skills automatic." No bound. Same text at 533ff20 and in the working tree at read time.
- Contrary evidence in the corpus: Claude Code `paths` (fetched `skills.md`, HTTP 200, 111,557 B, sha256 `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456`, matching the recheck prefix; line 403): "Claude loads the skill automatically only when working with files matching the patterns" (13 words). For a location split, `paths` resolves the overlap and both skills stay automatic in their paths. The same paragraph recommends a removal lever for location splits, so it contradicts itself.
- Fix: bound the sentence to intent-based overlap, or name `paths` as a scope lever outside the count.

### P2 — the bound's page count disagrees across four sites
- Round-50 entry, lines 9-10: "This entry widens that to eight more pages from five clients." Its table lists eight rows: S024, S025, S026, S027, S028, S029, S022, S019. S022 was already one of round 49's three pages (census lines 195-196: "Round 49 swept S022, S023 and S018"). New pages: seven (S019, S024-S029).
- Census line 195: "now on nine pages". Line 196: "Round 50 opened six more client pages (rows S024-S029". S019 is outside its count.
- Pinned `corpus/README.md:72` and `SKILL.md:379`: "eight client pages (S024–S029, S022, S019)" and "the eight client pages that entry read".
- Pinned `corpus/README.md:131`: "six more client pages document no tie-break".
- The eight-page bound the sweep was asked to check does not match the census count for the same pages. Fix: one page list and one count, copied to every site.

### P2 — the lever entry restates round-50 finding 1 without "author-written"
- `skill-overlap-levers-round51.md:8-9` (pinned): "found that no client documents a rule between two differently named skills whose descriptions both match." Round-50 finding 1 (`skill-selection-rules-round50.md:29`) says "two differently named, author-written skills". The bound is dropped. The working tree did not change these lines at read time.

### P3 — smaller bound gaps at the pin
- `SKILL.md:389` "where the description is still the only lever": bounded only by the paragraph's seven-row table; no "author-written". Uncommitted working-tree text narrows this; not judged.
- Census `:250` "the six pages opened this round document only name-keyed rules": the six include S026, which round-50 finding 2 says has a fit-based catch-all (`sub-agents.md:77`, cited there, not re-verified by me). The `:301` correction does not name this sentence (the build seat flagged the same gap).
- `PROVINCE.md:17` and `corpus/README.md:69`: "no documented tie-break exists between overlapping descriptions", cited to three pages (S022, S023, S018). No eight-page or author-written bound. Uncommitted working-tree edits add "author-written" to PROVINCE.md:17 and corpus/README.md:141; not judged.
- `corpus/README.md:131-132`: "six more client pages document no tie-break between overlapping descriptions". No author-written bound.
- `skill-overlap-levers-round51.md:74`: "omp documents no tie-break either". An unrecheckable negative about omp's shipped docs (no URL). Labelled outside the count, so not a hit; noted only.

## Checked and holding (pinned revision)
- `SKILL.md:379-380` (read as 375-377 by the build at 43ca0bf): eight pages and author-written present; the "documented remedy" clause is gone. HOLDS.
- `corpus/README.md:72`: eight pages, author-written, finding 4 superseded. HOLDS.
- `skill-selection-rules-round50.md:42` (finding 4): superseded note appended at `:94-98`. Closes the build's advisory P2. HOLDS, except the S026 gap in P1.
- `skill-selection-rules-round50.md:40` (finding 3): corrected at `:75-80`; "none compares two author-written descriptions" at `:80`. HOLDS.
- `skill-selection-rules-round50.md:86`: "keyed on the name" means the subagent name. HOLDS.
- Census `:34`, `:210`, `:225`, `:227`: corrected at `:304-311` (`:309`: "is false for Claude Code"). HOLDS as corrected in entry.
- Census `:301` heading quotes the withdrawn sentence as the thing corrected. HOLDS.
- `SCORECARD.md:28` (committed at 533ff20, not in the pin): quotes finding 4 under "Supersedes round-50 finding 4". HOLDS as a quote, but it inherits the P1 gap.

## Comparison with D3Sweep.md (build, measured at 43ca0bf)
- Build verdict: HOLDS. This verdict at 59903b2: FAILS.
- Same results: SKILL.md and `corpus/README.md:72` fixed and bounded; the owning entry's finding 4 now carries a supersession note (build advisory P2 closed).
- Different: census `:212` (build: page-scoped, not a hit; here: live P1); census `:250` (build: covered by `:301`; here: not covered, P3).
- New since the build's read, from the C2 text: lever entry `:64` (P2), entry `:8-9` bound loss (P2), the page-count mismatch (P2), `SKILL.md:389` (P3). The build could not see these.

## Residual risk and verification gaps
- The verdict applies the three bounds as written. If the lead accepts page scope as a bound, `:212` is still contradicted by sub-agents.md:729, so the sentence stays wrong either way.
- Two pages fetched once each with curl, no browser; no fetched content executed. Sub-agents page recorded at 15:22:38Z; skills page fetched in the next call, time not recorded separately.
- Not checked: omp's shipped docs; the phrase "from five clients" (depends on how vendors are grouped); the uncommitted working tree (not judged). Rerun this sweep on the committed head before landing.
- No verifier was run; the C1 and C2 counters are outside this item.

## Tools
- None installed or updated. No pacman use. Read-only git and curl into the scratch directory.

## Evidence (commands and exit codes)
1. Assigned sweep at the pin: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -i -e 'keyed on the name' -e 'documented remedy' -e 'only remedy' -e 'no client documents' 59903b2637689739a5b9901956301da72d0effe1 -- SKILL.md PROVINCE.md corpus/README.md corpus/knowledge SCORECARD.md AGENTS.md README.md` → exit 0, 9 hits: SKILL.md:379; corpus/README.md:72; census:301; levers:8, :9; round50:29, :40, :42, :86.
2. Phrasing sweeps at the pin, same file set, each exit 0: negatives ("no client", "no documented", "none documents", "documents no", "no rule", "no tie-break", "no documented tie"); "remedy|remedies|keyed"; "more specific description|specificity|description wording|sharpen|eight pages|eight client pages|only lever|only arbitration|only mechanism|only documented|only way|only fix|sole"; "rule between|differently named|both match|between two|overlapping description|tie-break|tiebreak|arbitrat|decides between|chooses between"; "supersede|withdrawn|author-written|superseded".
3. Subagent page: `curl -sS -L -o subagents.md -w 'http=%{http_code} bytes=%{size_download}\n' https://code.claude.com/docs/en/sub-agents.md` → http=200 bytes=110784; `sha256sum subagents.md` → 89aa73eb…; `grep -n -i -e deny -e disable -e disallow -e 'Agent(' subagents.md` → exit 0 (lines 83, 515, 729, 734, 1293).
4. Skills page: same method on `skills.md` → http=200 bytes=111557; sha256 cdfcb0df…; grep exit 0 (line 403, `paths`).
5. Round-50 seat text: `git grep -n -i -e disallowedTools -e 'Agent(' -e deny -e 'disable specific' 59903b2… -- .ufo/waves/round-50 …` → exit 0; hits only in `ReopenS024.md`.
6. HEAD check: `git rev-parse --short HEAD` → 533ff20; `git log --oneline 59903b2..HEAD` → one commit (533ff20); `git --no-pager --no-optional-locks status --porcelain` → exit 0: ` M SKILL.md`, ` M corpus/knowledge/skill-overlap-levers-round51.md`, ` M verifiers/verify_surfaces.py`, `?? .ufo/waves/round-51/`.
7. Disclosure: one earlier plain `git status --porcelain` ran without `--no-optional-locks` (read-only; may refresh the index stat cache). Nothing in the lane was edited.
8. Working-tree search (read-only search tool) on six tracked files: "only lever|only arbitration|documented remedy|Its remedy|author-written".
9. Committed-only check at 533ff20: `git grep -n -i -e 'only lever' -e remedy -e 'no client documents' -e 'keyed on the name' 533ff20 -- SCORECARD.md PROVINCE.md AGENTS.md README.md` → exit 0 (PROVINCE.md:17, SCORECARD.md:28, SCORECARD.md:31).

Scratch files: `/fast/scratch/hyaku/kotoba-r51/falsify/ReviewD3Sweep/` (`subagents.md`, `skills.md`). This report is the only lane file written.
