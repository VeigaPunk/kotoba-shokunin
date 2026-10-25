# RevC2Counter — round 70 wave 1 review of `verifiers/check_skill_evals.py` (C2)

Seat: `L1Kotoba70.RevC2Counter` (reviewer, read-only). Lane tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae`.

## Verdict

**The counter does what it declares, and its readings reproduce.** The tip reads `8 of 8` (exit 0), the base reads `0 of 8` (exit 1), the self-test passes 13 of 13, and the counter is byte-identical to the freeze commit. The live pages also match the pinned snapshot hashes today.

**But the counter is looser than its name.** It counts quotes found on the pinned snapshots, not facts. Eleven sandbox worlds keep `8 of 8` with exit 0 while one of the following is wrong:

- the fact text (inverted or deleted);
- the meaning of a quote;
- the `SKILL.md` citation (negated, hidden in a comment, or inside a code fence);
- the `source:` line (negated, inside a code fence);
- the SOURCES rows (wrong URL, kind or tier; negated `used-by`; a refused row shadowed by a later duplicate).

The lane's own history already shows the first kind of slip passing: at `8edeb49` the F2 fact said the opposite of the page's qualifier, and the counter read `8 of 8` (finding 2).

The exit codes do not match the docstring in two places. A tampered snapshot is checked lazily, so it can exit 1 instead of 2. Some environment faults (a missing git object, no `git` on `PATH`) exit 1, the same code as a content verdict.

**What this means for C2:** the counter is frozen and no item may be narrowed after data, so C2 stands as measured (`8 of 8`). The holes below are the residual risk the non-author spot-check has to cover by reading the entry, and the specification for the next counter.

## Baseline runs (all from the lane root)

```
$ python3 -B verifiers/check_skill_evals.py --self-test
PASS honest world: backed 8 of 8
PASS broken world rejected: junk control … -> backed 0
PASS broken world rejected: forged control … -> backed 0
… (11 broken worlds rejected, tampered snapshot raises)
self-test: 0 failure(s) over 13 assertions
exit=0

$ python3 -B verifiers/check_skill_evals.py --rev 16b212a390c7ce68b6bce49b2c3766b154fbcbae
measured-rev: 16b212a390c7ce68b6bce49b2c3766b154fbcbae
skill eval facts backed 8 of 8
exit=0

$ python3 -B verifiers/check_skill_evals.py --rev 7d51253f99906b8551b6a0a108761eedac00de74
measured-rev: 7d51253f99906b8551b6a0a108761eedac00de74
skill eval facts backed 0 of 8
  entry corpus/knowledge/skill-eval-artefacts-round70.md absent
exit=1

$ git log --oneline 7d51253f..16b212a3 -- verifiers/check_skill_evals.py
53de0ac round-70: frozen plan, two counters …          # only the freeze commit; diff 53de0ac..16b212a3 is empty

$ python3 -B verifiers/check_skill_evals.py --rev 16b212a3… --fetch
skill eval facts backed 8 of 8
live quotes found 8 of 8
exit=0

$ curl … | sha256sum    # live bytes vs the pins in SNAPSHOTS (check_skill_evals.py:46-57)
43e3b8f8…657f (S211)  a799805f…b684 (S209)  7cc54fbb…d837 (S210)   # all three equal the pins
```

## How the hole worlds were built

Sandbox: `mktemp -d /tmp/k70w1-RevC2Counter.XXXX`, then `git clone --shared` of the lane, detached at the tip. Each world is one commit on top of `16b212a3`, run with the frozen lane counter:

```
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_skill_evals.py --repo <sandbox> --rev <world-sha>
```

The driver scripts (`worlds.py`, `exits.sh`, `census.py`) lived in the sandbox and were deleted with it. Every mutation is described exactly below, so each world can be rebuilt by hand. Before trusting the results I checked each world's diff with `git show --stat` and `git show`; for example, the `SKILL.md` in the negated-citation world contains the entry path exactly once, only as part of the `.retired` path.

## Findings, by severity

### High

**1. The fact cell is never read; any fact text passes, including the opposite of the quote.**
`check()` reads only the `S###` and the quote from `cells[1:]` (`check_skill_evals.py:144-145`). The fact sentence is never compared with anything. The plan says "Fact Fi … is backed", but N counts on-snapshot quotes. The docstring's trust boundary (`:23-25`) disclaims "the entry's prose around the quote", yet the fact cell is the fact itself, not surrounding prose.

- World `fact_inverted`: the F7 fact becomes "A should-trigger query passes only when its trigger rate is BELOW 0.5; the threshold is 0.9 by default." The F8 fact becomes "The reference implementation and the specification agree exactly; there is no `>=` gap."
  → `skill eval facts backed 8 of 8`, exit=0.
