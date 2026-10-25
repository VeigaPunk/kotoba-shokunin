# ReviewC2Rows — S209, S210, S211 against SOURCES contract v1 (round 70, wave 1)

Seat: `L1Kotoba70.ReviewC2Rows` (reviewer, read-only). Rev measured: `16b212a390c7ce68b6bce49b2c3766b154fbcbae`
(`git rev-parse HEAD`). The working copy of `corpus/SOURCES.md` is clean: `git status --porcelain` lists only
untracked `.ufo/waves/round-70/w1*` paths. Contract: `/home/vgpnk/Projects/shokunin/CORPUS.md` § SOURCES.md (lines 64–151).

## Verdict

**Conformant on every rule the census can check, and on the quote, teaches, status and date rules. Two
low-severity nonconformances against the letter of the contract (not caught by the census):**

1. S209 and S210 `anchor` cells give an access date and a byte count instead of a revision.
2. S209 and S210 `source` cells cite the `.md` export URL, not the canonical URL the site declares.

Neither one changes the C2 reading. `check_skill_evals.py --fetch` prints `skill eval facts backed 8 of 8`
and `live quotes found 8 of 8`, exit 0.

## Census (CORPUS.md manual commands, run from the lane root)

| command | observed |
|---|---|
| rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | `137` (134 in census-before plus 3) |
| malformed `NF!=13` | `0` |
| tier histogram | `A=129 B=7 C=1` |
| status histogram | `mined=129 queued=7 rejected=1` |
| duplicate ids | (nothing) |
| enum / tier-inflation | (nothing) |
| mined used-by missing | (nothing) |

The maintained CLI agrees. `bash scripts/sources-census.sh validate kotoba-shokunin` (run from the fleet root)
prints `ok …/kotoba-shokunin/corpus/SOURCES.md` and exits 0. Its 18 `W04 duplicate url` warnings are all on
older rows (S018…S208). None is on S209–S211.

## Per-cell check

The per-row field dump `awk -F'|' '/^\|[[:space:]]*S(209|210|211)[[:space:]]*\|/ {print NF; …}'` gives
lines 150, 151 and 152, each `NF=13` with 11 non-empty cells.

- **No pipe inside cells.** NF=13 rules out raw pipes. Running
  `sed -n '150,152p' corpus/SOURCES.md | rg '\\\||&#124;|&vert;|｜|¦|│'` finds none of those variants. The only
  non-ASCII character is `—` (6 occurrences).
- **Append-only.** `git diff 7d51253f…16b212a3 -- corpus/SOURCES.md` shows `3 insertions(+)` at `@@ -149,0 +150,3 @@`
  and no other change.
- **kind/tier.** S209 and S210 are `docs`/`A`; S211 is `code`/`A`. All are valid enum values, and none is
  community-at-A. Each `scope` cell narrows the tier to the specification's guidance only, or to "one
  implementation, not the specification" for S211.
- **opened / recheck.** All three read `2026-10-25` / `90d`, both valid. The snapshots were committed in
  `53de0ac` on 2026-10-25 07:43 -0300. The lesson `## Gate` (`corpus/lessons/round-70.md:52-63`) records the URL,
  the 2026-10-25 access, and a located quote for each row.
- **status/used-by.** All three are `mined`, with `used-by` `corpus/knowledge/skill-eval-artefacts-round70.md`.
  The file exists, and its `source:` lines 1–3 cite S209, S210 and S211.

### Quotes (≤25 words, located)

The snapshot sha256 values match the counter pins (`sha256sum .ufo/waves/round-70/snapshots/*` gives `a799805f…`,
`7cc54fbb…` and `43e3b8f8…`). Live bytes are identical too: `curl` gives 16973 B / `a799805f…` and
13403 B / `7cc54fbb…`, and the raw file at `dbd4588` gives 11464 B / `43e3b8f8…`.

- **S209:** "The main file you author by hand is evals/evals.json." That is 9 words, matching the row's count.
  It sits at `S209-evaluating-skills.md:86`, under `## Running evals` (line 50) › `### Workspace structure` (line 54),
  directly after the tree that ends at line 84. The anchor is accurate. The snapshot has backticks around
  `evals/evals.json`, so the row's quote matches only after Markdown is stripped (informational).
- **S210:** "A should-trigger query passes … (0.5 is a reasonable default)." That is 17 words, matching. It is at
  `S210-optimizing-descriptions.md:92`, under `## Testing whether a description triggers` (line 77) ›
  `### Running multiple times` (line 88). The anchor is accurate.
- **S211:** "did_pass = trigger_rate >= trigger_threshold" is 5 whitespace tokens. It is at `S211-run_eval.py.txt:232`.
  The `should_trigger` branch spans lines 230–234 (from `should_trigger = item[...]` to `did_pass = trigger_rate < …`).
  The argparse defaults are at `:266` (`--runs-per-query … default=3`) and `:267` (`--trigger-threshold … default=0.5`).
  The anchor is accurate. The lesson gives the narrower range 231–232, which is consistent with the row. The unit
  label is "(5 tokens)" where the other rows say "(N words)" (informational).
- **S211 revision.** `git ls-remote https://github.com/anthropics/skills HEAD refs/heads/main` prints `dbd4588f…`
  for both refs, which confirms "equal to main on 2026-10-25". The blob URL returns HTTP 200.

### teaches grounded

