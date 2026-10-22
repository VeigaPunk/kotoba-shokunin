# RowKamaR50: round-50 kama adjacency ruling (falsify)

**Verdict: HOLDS-BOUNDED** for kama's `adjacent` class (basis sibling) at kotoba `956ee1676e4c18480bce8ac3993541462be76e11`. The class holds only through the census precedence excuse (census.md:256-260), which the ruling states but does not use. The ruling's stated reasoning FAILS on the pinned bytes: "judges no wording" is false, and the cited rows are historical by kama's own Errata. The row's clause "so it is no claim on kotoba's Core" is false as written.

Judged: kama `c808ba07f09c4be55413d3d6516c542ab69b64f8`, read with `git show` (no checkout, nothing written there). Scope: census entry § Round 50 (census.md:246-270), PROVINCE.md:44 (kama row), consumer-registry.md:91-92, 111-112, 325-326, cross-lane-scope.md:29. Scratch copies: `/fast/scratch/hyaku/kotoba-r50/falsify/RowKamaR50/`.

## The three questions

1. **Are the quotes verbatim at the cited lines?** The split is verbatim at cross-lane-scope.md:29 once bold markers are removed. census.md:268-269 quotes the whole sentence. PROVINCE.md:44 quotes a prefix that stops mid-sentence at "independent verification", with no ellipsis: a truncation, not a misquote. The ruling's own sentence ("verifies endpoint values and absences in instruction files and judges no wording", census.md:266-267) is a paraphrase. Its present-tense "verifies" fails (F2) and its "judges no wording" fails (F1). Every cited line number points at the right text.
2. **Does the reasoning hold on the bytes?** No, as written (F1-F4). The row survives on a different ground: kama's own split assigns the judged wording to kotoba, so any claim is excused.
3. **Would claim-always-wins (a claim makes the row contested, whatever the split says) change the row?** Yes, on the living kama text. kama becomes `contested`. C1's counter does not move (contested is non-none, so 9 of 9 either way). See F5.

## Findings

**F1 (High). "They judge no wording" is false on the pinned bytes.** Kama's registry and corpus judge the fallback statements:
- consumer-registry.md:91: "it is the only consumer with *no* fallback" (about janitor.md:20-21; owner column `kotoba [INFERENCE]`).
- consumer-registry.md:92: "**cascade-protected**: the cloud tail survives the 8080 break; janitor (#2) does not" (about distiller.md:7).
- cross-lane-scope.md:14 (not cited by the ruling): "The cloud cascade can mask an outage for the caller."
- cross-lane-scope.md:47 (not cited): recommends "synchronizing janitor.md's literal URL" and "retaining distiller.md's cloud cascade."
- corpus/knowledge/listener-census.md:110-111 (not cited): "NO — drift, no fallback" and "NO — drift, cascade-protected" (header: "Measured: 2026-09-28").
- Round 49 read these same registry rows the other way. census.md:182-186: they "audit agent prompt text and record a verdict on a sibling SKILL.md … a possible `contested` element … row stays `adjacent`." Round 50 reverses that with no new bytes and gives no reason.

