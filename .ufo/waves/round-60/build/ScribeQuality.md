Result: DONE — four exact append-only QUALITY row drafts are complete; the checker source is not yet integrated in the lane.

# ScribeQuality — Round 60

## Exact rows for `corpus/QUALITY.md`

The current tail ends at Q51 (`corpus/QUALITY.md:59-66`); these drafts take Q52–Q55 and leave `supersedes` as `—` because they add criteria rather than replace an existing row.

| Q52 | After any L1 census-token substitution, a seat scores the substituted token against every token clause before the freeze; the original token's score cannot be carried over or replaced by a post-freeze re-score. | frozen census tokens and token eligibility | M84 `census-token-substituted-without-rescore` (`corpus/lessons/round-59.md` § Mistakes); the round-59 spot-check found `.github/hooks/*.json` substituted after the census seat scored `.github/hooks/audit.json`, and `SrcVSCode` scored the replacement only after the freeze (`corpus/lessons/round-59-verifier-spotcheck.md:85-93`). | — |
| Q53 | A quote-shaping note is written from fetched bytes, not a seat's description: paste the output of `sed -n '<L>p'` for the source line in the report and state exactly which bytes were dropped, joined, or otherwise shaped. | quote-shaping notes in knowledge entries and lesson Gates | M85 `quote-note-overclaimed-third-time` (`corpus/lessons/round-59.md` § Mistakes); `ReviewEntry` F1–F2 found the S097/S098 shaping notes did not match the fetched lines (`.ufo/waves/round-59/falsify/ReviewEntry.md`). | — |
| Q54 | A lesson line stating an explicit `<N> words` or `<N>-word` count carries its `wc -w` command on that line or one of the next two lines; a number without that command is not evidence of its own count. | lesson word-count statements | M86 `word-count-without-command` (`corpus/lessons/round-60.md` § Mistakes); the tested checker-copy output is recorded in `.ufo/waves/round-60/build/ScribeMistakes.md:49-55` (sandbox copy; not an integrated verifier). | — |
| Q55 | Every timestamp in a plan or report is at or before the commit that ships that file; a later timestamp is a conformance defect and is corrected or replaced by a commit reference. | plan/report chronology | M87 `future-dated-timestamp` (`corpus/lessons/round-60.md` § Mistakes); round-59 R3 and the round-60 A1 recurrence are recorded in `.ufo/waves/round-60/build/ScribeMistakes.md:15` and `corpus/lessons/round-59-verifier-spotcheck.md:36-37,203-204`. | — |

## Findings and evidence

- **M84 / M85:** `corpus/lessons/round-59.md:51-70` records both mistakes; the round-59 spot-check gives the clause-by-clause census finding at `:85-93`. For M85, `ReviewEntry.md` F1–F2 is cited by the lesson; I did not reopen sources or rerun that comparison.
- **R1 / M86:** `corpus/lessons/round-60.md:49-55` now records M86 and the failed check. `ScribeMistakes.md:49-55` says the command `python3 -B verifiers/check_word_counts.py --rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af --file corpus/lessons/round-59.md` returned checker exit 1 with `corpus/lessons/round-59.md:27: stated word count (29 words, 25-word, 10-word) with no wc -w command on this line or the next 2` and `stated word counts without a counting command: 1 of 1 claimed lines`. That run was in `/fast/scratch/hyaku/kotoba-r60/ScribeMistakes/sandbox` against the named revision; the report identifies the checker copy as read from the executor's working tree, not integrated or final. A direct read of lane `verifiers/check_word_counts.py` returned not found, and the build listing has no `ExecWordCountCheck.md` yet. I therefore cite the M86 lesson and tested sandbox report, not an integrated verifier.
- **R3 / M87:** the round-60 lesson records M87 at `corpus/lessons/round-60.md:57`; its evidence says `git show bfe8cc2b:plans/round-60.md | grep -n 10:36Z` printed the A1 header at exit 0 and `git log -1 --format=%cI bfe8cc2b` returned `2026-10-23T07:33:42-03:00` at exit 0; UTC conversion returned `2026-10-23T10:33:42Z`. At freeze the header used the commit reference instead. The 10:12Z report-close defect is recorded at `corpus/lessons/round-59-verifier-spotcheck.md:36-37`.

**Verbatim conflict:** the task supplied `10:33:44Z` for `bfe8cc2b`; the executed `%cI` command returned `2026-10-23T07:33:42-03:00`, and the executed UTC conversion returned `2026-10-23T10:33:42Z`. Both precede the header's `10:36Z`; I have not replaced either timestamp with the other.

## Gates, surfaces, limits

- No source fetch, build, verifier, test suite, or counter was run by this seat. No tool was installed or upgraded.
- This seat wrote only `.ufo/waves/round-60/build/ScribeQuality.md`; `corpus/QUALITY.md` is unchanged. The four rows are deliverable text for L1 integration.
- R1 evidence is a checker run in a sandbox copy; `verifiers/check_word_counts.py` is not present at the lane path at this read. If the executor's final artifact lands, L1 can add its exact committed-file evidence to Q54.

## Provenance

Assignment base: `31092dc6f875370bddd6eb1e4da4ca0d210c56af`; freeze: `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`. Read surfaces: `corpus/QUALITY.md`, `corpus/lessons/round-59.md`, `corpus/lessons/round-59-verifier-spotcheck.md`, `corpus/lessons/round-60.md`, `.ufo/waves/round-60/build/ScribeMistakes.md`, and `.ufo/waves/round-60/w0/ExecR1Recount.md`.

Report: `.ufo/waves/round-60/build/ScribeQuality.md`
