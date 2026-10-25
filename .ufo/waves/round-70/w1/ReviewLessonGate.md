# ReviewLessonGate — round 70 wave 1 (reviewer, read-only)

**Verdict: the Gate is not conformant as written. There are 2 medium and 5 low findings. The mechanics are clean.**

The Gate does satisfy the mechanical rules:

- Every new row (S209, S210, S211) carries a URL, an access date and a located quote of 25 words or fewer.
- The renumber map is correct by document.
- The collision, guard-proof and quarantine files reproduce byte-exact.
- At least one admit and at least one reject are recorded.
- CORPUS.md rule 2 holds: the only registry change since the base is three appended rows.

The defects are in what the refusals assert and in one receipt that cannot be reproduced. One of these is the reject the Gate itself suggests the closure spot-check (S301). The other is a refusal whose flip condition would admit an entry that is already contradicted.

Scope: `corpus/lessons/round-70.md` § Gate (lines 31–108), checked against `CORPUS.md` § SOURCES.md rules 1, 2 and 4, and the prompt `.ufo/prompts/kotoba-round-70.md` §6 item 10 (lines 390–495). Lane HEAD is `16b212a390c7ce68b6bce49b2c3766b154fbcbae` and the base is `7d51253f`. Scratch was `/tmp/k70w1-ReviewLessonGate.TotO`, now deleted. Network fetches were read-only GETs. Nothing was written to, run inside or fetched into `/home/vgpnk/Projects/shokuknow`. No tools were installed.

## Findings by severity

### MEDIUM-1 — The refusal of `english-leads-relocated-round9.md` rests on a weaker reason than the lane already holds, and its flip condition would wrongly admit the entry. The Gate also calls an opened page "unopened".

The Gate (lines 85–90) refuses the staged entry with this reasoning: "its central claim is a negative over a whole vendor's documentation … this round ran no bounded sweep". The flip condition is "a logged, bounded sweep of OpenAI's docs index". It adds that the OpenAI page "Testing Agent Skills Systematically with Evals" "stays a lead, unopened".

The staged entry's central claim is that the page "does not exist" and that OpenAI "never" publishes the protocol:

```
grep -n 'does not exist\|never that protocol' /home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/english-leads-relocated-round9.md
→ 2:# The should_trigger protocol is the specification's and Anthropic's; OpenAI publishes skills but never that protocol
→ 13:Agent Skills Systematically with Evals". That page does not exist. …
```

The lane's own registry already holds that page as a **mined** row, opened 2026-10-22:

```
git show HEAD:corpus/SOURCES.md | grep -n '^| S066 '
→ 79:| S066 | OpenAI Developers — Testing Agent Skills Systematically with Evals — https://developers.openai.com/blog/eval-skills.md | docs | A | … sha256 `6cf414bb3e2dddfd940e3ea3293ce588f777e80a7d935cf8a73d9f5cfb94d3a2` … | mined | 2026-10-22 | 90d | corpus/knowledge/explicit-invocation-round55.md, corpus/lessons/round-55.md |
```

Today the live page is byte-identical to that pin, and it carries `should_trigger`:

```
curl -sSL -o oai -w '%{http_code} %{size_download}\n' https://developers.openai.com/blog/eval-skills.md   → 200 19356
sha256sum oai                                                                                            → 6cf414bb3e2dddfd940e3ea3293ce588f777e80a7d935cf8a73d9f5cfb94d3a2
grep -n 'should_trigger' oai                                                                             → 162:id,should_trigger,prompt
```

The refusal outcome is right, but for three reasons the Gate states it badly:

- **Wrong reason.** Q62 (`corpus/QUALITY.md:78`) asks a refusal to rest on an observed fact. The lane has one: the page exists at S066's URL, sha-identical to the round-55 pin, and line 162 carries `should_trigger`. The Gate instead gives "no sweep was run".
- **Miscalibrated flip.** A bounded sweep cannot make a contradicted claim true. The flip should be the claim itself becoming true, for example the S066 URL stops serving `should_trigger`. As written, the flip invites a later round to admit a false entry.
- **False "unopened".** The page was opened in round 55 (S066). The `corpus/SOURCES.md` § Leads (unopened) bullet at lines 234 and 276 is stale, and the Gate repeats it as fact.

Fix: append a correction to the lesson that restates the refusal reason as the observed S066 fact and changes the flip. Optionally, retire the stale Leads bullet in an appended note.

### MEDIUM-2 — The flip condition of the S301 refusal is false: S209 does describe blind comparison. This is the Gate's own suggested reject sample.

Gate line 81 reads "Flip: an entry about blind comparators, which S209 does not describe." The pinned S209 snapshot contradicts it:

```
grep -n -i 'blind' .ufo/waves/round-70/snapshots/S209-evaluating-skills.md
→ 214:> For comparing two skill versions, try **blind comparison**: present both outputs to an LLM judge without revealing which came from which version. …
```

The rest of the S301 refusal checks out. The S301 quote is on the live page:

```
curl -sSL -A 'Mozilla/5.0' -o l301 https://claude.com/resources/articles/improving-skill-creator-test-measure-and-refine-agent-skills
sed -e 's/<[^>]*>/ /g' l301 | grep -o -i '.\{60\}comparator.\{120\}'
→ … We&#x27;ve also added comparator agents for A/B comparisons: two skill versions, or skill vs. no skill. They judge outputs without knowing which is which …
```

The page also dates itself `March 3, 2026` (2 hits) and `2026-03-03` (4 hits).

The refusal is in fact stronger than stated: the tier-A S209 already covers blind comparison, so the tier-B S301 adds nothing even on that topic. But the stated flip would never fire, because a blind-comparator entry would cite S209 rather than S301. Line 108 nominates S301 as the reject sample for the non-author closure, so the closure will land on this false sentence. Fix: append a correction with a flip that can fire, for example "an S301 claim that S209 lacks, such as a tool-specific behaviour, enters an admitted entry".

### LOW-1 — The census receipt cannot be reproduced from the committed mirror.

The receipt `assimilation/census-validate-append.txt` says `exit=0` and names `…/assimilation/validate/corpus/SOURCES.md` on its `ok` line. Its header describes the mirror as "lane corpus/ … + SKILL.md + the admitted entry", and Gate lines 97–101 say the same. At HEAD, however, the mirror holds only three files:

```
git ls-tree -r --name-only HEAD -- .ufo/waves/round-70/assimilation/validate
→ validate/corpus/QUALITY.md  validate/corpus/README.md  validate/corpus/SOURCES.md
```

Rerunning the census on a `git archive` copy of the committed mirror fails:

```
git archive HEAD .ufo/waves/round-70/assimilation/validate | tar -x -C $T/m1
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file $T/m1/.ufo/waves/round-70/assimilation/validate/corpus/SOURCES.md
→ (E11 'missing used-by' for every mined row, S001 … S211)   exit=1
```

A mirror rebuilt from HEAD `corpus/` plus `SKILL.md` passes, and the lane-level gate passes too:

```
git archive HEAD corpus SKILL.md | tar -x -C $T/m2; sources-census.sh validate --file $T/m2/corpus/SOURCES.md   → ok, exit=0
sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba                                              → kotoba ok, exit=0
```

So the substance holds, but the committed receipt points at bytes that no longer show it.

Ordering is also unproven. The rows and the receipt land in the same commit, so "validated before the rows were committed" cannot be seen in history:

```
git log --format=%h -S'| S209 |' -- corpus/SOURCES.md                                                          → 8edeb49
git log --format='%h %ad' --diff-filter=A -- .ufo/waves/round-70/assimilation/census-validate-append.txt     → 8edeb49 2026-10-25 08:43:43 -0300
```

The receipt's file mtime is 08:50:19, which is later than the commit. That is not proof either way (jj can rewrite mtimes), so the order is unobserved. Fix: commit the full mirror, or re-word the receipt to "mirror = HEAD `corpus/` + `SKILL.md`, rebuild with `git archive`".

### LOW-2 — "Every claim it makes was re-opened on S209" over-states the admit and hides one contradicted claim.

Gate lines 65–66 say this of the staged `spec-eval-file-format.md`. The staged entry, however, also makes an S210 claim ("a description carries the entire burden of triggering"; S210 snapshot line 17). It also makes one claim that S209 contradicts:

```
grep -n 'travels with the skill' …/merge/kotoba/knowledge/corpus/knowledge/spec-eval-file-format.md
→ "the rest are produced by the run — grading.json, timing.json and benchmark.json — so the evaluation record travels with the skill"
sed -n 56p .ufo/waves/round-70/snapshots/S209-evaluating-skills.md
→ Organize eval results in a workspace directory alongside your skill directory. …
```

The S209 tree (lines 58–83) places `grading.json`, `timing.json` and `benchmark.json` under `csv-analyzer-workspace/`, outside the skill. The lane's entry correctly does **not** repeat the error: `skill-eval-artefacts-round70.md:30-31` says only that `evals/evals.json` travels with the skill. The Gate should still record that the staged claim was dropped as contradicted rather than imply that every claim was confirmed.

### LOW-3 — The stripped recheck prose is quoted inexactly for S234 and not recorded for S231.

Gate lines 92–94 quote S234's prose as "…the script-over-LLM-judgment rule…". The staged row cell reads differently:

```
awk -F'|' '/^ {0,3}\|[[:space:]]*S(234|231)[[:space:]]*\|/ {print $2 "::" $11}' …/SOURCES.append.md
→ S231 :: 90d — re-fetch the `.md` and confirm the 20-query / 8-10 / near-miss figures are unchanged (ran 2026-10-23)
→ S234 :: 90d — re-fetch the `.md` and confirm the four JSON file names and the script-over-LLM rule are unchanged (ran 2026-10-23)
```