- World `fact_cell_dropped`: every fact row becomes `| Fi | S2xx | "quote" |`, with no fact text at all.
  → `8 of 8`, exit=0.

**2. A quote can be any on-page substring: cut off before the page's qualifier, or starting mid-statement.**
The match is a bare `quote in norm(snapshot)` (`:160`). There is no sentence or word boundary, and `norm` collapses newlines (`:77`), so a quote may also span several lines of code. A census of every whole-word 5–25-token window in the pinned snapshots that passes each fact's key-term gate found:

| Fact | Passing windows | Windows that omit the page's qualifier |
|---|---|---|
| F2 | 231 | 195 omit "by the agent, by scripts, or by you" |
| F3 | 153 | 75 omit "(or with a previous version)" |
| F8 | 294 | shortest is `>= trigger_threshold else: did_pass =` |

Across all eight facts, the census found between 105 and 294 passing windows per fact. The shortest F8 window does not even name what is compared.

- **Lane-history evidence.** `python3 -B verifiers/check_skill_evals.py --rev 8edeb49` gives `skill eval facts backed 8 of 8`, exit=0. At that commit the F2 fact read "Three more JSON files are produced by the run, **not written by the author**". The page (S209 snapshot line 86) continues "— by the agent, by scripts, or by you." The quote stops before that qualifier and passed. The L1 fixed the wording by hand in `ac3c0f1` (`git diff 8edeb49 ac3c0f1 -- corpus/knowledge/skill-eval-artefacts-round70.md`). The counter never saw the defect.
- World `f8_opposite_branch`: F8 row = `| F8 | The reference implementation passes a should-trigger query only strictly below the threshold. | S211 | ">= trigger_threshold else: did_pass = trigger_rate < trigger_threshold" |`
  → `8 of 8`, exit=0. The only complete comparison in the quote is the `<` (should-not-trigger) branch, from S211 snapshot lines 232–234.
- World `quote_drops_qualifier_span`: the F8 quote is widened across both branches (`"did_pass = trigger_rate >= trigger_threshold else: did_pass = trigger_rate < trigger_threshold"`)
  → `8 of 8`. This shows that multi-line spans are accepted.

### Medium

**3. The `SKILL.md` conjunct is met by any occurrence of the path string.**
The test is `skill_ok = ENTRY in skill` (`:135`), a raw substring check. The plan's "cites the entry path" is not checked: a negation, a longer path, a comment or a code fence all pass.

- World `skill_negated`: the `SKILL.md` line 241 becomes "- Never cite `corpus/knowledge/skill-eval-artefacts-round70.md.retired`: its eight facts were withdrawn." → `8 of 8`, exit=0.
- World `skill_in_code_fence`: the line becomes a fenced block holding `stale path, not a citation: xcorpus/knowledge/skill-eval-artefacts-round70.mdx` → `8 of 8`, exit=0.
- World `table_in_html_comment` (also covers finding 4): the line becomes `<!-- corpus/knowledge/skill-eval-artefacts-round70.md -->` → `8 of 8`.

**4. Fact rows and `source:` lines count anywhere in the file, even inside HTML comments or code fences, and even when negated.**
`fact_rows` accepts any line that starts with a pipe (`:100-122`). `src_line` joins every line that starts with `source:` (`:131`). Neither checks Markdown context or position in the header.

- World `table_in_html_comment`: the whole Facts table is wrapped in `<!-- retired, do not read: … -->`, so it does not render. → `8 of 8`, exit=0.
- World `source_line_negated`: all three header `source:` lines are deleted, and a fenced block at the end of the file adds `source: refused — none of S209 S210 S211 back this entry` → `8 of 8`, exit=0.

**5. The SOURCES row is only shape-checked: its URL, kind and tier are not bound to the snapshot, `used-by` is a substring test, and a later duplicate row silently replaces an earlier one.**
`source_rows` keys rows by id, so the last row wins (`:107-113`). It also matches rows inside code fences. The check reads only `row[7] == "mined"` and `ENTRY in row[10]` (`:167`). The `SNAPSHOTS` URL (`:46-57`) is never compared with the row's `source` cell.

- World `sources_url_kind_tier`: S209–S211 get source `Unrelated blog — https://example.invalid/not-the-spec`, kind `forum`, tier `D` → `8 of 8`, exit=0.
- World `usedby_negated`: S209–S211 `used-by` becomes `NOT corpus/knowledge/skill-eval-artefacts-round70.md.bak (withdrawn)` → `8 of 8`, exit=0.
- World `sources_dup_last_wins`: the real S209–S211 rows are set to status `refused`, and three skeleton `mined` rows are appended inside a fenced block at the end of `SOURCES.md` → `8 of 8`, exit=0. This also means duplicate registry ids go undetected.

