Result: HOLDS — the three `corpus/README.md` index rows added at `c63ccc68` are field-accurate on every checked cell, `unindexed` goes 1→0 (DRIFT→PASS), and no new DRIFT name appears at `c63ccc68` (the data commit's DRIFT set is a strict subset of the base's); one MEDIUM defect found in the round's new lesson text (a sandbox-labelled hash that trips the corpus citation grammar, adding +1 `commit_unresolvable`), plus one LOW imprecision in the round-59-lessons row.

Seat: KotobaR59.ReviewIndexCorpus · 2026-10-23 · run timestamp `Fri 23 Oct 2026 10:01:21 AM UTC` (`date -u`).

# Method

- Sandbox clone (bounds-mandated shape): `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/ReviewIndexCorpus`, then `git worktree add wt-base a975cbbf00534443c49bf02e29c813a3db0bf0f8` and `git worktree add wt-data c63ccc6823e1f6a8577acbb43d19551eadbbee9a` (both inside the clone; both `git status --short` clean). No sandbox commits were made, so no sandbox hashes are cited. No writes anywhere in the lane except this report file.
- Runs: `python3 -B verifiers/verify_corpus_integrity.py --json` in `wt-base` → `EXIT=1`; in `wt-data` → `EXIT=1`. JSON saved at `/fast/scratch/hyaku/kotoba-r59/ReviewIndexCorpus/{base,data}.json`.
- Tooling directive: no tools installed or upgraded (none needed; python3 present).
- LSP: no `lsp` device exists in this seat's tool inventory (read/bash/edit/eval/glob/grep/task/wait/web_search/write), so no server was available; all semantic checks below are direct file reads, regex extracts of the verifier's own machine-readable JSON, and `git cat-file` probes — text grep was used only as the literal fallback and is never presented as semantic proof.

# DRIFT names (check ids with verdict DRIFT)

At base `a975cbbf` (5):

| check | observed | expected | verdict |
|---|---|---|---|
| corpus.index.tracked_files | 94 | 81 | DRIFT |
| corpus.index.unindexed | 1 | 0 / empty | DRIFT |
| corpus.pointers.report_total | 64 | 51 | DRIFT |
| corpus.pointers.commit_total | 33 | 32 | DRIFT |
| corpus.pointers.commit_unresolvable | 1 | 0 / empty | DRIFT |

At data `c63ccc68` (4):

| check | observed | expected | verdict |
|---|---|---|---|
| corpus.index.tracked_files | 96 | 81 | DRIFT |
| corpus.pointers.report_total | 64 | 51 | DRIFT |
| corpus.pointers.commit_total | 34 | 32 | DRIFT |
| corpus.pointers.commit_unresolvable | 2 | 0 / empty | DRIFT |

PASS at both revs: stale_patterns, missing_paths, report_dead, commit_nonhash (all 0/empty).