- **S209.** "evals/evals.json inside the skill directory" is at `:19` ("Store test cases in `evals/evals.json`
  inside your skill directory"). "with and without the skill" is at `:52`. "PASS or FAIL with quoted evidence"
  is at `:170` ("The evidence should quote or reference the output").
- **S210.** `should_trigger` appears at `:36-37` and `:85-86`. "about 3 times" is at `:90` ("3 is a reasonable
  starting point"). The threshold 0.5 is at `:92`. The held-out validation split is at `:136-161`.
- **S211.** `>=` at the 0.5 default is at `:232` and `:267`, and 3 runs is at `:266`. "Disagrees only at an even
  run count" is an arithmetic derivation, not a quote: k/n = 0.5 only when n is even. The should-not-trigger
  sides agree, since the spec says "below" (`S210:92`) and the code uses `<` (`:234`). The claim holds because the
  cell scopes it to "the 0.5 threshold". At a non-default threshold (for example 1/3 with n = 3) the two would
  disagree at an odd count too. This is grounded as scoped; I flag it only as a derived claim with no quote.

## Findings (by severity)

### LOW-1 — S209 and S210 `anchor`: no revision (cell `anchor`, lines 150–151)

The contract (`CORPUS.md` § SOURCES.md, `anchor`) requires "exact section … plus revision (version, commit, or
publication date)". S209 has "(page fetched 2026-10-25, 16 973 B)" and S210 has "(page fetched 2026-10-25,
13 403 B)". Those are an access date (which the `opened` cell already carries) and a size, not a revision.

- The live server offers no revision. `curl -D` shows `last-modified: Sun, 25 Oct 2026 11:57:36 GMT`, which
  equals the request time, so the header is dynamic.
- An upstream commit revision was obtainable:
  - `api.github.com/repos/agentskills/agentskills/commits?path=docs/skill-creation/evaluating-skills.mdx&per_page=1`
    gives `7d9e51a92ac788b0247e7c9b968c8e0c22885c0a` (2026-03-13).
  - The same query for `optimizing-descriptions.mdx` gives `b8d2613ac050aa4aa8bfb2cf28380d81cdfcd1ca` (2026-04-19).
  - The raw `.mdx` at those commits contains both quotes: `e.mdx:84` "The main file you author by hand…" and
    `o.mdx:89` "A should-trigger query passes if its trigger rate is above a threshold…".
- The snapshot sha256 pinned in the C2 counter does fix the bytes, but the anchor cell does not name it.

Mitigation: S001 and S002 ("live page opened 2026-10-19") set the same precedent, so this is an inherited lane
convention, not one this round introduced. Under rule 2 the cell cannot be edited in place. The repair is a
superseding row, or a contract-version decision on whether a sha-pinned snapshot counts as a revision.

### LOW-2 — S209 and S210 `source`: non-canonical URL (cell `source`, lines 150–151)

The contract requires "title — canonical URL". Both rows cite the `.md` export
(`…/evaluating-skills.md`, `…/optimizing-descriptions.md`). The pages declare otherwise:
`curl -L https://agentskills.io/skill-creation/evaluating-skills` returns `<link rel="canonical"
href="https://agentskills.io/skill-creation/evaluating-skills"/>`, and the same holds for
`optimizing-descriptions`.

The lane is inconsistent on this. For agentskills.io, S018 cites the canonical `https://agentskills.io/specification`
and records "fetched as …/specification.md" in its anchor, and S001 and S002 also use canonical URLs. S209 and S210
break that same-domain pattern. Lane-wide, though, 69 rows cite `.md` URLs (from the awk sweep over `$3 ~ /\.md/`:
S032…S124, S198, S202, S209, S210). So the rows match one lane habit and contradict another. The repair takes the
same route as LOW-1.

### Informational (not nonconformances)

- The S211 quote counts in "tokens" where the other rows count in "words".
- The S209 row quote drops the backticks the page has; it matches only after the counter's normalisation.
- The second half of S211 `teaches` is derived arithmetic, scoped to 0.5 (see above).

## Residual risk and verification gaps

- **Spot-check scope.** I re-opened all three rows live. I did not re-open S301, S285/S286 or S303 (the
  refusals); they are outside this item.
- **Who opened the sources.** Whether the L1 actually opened the sources in-round rests on the committed snapshots,
  their 2026-10-25 commit time and the live byte equality. I have no access log of the L1's own fetch (unobserved).
- **Commit coverage.** For the upstream `.mdx` I checked only the latest commit per path, through the
  unauthenticated GitHub API. I did not show that the rendered `.md` derives from exactly that commit; the `.md`
  and `.mdx` sizes differ (16973 vs 16755 B).

## Commands used (all read-only; scratch `/tmp/k70w1-ReviewC2Rows.uMlk`, deleted)

The seven CORPUS.md census commands verbatim; `awk -F'|'` field dump of S209–S211; `sha256sum` of the snapshots;
`rg -n` over the snapshots; `git diff 7d51253f…16b212a3 -- corpus/SOURCES.md`; `curl -sS -D` on both
agentskills.io `.md` URLs and the canonical pages; `git ls-remote` on anthropics/skills and agentskills/agentskills;
raw fetch of `run_eval.py` at `dbd4588`; GitHub commits API and raw `.mdx` at `7d9e51a`/`b8d2613`;
`python3 -B verifiers/check_skill_evals.py --rev 16b212a3… --fetch` (exit 0);
`bash scripts/sources-census.sh validate kotoba-shokunin` (exit 0). No tools installed or upgraded.