**F2 (High). The cited rows describe no present state, and the ruling does not say so.**
- consumer-registry.md:56-58: `~/.config/opencode/agents/` is "Deleted since round 2".
- consumer-registry.md:64-65: "Rows #1-#11 … are therefore historical." Rows 91-92 are #2 and #3.
- consumer-registry.md:72-74: "Every `MODEL_OK`/`FOREIGN_SERVICE` verdict in the table is historical." This covers rows 111-112. Today's check reads `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2`.
- corpus/README.md:54 (the row's own cite): "all three files are deleted or emptied."
- Live, 2026-10-22: `ls ~/.config/opencode/agents/distiller.md ~/.config/opencode/agents/janitor.md` gives "No such file or directory" for both, exit 2.
- So "verifies endpoint values in instruction files" is false for rows 91-92 and for the `agents/` branch of row 325.

**F3 (Medium). Rows 111-112 cannot bear on kotoba's row.** They are kengaku's files: kengaku-shokunin/SKILL.md:322-323 and PROVINCE.md:14. They check endpoint values in another lane's files, which census.md:254-255 excludes from "claim." They say nothing about kotoba's wording.

**F4 (Medium). The excuse, not the premise, keeps the row `adjacent`.**
- The contested arm covers "writing or auditing other lanes' SKILL.md, prompts or AGENTS.md-class files" (census.md:45-46). Agent definitions are kotoba's Core (PROVINCE.md:13).
- The endpoint carve-out (census.md:254-255) covers the verdicts in 111-112. It does not cover the fallback judgments in 91-92 and cross-lane-scope.md:14, or the cascade-retention sentence in :47.
- The precedence rule (census.md:256-260) excuses a claim when the sibling's own split assigns the element. Kama's split does: cross-lane-scope.md:13 ("**Kotoba:** agent/instruction surface, including the model and no-fallback claims"), :14 ("**Kotoba:** the agent file and declared primary/fallback policy"), :29 and :41.
- So the class holds because claims exist and are excused. "No claim on kotoba's Core" is false. Correct wording: kama's registry and cross-lane-scope judge agent-file fallback statements; kama's own split assigns those to kotoba; the arm does not fire.

**F5 (Medium). Claim-always-wins flips the row, on living text.**
- Strongest trigger: cross-lane-scope.md:47. Its URL half can be read as an endpoint value (carved out). Its "retaining distiller.md's cloud cascade" half is a fallback-policy verdict (not carved out). cross-lane-scope.md:14 is a second trigger.
- Rows 91-92 trigger the flip only if read as live. The registry labels them historical, so the census must choose a reading, and the ruling does not choose.
- If the row flips: census.md:265 ("9 adjacent, 11 none, 0 contested") becomes 8 / 11 / 1 (arithmetic on census.md:265, not run). PROVINCE.md:44 changes class. The census and PROVINCE must change together, because the `--province` guard checks that they agree. C1 is unchanged.
- If cross-lane-scope.md:47 is read as an endpoint-only note, nothing flips today.

**F6 (Low). Citation and basis details.**
- PROVINCE.md:44 "basis sibling": census.md:261-262 says the round-50 description edit "adds kotoba's side for … kama." The judged SKILL.md description now says "kama owns endpoint verification" (frontmatter, sibling-boundary sentence). At 956ee the basis is "both." "Sibling" is the base-commit basis.
- PROVINCE.md:44 "the agent files it names were deleted … per kama corpus/README.md:51-55": the README names janitor.md, opencode.json and the-janitor. distiller.md's deletion is recorded only at consumer-registry.md:56-58.
- consumer-registry.md:326 "no matches" for `~/.agents`: the same pattern now returns one live hit, `/home/vgpnk/.agents/skills/unreal-mcp/references/setup.md:75` (`"url": "http://127.0.0.1:8000/mcp"`). That is an MCP URL, not a model endpoint, so the model-endpoint verdict stands, but the literal "no matches" does not.

**F7 (Residual risk). Ownership is still open in the fleet's own tables.** PROVINCE.md:41 (kagi): "the opencode config group owner is unresolved and stays with the integrator." census.md:125-127 records `owner=integrator, status=unresolved`. The round-49 section (census.md:158-161) calls kotoba "a wording claimant" there and files the opencode config item as an operator question. The kama row rests on kama's own split for that wording. The rule allows that excuse, but the item is not closed.

## Recommended re-rule (not applied; for the integrator)
- Replace the reasoning with the excuse: kama's registry and cross-lane-scope judge agent-file fallback statements (consumer-registry.md:91-92; cross-lane-scope.md:14); kama's split assigns those to kotoba (cross-lane-scope.md:13, 14, 29); the arm does not fire.
- Drop "no claim on kotoba's Core," or qualify it as above.
- Cite only live text, or state that the rows are historical.
- Basis: "both" (kama's split; kotoba's description "kama owns endpoint verification").
- Decide whether cross-lane-scope.md:47 is live, and say how claim-always-wins treats it.
- Fix the PROVINCE.md:44 truncation, the README cite (janitor.md only) and the `~/.agents` literal in row 326.

## Evidence (commands and exit codes)
- `git -C /home/vgpnk/Projects/shokunin/kama-shokunin show c808ba07f09c4be55413d3d6516c542ab69b64f8:<path>`, exit 0 for: corpus/knowledge/consumer-registry.md (413 lines, 42,709 B, sha256 c577e615…2932); corpus/knowledge/cross-lane-scope.md (87 lines, 21,286 B, sha256 1801cb7f…28a9); corpus/README.md (389 lines, sha256 cbbfe6c6…); corpus/knowledge/listener-census.md (exit 0); MINT.md (67 lines).
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 956ee1676e4c18480bce8ac3993541462be76e11:<path>`, exit 0 for: PROVINCE.md (56 lines, sha256 a6c12cdc…); corpus/knowledge/sibling-overlap-census-round49.md (295 lines, sha256 40ea8f98…); SKILL.md (539 lines, sha256 9fe2ca74…).
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse --verify --quiet 956ee1676e4c18480bce8ac3993541462be76e11^{commit}`, exit 0, same hash.
- Line reads: `read` on the scratch copies at the ranges cited above.
- `git -C .../kama-shokunin grep -n -i kotoba c808ba07… -- ':!*.patch' | head -60`: pipeline exit 141 (SIGPIPE from `head`). Partial; no count is taken from it.
- `grep -rEn 'localhost:[0-9]+|127\.0\.0\.1:[0-9]+' ~/.agents ~/.config/opencode`: exit 0, one hit (`~/.agents/skills/unreal-mcp/references/setup.md:75`).
- `ls ~/.config/opencode/agents/distiller.md ~/.config/opencode/agents/janitor.md`: exit 2, both "No such file or directory".
- `wc -l ~/.config/opencode/opencode.json` gives 5. `grep -c 8080 ~/.config/opencode/opencode.json` gives 0 (exit 1).

## Tooling
Nothing installed or updated. Used host tools already present: git, grep, sed, awk, sha256sum, wc, ls.

## Not run and residual limits
- The C1/C2 counters, the census guard and the box-proof driver were not run (outside this seat).
- Flip counts (8/11/1) are arithmetic on census.md:265, not a guard run.
- The live checks cover only the paths named above, on this workstation. They are present-day readings, not a pin-level proof.
- Writes: only my scratch directory and this report.