### Exit-code classes

**6. The docstring says "sha256 verified first — a tampered or missing snapshot is exit 2" (`:18-19`); the code only hashes a snapshot when some fact reaches the quote step (`:160`).**

- World E1: the S211 snapshot is tampered (one line appended) and the F8 row is removed.
  → `skill eval facts backed 7 of 8 / F8: 0 table rows`, exit=1. The tamper is never reported.
- World E2: all three snapshots are tampered and the entry is deleted.
  → `0 of 8 / entry … absent`, exit=1.
- Control E3: the S209 snapshot is tampered and the entry is intact.
  → `environment error: snapshot_tampered: S209-evaluating-skills.md`, exit=2. This is correct when a fact reaches the check.

**7. Environment faults exit 1, the same code as a content verdict.**
`Repo.show` turns every `git show` failure into `None` (`:84-87`), which then reads as "absent". `subprocess` failures are not caught (`:85`, `:329`).

- World E4: an entry edit is committed, then its loose blob object is deleted. `cat-file -t` still reports the commit as a `commit`.
  → `0 of 8 / entry … absent`, exit=1.
- World E5: the same, for the `SOURCES.md` blob.
  → `0 of 8`, with all eight findings wrongly saying `S209 is not an 11-cell SOURCES row`, exit=1.
- World E6: `env PATH=/nonexistent python3 -B verifiers/check_skill_evals.py --repo <sb> --rev 16b212a3…`
  → `FileNotFoundError: [Errno 2] No such file or directory: 'git'` traceback, exit=1.

The docstring says "an unreadable environment is exit 2" (`:26`, `:28`).

### Low

**8. The key-term gate is case-sensitive substring matching (`:153`).**
On its own it accepts `0.5` in "10.55", `PASS` in "BYPASS", `produced` in "never reproduced", and `by hand` in "not by hand"; the census script confirmed each of these against the gate. This is not exploitable at the current pins, because the quote must also appear in the sha-pinned snapshot, and none of those forms appears there. It would matter if the snapshots were re-pinned.

**9. For F8, `--fetch` is not independent evidence.**
The S211 live URL is pinned to a commit (`raw.githubusercontent.com/…/dbd4588…/run_eval.py`, `:55-56`), so its bytes can never differ from the snapshot. Today they are identical: the hash is `43e3b8f8…`, the same as the pin. A fetch failure is also never part of the verdict (`:187`), which matches the docstring.

**10. The 5-word floor counts operators as words.**
F8's quote `did_pass = trigger_rate >= trigger_threshold` reaches 5 only by counting `=` and `>=`; the SOURCES row itself calls it "(5 tokens)". This is harmless here, but the floor does not guarantee a statement.

**11. The self-test does not cover any of the paths above.**
`FakeRepo.snapshot` raises when the text is `None` (`:231-235`), so the real sha256 path in `Repo.snapshot` (`:89-97`), the exit mapping in `main()` (`:316-349`) and `live_fetch` are never exercised. None of findings 1–7 has a broken world in the self-test.

## Residual risk and verification gaps

- The current entry's quotes are on-page and the live pages match the pins. Whether each fact sentence faithfully reads its quote is outside what the counter can show (findings 1–2). The non-author spot-check must read F1–F8 against S209 lines 52, 86, 144, 170 and 172, S210 line 92, and S211 lines 230–234.
- I did not re-run the committed C2 control receipts (`controls/C2-base.txt`, `C2-junk-control.txt`, `C2-forged-control.txt`, `C2-honest-sandbox.txt`). I only confirmed they are tracked at the tip (`git ls-tree -r --name-only 16b212a3 .ufo/waves/round-70/`); that is another seat's item.
- I did not run an LSP. The target is a single self-contained script, and every claim above cites a line read with `cat -n`.

## Suggested fixes for the next counter (not applied; the counter is frozen)

- Require each quote to begin and end on a sentence boundary of the page, or require the fact cell to share its key terms.
- Parse rows only outside fences and comments, and only under `## Facts`; reject duplicate SOURCES ids.
- Compare the row's URL with the `SNAPSHOTS` URL, and match `used-by` against the exact path token.
- Require `SKILL.md` to cite the path as a whole token on a non-comment line.
- Hash all three snapshots before parsing anything, and map git or `OSError` failures to exit 2.
- Add self-test worlds for each of the above.

## Tooling

No installs or updates.

## Scratch

`/tmp/k70w1-RevC2Counter.nY8A` (the sandbox clone and three driver scripts) was deleted before return. No committed lane file, jj state or Git index was touched; the only lane write is this report.