The "-judgment" wording comes from the staged *entry's* `recheck:` line, not from the row. For S231 the Gate writes only "prose cadence → 90d". The contract (prompt lines 450–451) asks that "the stripped prose (re-verify conditions …) [be] recorded in the round lesson's Gate block", and the S231 condition (20-query / 8-10 / near-miss) is not recorded.

### LOW-4 — Some `teaches` cells claim more than their Gate quotes ground.

Rule 1 asks for a quote "grounding `teaches`":

- **S209** teaches "inside the skill directory … run with and without the skill". The Gate's quotes (lines 52–55) cover the `evals.json` artefact and PASS/FAIL with evidence. They do not cover the with/without run, which is at S209 line 52 ("run each test case twice"), or the location, which is at line 19 ("inside your skill directory").
- **S210** teaches "run about 3 times each … with a held-out validation split". The Gate quotes only the 0.5 pass rule (S210 line 92).

The facts are on the pages; the Gate simply does not quote them.

### LOW-5 — The S211 line span is inconsistent across documents.

The Gate (line 62) gives "lines 231–232", while the row and the entry say "lines 230-234". The snapshot shows:

```
grep -n 'did_pass' .ufo/waves/round-70/snapshots/S211-run_eval.py.txt   → 232: did_pass = trigger_rate >= trigger_threshold / 234: …< trigger_threshold
```

Both spans contain line 232, so this is cosmetic only.

## Checks that passed (reproduced)

| Gate claim | Command | Observed |
|---|---|---|
| reg-ids is 134, staged-ids is 188, collisions are S203–S208 | 0–3-space extractor on `git show 7d51253:corpus/SOURCES.md` and on staged `SOURCES.append.md` (sha256 `e2bdff3f…`, mtime 2026-10-24 23:33) | 134 / 188 / 6; `cmp` matches all three committed files byte-exact |
| Guard proof | 0–3-space extractor on `guard-proof/SOURCES.md`, then `comm -12` with staged-ids; `grep -cE '^\|[[:space:]]*S234'` | `S234` (matches `guard-proof/collisions`); column-zero count 0 |
| Renumber by document | `grep` of staged S234 and S231 | S234 = `…/evaluating-skills.md` → S209; S231 = `…/optimizing-descriptions.md` → S210 |
| Rule 1 rows | Gate lines 52–63 against the snapshots | S209 quote at snapshot line 86, under `## Running evals` (line 50), after the tree (lines 58–84); S210 at line 92 under `### Running multiple times` (line 88); S211 at line 232; word counts 9, 17 and 5 tokens |
| Snapshots equal the live sources | `curl` the three URLs plus `sha256sum`, and `git ls-remote …/anthropics/skills refs/heads/main` | `a799805f…`, `7cc54fbb…`, `43e3b8f8…` match the snapshots and the counter pins (`verifiers/check_skill_evals.py:48-54`); sizes 16973, 13403 and 11464 B; main = `dbd4588f…` |
| S285/S286 duplicate S209/S210 | Fetched both `.mdx` files (200, 13151 B and 16755 B); stripped `` ` `` and `*` | All four Gate quotes for S209/S210 are present verbatim in the `.mdx` files |
| S303 lines 64 and 68 | `curl …/dbd4588…/improve_description.py`, then `grep -n should_trigger` | `64: if r["should_trigger"] and not r["pass"]`, `68: if not r["should_trigger"] and not r["pass"]` |
| Quarantine slice (13 rows) | The prompt's awk over the register | `cmp` matches `assimilation/quarantine-slice`; 7 payload-absent and 6 could-not-fetch |
| At least 1 admit and at least 1 reject | Gate lines 65–90 | 1 admit (an entry) and 4 refusal groups |
| Rule 2: append-only | `git diff 7d51253 HEAD -- corpus/SOURCES.md` | Only `+` lines are S209, S210 and S211; no `-` lines |
| No stale staged ids in lane bytes | `git grep -E '\bS(234\|231\|285\|286\|301\|303)\b' HEAD -- corpus SKILL.md verifiers` | Prose mentions labelled "staged" only; no citation |
| shokuknow untouched | `find merge/kotoba .ufo/waves/corpus-expansion-1 -newermt '2026-10-25 06:00 -0300'` | No files |

## Residual risk and verification gaps

- **New package collisions.** The lane's new S209, S210 and S211 now collide with the package's staged S209 (ManyIH), S210 (SkillRouter) and S211 (SkillsBench), which are different documents. At HEAD the extractor gives 9 collisions instead of 6. The renumbering was correct by the contract (ids continue the lane registry), but the Gate does not warn a later round that those three staged rows now need renumbering.
- **PROVINCE scope.** The claim that "tameshi owns the fixture and mutation method" was checked only against this lane's `PROVINCE.md:68`. Tameshi's own `PROVINCE.md` was not opened.
- **Ordering.** Whether the census validation happened before the rows were committed is unobserved (see LOW-1).
- **Not covered.** I did not re-run `check_skill_evals.py`, the C1 counter, or any no-harm gate; those belong to other seats.
