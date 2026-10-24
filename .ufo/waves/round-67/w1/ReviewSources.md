# ReviewSources — round 67

## Scope and measured state

The assigned draft `.ufo/waves/round-67/w1/drafts/SOURCES.rows.r67.md` was absent on repeated reads. Per the fallback instruction, I reviewed the three corresponding staged rows — S123, S124 and S129 — in `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`.

During the review, three transformed rows appeared in the lane working tree at `corpus/SOURCES.md:134-136`. I reviewed that actual diff as well. At measurement time, both `master` and `HEAD` resolved to the pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2`; the new rows were uncommitted working-tree additions, not a committed tip. Findings below target the current working-tree rows first, followed by the staged-only defects already resolved there.

I independently re-opened all three named sources on 2026-10-24 (each HTTP 200):

| row | fetched artifact | bytes | sha256 |
|---|---|---:|---|
| S123 | `https://model-spec.openai.com/2026-08-18` → `/tmp/k67-review-sources-S123.html` | 2,662,295 | `72db50e5063c3c8942671c3ce6e30d0dd643de558eefd690aab127ec53bf4e5a` |
| S124 | raw `skills/skill-creator/SKILL.md` at `dbd4588f9e1033efb41dad4bef2f7947c8993d44` → `/tmp/k67-review-sources-S124.md` | 33,168 | `dcd4803e61e913e6fc27294184cd3a71f09f5e924ff20c8a9a20173e7b3c2bcf` |
| S129 | `https://arxiv.org/abs/2604.09443` → `/tmp/k67-review-sources-S129.html` | 43,281 | `3d3ca32cdfb668da9f554f0a75070d4784db8a780393bbf74987700028b45209` |

## Findings by severity

### High

1. **S124's second `anchor` quote is not verbatim, and the same misquote has propagated into both citing documents.**
   - **Locations:** `corpus/SOURCES.md:135`; `corpus/knowledge/instruction-authority-ladder-round67.md:22-23`; `corpus/lessons/round-67.md:32`.
   - **Evidence:** all three quote `evaluates current description (running each query 3 times to get reliable trigger rate)`. The pinned source at `/tmp/k67-review-sources-S124.md:394` actually says `evaluates the current description (running each query 3 times to get a reliable trigger rate)`: the draft drops both `the` and `a`. A literal substring check against the fetched pinned bytes returned `False` for the drafted quote.
   - **Fix:** replace the quote in all three locations with the exact 15-word fragment `evaluates the current description (running each query 3 times to get a reliable trigger rate)`. This is verbatim and remains below the 25-word cap. S124's other quote, `Create 20 eval queries — a mix of should-trigger and should-not-trigger.`, is verbatim (11 words) and needs no change.

### Medium

2. **Two `teaches` cells claim more than their own `scope` and source support.**
   - **S123 — `corpus/SOURCES.md:134`:** the scope is explicitly OpenAI-only and disclaims any claim that a skill client implements the Model Spec, but `teaches` calls the ladder `the outer bound on what a skill body may assert`. The opened page assigns `No Authority` to assistant/tool messages and quoted/untrusted data (`/tmp/k67-review-sources-S123.html:2082-2091`); it does not make a ruling about `SKILL.md` bodies. The last teaches clause is therefore an unsupported cross-client application, not a fact inside the row's scope.
     - **Fix:** bound the cell to OpenAI, for example: `OpenAI's ordered authority levels, including No Authority for assistant/tool messages and quoted or untrusted data, and the rule that higher authority wins; application to a skill body requires a separate client-specific source.`
   - **S124 — `corpus/SOURCES.md:135`:** `teaches` says `the description field is the trigger mechanism`, dropping both the source's qualifier `primary` and its Claude scope. The pinned source says `The description field in SKILL.md frontmatter is the primary mechanism that determines whether Claude invokes a skill.` (`/tmp/k67-review-sources-S124.md:335`). The row's own scope also limits the claim to Anthropic.
     - **Fix:** use `For Claude, the description field is the primary invocation mechanism; Anthropic's trigger-evaluation loop uses 20 labelled queries, a 60/40 train/test split, 3 runs per query and up to 5 iterations.`