- **unindexed 1 → 0: CONFIRMED.** Base `unindexed_detail = ['corpus/lessons/round-58-verifier-spotcheck.md']`; data `unindexed_detail = []` and `corpus.index.unindexed` PASS. The one unindexed file at base is exactly the file the new index row (README:98) covers.
- **No new DRIFT name: CONFIRMED.** Data's DRIFT set {tracked_files, report_total, commit_total, commit_unresolvable} ⊂ base's set. `corpus.index.unindexed` left the set; nothing entered.
- **Growth attribution (all explained by the round's new tracked files):**
  - tracked_files 94→96: the round adds exactly two corpus files (`git diff --name-status a975cbbf c63ccc68`: `A corpus/knowledge/hook-files-round59.md`, `A corpus/lessons/round-59.md`).
  - commit_total 33→34 and commit_unresolvable 1→2: both from the single new citation token at `corpus/lessons/round-59.md:45` (see F1). Verified one occurrence: `grep -c 'sandbox commit `+backtick hash` = 1`.
  - report_total 64→64: unchanged; the new/modified corpus files added no `.ufo/reports/` pointers; report_dead stays 0.
- **Baseline staleness is pre-existing, not introduced:** `verifiers/corpus-baseline.json` (expects tracked_files=81, report_total=51, commit_total=32) is untouched between the two revs (absent from the name-status diff), so the three `equal`-check DRIFTs were already red at base (94/64/33 observed there). The base was red on 5 checks, not only `unindexed 1`; the README row's wording ("turned `verify_corpus_integrity.py` red at that base: `unindexed 1`") is accurate for the `unindexed` conjunct it names.

# Findings

## F1 · MEDIUM — new lesson cites a sandbox hash in citation grammar; `commit_unresolvable` 1→2 (zero-check drift, permanent until reworded)

`corpus/lessons/round-59.md:45` (mistake M81) ends: "(`MutC1Content.md:146-161`; sandbox commit `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` at `/fast/scratch/hyaku/kotoba-r58/MutC1Content`). This is the earlier seat's recorded run, not a run by me."

- The verifier's grammar `COMMIT_RE = (?<![A-Za-z0-9_-])commit[ \t]+` + backtick token (`verifiers/verify_corpus_integrity.py:149`) matches the words "sandbox commit `b8e7d8aa…`"; the token is 40-hex so it is counted (`commit_total` 33→34) and `git cat-file -e b8e7d8aa…^{commit}` fails → `commit_unresolvable` 1→2 (a `zero` check: DRIFT at any baseline, exit 1).
- Unresolvable everywhere it could live: exit 128 in the `c63ccc68` sandbox worktree, exit 128 in the live lane repo, exit 128 in the fleet repo `/home/vgpnk/Projects/shokunin` (the hash is a round-58 scratch-clone commit of seat MutC1Content; its own report labels it `sandbox b8e7d8aa… (/fast/scratch/hyaku/kotoba-r58/MutC1Content)` at `.ufo/waves/round-58/falsify/MutC1Content.md:148`).
- Precedent says this grammar is a corpus defect, not an accepted shape: round-54's identical finding (``commit `451a02ff` `` unresolvable) was fixed in `cae8f2ea` by rewording to `google-gemini/gemini-cli@451a02ff` (`corpus/lessons/round-54-verifier-spotcheck.md:145-149`). Prior lessons avoid the grammar while still labelling: round-56 says "sandbox commits under `/fast/scratch/…`" (no backticked token after the word `commit`, `corpus/lessons/round-56-verifier-spotcheck.md:31`), round-57 lists the hashes as bare backticked tokens with the word `sandbox` after (`corpus/lessons/round-57.md:83`). The round-59 label itself follows the round-57 fix convention (label + clone path); the collision is purely with the citation regex.
- **Exact correction:** in `corpus/lessons/round-59.md:45` reword the citation to drop the word `commit` before the backticked hash — e.g. "(`MutC1Content.md:146-161`; sandbox `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` at `/fast/scratch/hyaku/kotoba-r58/MutC1Content`)" — or fully double-quote the span. Expected effect at `c63ccc68`: `commit_total` 34→33, `commit_unresolvable` 2→1 (the remaining 1 being the pre-existing round-54 self-quote at `corpus/lessons/round-54-verifier-spotcheck.md:147`). No other corpus file gained a matching token (checked: `grep -rln 'sandbox commit' corpus/` → round-56, round-57, round-59 only; the first two do not match `COMMIT_RE`).
- Scoping note: this growth *is* caused by the round's new tracked file, so the attacked claim "no new DRIFT … not explained by the round's new tracked files" survives literally; the defect is in the lesson text the index row points at, and it is the only regression-shaped change the verifier sees anywhere in this round.

## F2 · LOW — README:100 Gate summary omits S102

Row "Round-59 lessons" (`corpus/README.md:100`) says "`## Gate` S096–S101 with access records and the rejections". The Gate section (`corpus/lessons/round-59.md:6-33`) admits S096–S101 **and S102** (the routed-R4 anchor-correction row for S089). Every element the row names exists (S096–S101 with URL/UTC/HTTP/sha/seat records, plus the `### Rejected` list), so this is imprecision, not falsehood — and the C1 claim elsewhere names S102 explicitly. Optional correction: "S096–S102".

# Field-cell rulings, row by row (README added lines 98, 99, 100)

**Row 98 — "Round-58 non-author spot-check (closure)" → `lessons/round-58-verifier-spotcheck.md`: HOLDS.**
- File exists and was tracked and unindexed at base (that is precisely the base `unindexed_detail` entry) — the row's "landed at `a975cbbf` without an index row … `unindexed 1`" is confirmed by direct measurement at `a975cbbf`, and "indexed round 59" by the unindexed→0 flip.
- "round 58 admitted, C1 verified (`6 of 6; new ground 4`)" = `corpus/lessons/round-58-verifier-spotcheck.md:277` ("C1 is verified … `6 of 6; new ground 4`, exit 0") and :43, :79.
- "routed defects R1–R6 (round 59 works R1–R5 in `lessons/round-59.md`)" = spotcheck route list R1–R6 (:165-172, :243-267; R6 "carried") vs round-59 `## Mistakes` M79–M83 mapping captured-by R1, R2, R3, R5, R4 (`corpus/lessons/round-59.md:38-49`). Consistent.

**Row 99 — "Hook files by client (round 59)" → `knowledge/hook-files-round59.md`: HOLDS.**
- The six paths in the row's Basis cell appear in the entry's table in S096–S101 order: `.claude/settings.json` (S096), `~/.codex/hooks.json` (S097), `.github/hooks/*.json` (S098), `~/.copilot/hooks/*.json` (S099), `.gemini/settings.json` (S100), `.cursor/hooks.json` (S101) (`corpus/knowledge/hook-files-round59.md:23-28`).
- "opencode not eligible (its hook code lives only in plugin folders)" = entry § "opencode — no hook file" (:54-57); SOURCES rows S096–S102 all exist (`corpus/SOURCES.md:108-114`).
- "`SKILL.md` § Hook files by client" exists (`SKILL.md:121`); "`../verifiers/check_hook_files.py --rev <rev> --fetch`" exists and is executable; bonus cross-check: `sha256sum verifiers/check_hook_files.py` at `c63ccc68` = `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`, byte-identical to the frozen counter hash in the claim.

**Row 100 — "Round-59 lessons" → `lessons/round-59.md`: HOLDS except F2.**
- "`## Gate` … with access records and the rejections": `## Gate` at :6 with per-row URL/UTC-timestamp/HTTP/bytes/sha256/seat records and a `### Rejected` section (nine rejections); `## Mistakes` at :36 starting at M79 ("M79–M83 are the round-58 spot-check routes…; M84 is this round's own") — "M79 onward" accurate.
- "the round-58 routed defects R1–R5": M79–M83 captured-by fields name R1, R2, R3, R5, R4. Accurate.
- F2: Gate also holds S102; row's enumeration stops at S101.

**Appendix note (README:177-178): HOLDS.** Both referenced artifacts exist (`knowledge/hook-files-round59.md`; `../SKILL.md` § Hook files by client at `SKILL.md:121`; `../verifiers/check_hook_files.py`), and the note's hedge ("checks the cited event identifiers … not observed execution"; "opencode hooks are code in plugin folders") matches the entry.

# Residual risk and verification gaps

- The three `equal`-check DRIFTs (tracked_files/report_total/commit_total vs the stale `verifiers/corpus-baseline.json`) pre-date this round and were not repaired by it; every future corpus change keeps the verifier exit 1 until the baseline is regenerated. Out of scope for this item; flagged so nobody reads exit 1 as this round's regression.
- `commit_unresolvable` at `c63ccc68` = 2 (one pre-existing self-quote in the round-54 lesson, one new from F1). I did not verify the round-54 hash's history beyond the lesson's own account.
- I did not run `check_hook_files.py` or audit SOURCES row bodies / SKILL section content — those belong to the C1 counter and sources seats; my hash cross-check of the counter is byte-identity only.
- `CORPUS.md:112-118` (cited by M83's fix) resolves only at the fleet root `/home/vgpnk/Projects/shokunin/CORPUS.md` (lane has none; existence checked, contents not audited — prose pointer, unchecked by the verifier).
- Verdict is a recommendation to the L1 (agent://KotobaR59); I edited nothing in the lane.