3. **S129 is collision-free but is not the next free id for this three-row append.**
   - **Locations:** `corpus/SOURCES.md:136`; the same staged id originates at `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:13`.
   - **Evidence:** the base registry ends at S122. After S123 and S124, the next unused id is S125; S129 skips S125–S128. `.ufo/waves/round-67/w1/controls/collision-count` contains `0`, but that proves only non-collision, not the separate next-free requirement. `corpus/lessons/round-67.md:67-72` likewise records only the collision rationale.
   - **Fix:** while these rows are still uncommitted additions, renumber the arXiv row S129 → S125 and re-point citations **by document (URL/anchor), not by arithmetic**. Affected lane references found are `corpus/knowledge/instruction-authority-ladder-round67.md:5`, `corpus/lessons/round-67.md:37,61,116`, and `corpus/README.md:125`. If `.ufo/waves/round-67/w1/drafts/SOURCES.append.r67.md:3` is used as the integration input, update it as well. After renumbering, the README's source shorthand can accurately be S123–S125; its current `S123-S129` range notation spans ids that have no rows.

## Staged-fallback defects and their disposition in the working tree

These were defects in the read-only staged rows. Do **not** edit the package; the required fix belonged to the adoption transform. The current working tree has already resolved the items in this table.

| staged location | defect observed in the fallback review | required fix / current disposition |
|---|---|---|
| `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:7,8,13` | `opened` was the campaign date `2026-10-23`, not this round's date. | Use `2026-10-24`; all three working-tree rows now do. |
| same lines | `recheck` contained cadence plus re-fetch prose, not a bare cadence. | Strip to a cadence and preserve the prose in the lesson Gate; the working-tree rows now contain bare `90d`. |
| same lines | `used-by` pointed at the package's `instruction-authority-ladder.md`, not the round-67 admitted path; S124 additionally pointed at the non-admitted `description-writing-and-trigger-testing.md`. | Point only to admitted citing knowledge/lesson paths. The working-tree rows point to `instruction-authority-ladder-round67.md` and `round-67.md`; both exist and cite their rows. |
| `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:13` | The quote `requiring models … instructions … 853 agentic tasks` used an ellipsis in place of source text and was not a verbatim substring; the anchor also omitted the record revision. | Use an unshaped ≤25-word quote and pin v4. The working-tree S129 instead uses the verbatim 17-word quote `assumes a fixed, small set of privilege levels (typically fewer than five) defined by rigid role labels` and records v4, resolving both defects. |
| `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:7` | The anchor invoked `The chain of command` but omitted that section's `No Authority` entry. | Record both the earlier five-level list and the chain-of-command addition; `corpus/SOURCES.md:134` now does so. |

The staged S123/S124 `teaches` overclaims and the S129 next-free issue persist in the transformed working tree and are therefore listed as current findings above rather than as resolved fallback items.

## Checks that passed on the current working-tree rows

- `corpus/SOURCES.md:134-136` each parse as exactly 11 columns (13 pipe-delimited fields), with zero escaped pipes and no literal cell pipe.
- All three have `status=mined`, `opened=2026-10-24`, and bare recheck cadences. Their two `used-by` paths exist and contain citations to the corresponding ids.
- Verbatim substring checks passed for S123's 9-word quote, S124's first 11-word quote, and S129's 17-word quote. Only S124's second quote failed.
- No S123/S124/S129 id or exact source-URL collision was found in the base registry. S012 is a same-tree neighbour for S124, not the same file URL.
- `git diff -- corpus/SOURCES.md` showed only the three new rows inserted after S122 and before `## Paths`; it showed no modification or deletion of an existing registry row. This is an uncommitted-diff observation, not a committed append-only-gate verdict.

## Residual risk and verification gaps

- The working tree changed while the review was running, and there is no final committed revision in this report. Re-run the quote, next-free-id, used-by and census checks on the final integration bytes.
- The assigned draft remained absent. The auxiliary `.ufo/waves/round-67/w1/drafts/SOURCES.append.r67.md` is not identical to the registry rows (including S129's tier/cadence and some anchor text), so it must not be substituted blindly; the current findings cite the registry version explicitly.
- Append-only safety was checked from the actual textual diff only. I did not claim a committed-range `check_sources_append_only.py` result because these additions were not committed at measurement time.
- Live-source evidence is the independently fetched `/tmp` set above; those temporary snapshots are not a committed source-snapshot bundle.

Report: .ufo/waves/round-67/w1/ReviewSources.md
