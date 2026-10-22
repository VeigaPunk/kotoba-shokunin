Result: DONE — the in-place S050 edit of `e792607e` is reproduced and traced to its cause, the served Zed page was re-opened this round and still carries the recorded 3,169 bytes with no revision marker of its own, so the verified anchor is the docs source tree written `repo@40-hex` (the parenthetical "frontmatter only differs" is false), and a paste-ready append-only correction (row S061, Gate row, lesson paragraph) is drafted and run against the corpus gates in a sandbox clone, where it changes no gate verdict and adds no commit citation.

# Closure routed defect 3 — S050 in-place `anchor` edit (round 54, seat ScribeS050Fix)

Scope: draft the correction only. No lane file was written except this report; no lane git or jj write ran; the in-place edit is not proposed for revert. Every executed probe ran in `/fast/scratch/hyaku/kotoba-r54/ScribeS050Fix/` (lane clone at tip `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`, plus a second pristine clone `pristine/` for the mutation falsifier).

## 1. What commit `e792607e` changed in `corpus/SOURCES.md`

Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e792607e -- corpus/SOURCES.md` (and the same with `-U0 --format=`) → exit 0, diffstat `3 ++-`, `2 insertions(+), 1 deletion(-)`.

| line at `e792607e^` | line at `e792607e` |
|---|---|
| `… body identical to `docs/src/ai/instructions.md` at commit `cfb894a5` (frontmatter only differs) …` | `… body identical to `docs/src/ai/instructions.md` at zed-industries/zed@`cfb894a5` (frontmatter only differs) …` |

Two changes in one commit's file: that single cell rewording inside the S050 row (line 63 in both revisions — an in-place edit of a cell the contract keeps append-only), and one appended row (S052, Cursor help page). Nothing else in the S050 row moved; `diff` of the two folded lines differs only in that span.

The breach is real under the frozen contract: fleet `CORPUS.md` § "SOURCES.md — where a shokunin learns" → Rules 2, "Append-only. Only `status`, `recheck` and `used-by` change in place … A correction is a new row whose `teaches` opens `supersedes S0NN —`." The round-53 lesson disclosed it as a wording fix (`corpus/lessons/round-53.md:44`) rather than as a correction row.

## 2. Re-open receipts (ordinary `curl`, no browser, no challenge bypass, no model call)

| # | URL | UTC access | HTTP | bytes | sha256 | content-type |
|---|---|---|---|---|---|---|
| 1 | https://zed.dev/docs/ai/instructions.md | 2026-10-22T21:16:10Z | 200 | 3,169 | `7c63efe035bf063809fb9815d4ed4ce6bdde6adb718e56ecd245e025f8244ab9` | not recorded on this fetch |
| 2 | same page, second fetch | 2026-10-22T21:20:47Z | 200 | 3,169 | `7c63efe035bf063809fb9815d4ed4ce6bdde6adb718e56ecd245e025f8244ab9` | `text/markdown; charset=utf-8` |
| 3 | https://raw.githubusercontent.com/zed-industries/zed/cfb894a5dde8ccf3fba1659164f47fdd1c024e2e/docs/src/ai/instructions.md | 2026-10-22T21:16:44Z | 200 | 3,256 | `1bc6e31274cb4f7ff637f74c2fab1d0051ff258b5f310db485580336f91d7f4a` | not recorded on this fetch |
| 4 | https://raw.githubusercontent.com/zed-industries/zed/cfb894a5/docs/src/ai/instructions.md (8-character form) | 2026-10-22T21:17:27Z | 200 | 3,256 | `1bc6e31274cb4f7ff637f74c2fab1d0051ff258b5f310db485580336f91d7f4a` | not recorded |
| 5 | fetch 3 repeated | 2026-10-22T21:20:47Z | 200 | 3,256 | `1bc6e31274cb4f7ff637f74c2fab1d0051ff258b5f310db485580336f91d7f4a` | `text/plain; charset=utf-8` |

`cmp` receipts: fetch 1 vs 2 → identical (`PAGE_STABLE`); fetch 3 vs 5 → identical (`SRC_STABLE`); fetch 3 vs 4 → identical (`SHORT_EQ_FULL`).

Body comparison (commands run in the fetch directory):
- `tail -n +2 zed-instructions.md > served-body.txt` (drops the served line-1 `llms.txt` navigation line, 91 bytes) and `tail -n +5 zed-src-cfb894a5.md > src-body.txt` (drops the 4-line, 178-byte frontmatter):
  `wc -lc served-body.txt src-body.txt` → `62 3078` for both; `sha256sum` → `2ec79b6c0dce27397b32672bbe92f3a808e3f62b69ad651be809e03329b48db9` for both; `cmp` → no output, `IDENTICAL`.
- Byte arithmetic holds: 3,169 − 91 = 3,078 and 3,256 − 178 = 3,078.
- The served page contains no revision marker: `grep -niE 'revision|commit|updated|sha256|version' zed-instructions.md` → no output, exit 1.
- Headings of the four cited ranges exist at the recorded lines: `grep -n '^## '` → `11`, `23`, `39`, `50`, `57` (so `:11-21`, `:23-37`, `:39-48`, `:57-63` are the sections the row names).
- Quote line: `sed -n '25p'` → `Project instruction files apply to the current project. Zed uses the first matching file in this list:`; `wc -w` → 17; `grep -cF` of the full sentence → 1 (verbatim).

## 3. Which anchor is right

Candidates: the pre-edit string `at commit `cfb894a5`` and the committed string `at zed-industries/zed@`cfb894a5``.

- Both name the same revision: the 8-character and 40-character forms resolve to identical 3,256-byte bytes (`SHORT_EQ_FULL`), and `cfb894a5` is the full `cfb894a5dde8ccf3fba1659164f47fdd1c024e2e`.
- The committed form is right in kind: the served page carries no revision marker of its own, so the revision can only be the docs source tree, and naming the repository (not a bare hash) is what tells a reader it is an upstream Zed revision rather than a lane commit.
- The committed form is not yet right in fact, in two ways:
  1. An 8-character sha is not a whole revision id for a registry whose other upstream pins are written as `repo@` plus 40 hex or as a date (`corpus/lessons/round-53.md` build record already carried the full `cfb894a5dde8ccf3fba1659164f47fdd1c024e2e`, `.ufo/waves/round-53/build/ScribeZed.md:21`).
  2. The parenthetical `(frontmatter only differs)` is false and was already falsified outside the lane: the served page drops the 178-byte frontmatter **and adds** the 91-byte `llms.txt` navigation line (round-53 falsify seat `W2ReopenS050.md` § "Anchor-cell comparison", defect D1; re-measured this round in § 2 above).
- So the verified anchor is `zed-industries/zed@cfb894a5dde8ccf3fba1659164f47fdd1c024e2e` plus the exact difference (navigation line removed, frontmatter added, body byte-identical), which is what S061 carries.

Why the edit was made, and what it actually bought (measured, not inferred): with the pre-edit wording restored in a pristine clone, `python3 -B verifiers/verify_corpus_integrity.py` prints `corpus.pointers … commit_total=33 unresolvable=1 nonhash=0` with site `commit_unresolvable: corpus/SOURCES.md:63: cfb894a5`, 4/9 checks pass, exit 1. At the tip the same gate prints `commit_total=32 unresolvable=0`, 6/9 pass, exit 1. So the edit removed one finding from a gate that was red at the tip anyway (`tracked_files`, `unindexed`, `report_total`); it turned no failure into a pass. That distinction belongs in the lesson text (below) and is why the correction is a row, not a revert.

## 4. Draft delivery

### (a) New `corpus/SOURCES.md` row — paste after S060 (the defect-2 correction row) at integration

~~~markdown
| S061 | Zed — Agent Instructions (served markdown, verified against the docs source tree) — https://zed.dev/docs/ai/instructions.md | docs | A | Which always-on instruction filenames the Zed Agent loads, in what order, and how personal and project files combine | § Personal Instructions (`instructions.md:11-21`), § Project Instructions (`:23-37`), § Instruction File Support (`:39-48`), § Migrating from Rules (`:57-63`); the served page carries no revision marker (a case-insensitive grep for revision, commit, updated, sha256 and version prints nothing), so the revision names the docs source tree that matches it; re-opened 2026-10-22T21:16:10Z (200, 3,169 B, sha256 `7c63efe035bf0638…`), the byte count and digest prefix the round-53 fetch of 2026-10-22T20:05:08Z records; body byte-identical to `docs/src/ai/instructions.md` at zed-industries/zed@`cfb894a5dde8ccf3fba1659164f47fdd1c024e2e` (re-fetched 2026-10-22T21:16:44Z, 200, 3,256 B, sha256 `1bc6e312…`; the 8-character form `cfb894a5` re-fetched 2026-10-22T21:17:27Z returns the same 3,256 B and digest) once the served line 1 `llms.txt` navigation line (91 B) and the source's four frontmatter lines (178 B) are removed — both leave 62 lines, 3,078 B, sha256 `2ec79b6c…`; the served page therefore differs by that navigation line and by the frontmatter, not by frontmatter alone | supersedes S050 — records the in-place anchor edit of `e792607e` as a correction, not a new reading: the re-opened page still says Zed uses the first matching project instruction file in the list | mined | 2026-10-22 | 90d | corpus/lessons/round-54.md |
~~~

Design notes, each tied to a rule:
- `teaches` opens `supersedes S050 —` (contract rule 2) and stays inside the 17-word quote: it does not restate the nine filenames, the "never merges" paraphrase or the `@AGENTS.md` inference — those remain S050's cells, which the round-53 falsify seat verified hold. "still says" is backed by the unchanged bytes, recorded in the same row.
- The revision is written repo-qualified with the full 40-hex sha and in no place takes the shape the corpus gate reads as a commit citation (the lowercase word followed by a backticked token), so the gate does not read it as a lane commit: with this row applied, `commit_total` stays `32` and `unresolvable` stays `0` (measured, § 5).
- `used-by: corpus/lessons/round-54.md` is true only once that lesson exists and carries the Gate row below (a lesson is a permitted citation surface; S038/S039 use `corpus/lessons/round-52.md` the same way). **If the row lands before the lesson file, use `queued` and `—` instead** — a `mined` row whose `used-by` path does not exist is an E11 finding.
- S050 is not edited: `status`, `recheck` and `used-by` need no change, and there is no `superseded` status in the enum.

### (b) `corpus/lessons/round-54.md` § Gate row (round-53 Gate column shape)

~~~markdown
| S061 | https://zed.dev/docs/ai/instructions.md | 2026-10-22T21:16:10Z (source tree re-fetched 21:16:44Z; 8-character form 21:17:27Z) | 3,169 B, `7c63efe0…` (source 3,256 B, `1bc6e312…`) | "Project instruction files apply to the current project. Zed uses the first matching file in this list:" | `instructions.md:25` | ScribeS050Fix; correction row for the in-place S050 anchor edit of `e792607e` |
~~~

The quote is 17 words, verbatim at served line 25 (§ 2), and is the sentence `teaches` is bounded to.

### (c) One-paragraph lesson note (fits the round-53 § Mistakes evidence cell; paste as the paragraph or as that cell)

> **Append-only breach: S050's `anchor` cell.** Commit `e792607e` rewrote S050's anchor cell in place — the round-53 text read "... at commit `cfb894a5` (frontmatter only differs)" and the committed text reads "... at zed-industries/zed@`cfb894a5` (frontmatter only differs)" — while SOURCES contract rule 2 allows an in-place change only to `status`, `recheck` and `used-by`. The round-53 lesson recorded it as a wording fix; no gate compares a registry row's text against the previous revision (the integrity and derivation verifiers compare counts, the corrections sweep compares only the phrases registered in it, and the counters that read SOURCES check cell shape, tier, URL host and citations), so nothing failed. The edit's stated purpose holds: with the pre-edit wording, `verify_corpus_integrity.py` reports `commit_unresolvable=1` at `corpus/SOURCES.md:63`, and the committed row reports `0` — but that gate was already red at the tip on three other findings (`tracked_files`, `unindexed`, `report_total`), so the edit removed one finding, not a failure. The edited cell also kept the parenthetical "frontmatter only differs", which round-53 falsify seat W2ReopenS050 had already broken, and an 8-character sha is not a whole revision id. Round 54 appends correction row S061 (`supersedes S050`) with the verified anchor and leaves the in-place cell as committed.

Both occurrences of the old wording are inside double quotes on their line, which is the corpus gate's documented exclusion for quoted meta-findings; measured effect: `quoted-excluded` 4 → 5 and `commit_total` unchanged (§ 5).

## 5. Verification battery (sandbox clone, same commands the lane's gates use)

Applied the row (after S052) and the lesson fragment to the sandbox clone at tip, `git add -A corpus` inside the clone only, then:

| gate | result with the draft | result at tip `7ad05d34` (unmutated) |
|---|---|---|
| `python3 -B verifiers/verify_corpus_integrity.py` | exit **1**; `tracked=80 unindexed=2 stale=0 missing=0`; `report_dead=0/51 commit_total=32 unresolvable=0 nonhash=0 … quoted-excluded=5`; `6/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total` | exit **1**; `tracked=79 unindexed=1`; `commit_total=32 unresolvable=0 nonhash=0 … quoted-excluded=4`; same DRIFT set (`6/9`) |
| `python3 -B verifiers/verify_corpus_independent.py` | exit **1**; `commits candidates=37 citations=32 hex=32 quoted=5 nonhash=0 unresolvable=0`; the quoted-meta list gains `corpus/lessons/round-54.md:6: cfb894a5` | exit **1**; `commits candidates=36 citations=32 hex=32 quoted=4 nonhash=0 unresolvable=0` (the extra candidate is the quoted lesson citation; citations do not move) |
| `python3 -B verifiers/check_correction_sweep.py --root .` | exit **0**, `correction sweep: 0 stale block(s)` | exit **0**, same line |
| `scripts/sources-census.sh validate <sandbox lane> --today 2026-10-22` | exit **0**, `ok` + the three carried `W04` warnings (S018, S019, S021); no `E04` for S061 because `supersedes S050` suppresses it | exit **0**, `ok` + the same three `W04` warnings |
| frozen malformed-row census (field count on the 11-column table) | `0` | `0` |
| duplicate ids / enum / `mined`-with-missing-`used-by` censuses | `0` / `0` / `0` | `0` / `0` / `0` |

Two honest deltas, both expected and both needing the L1's hand:
- `corpus.index.unindexed` rises 1 → 2 because `corpus/lessons/round-54.md` has no coverage-map row in `corpus/README.md` yet (the pre-existing unindexed file is `corpus/lessons/round-53-verifier-spotcheck.md`; a peer's working-tree edit adding its row is in flight — see § 7). The lesson file needs its own row in `corpus/README.md` § coverage map, which is outside this seat's write scope.
- `corpus.index.tracked_files` rises 79 → 80 for the same new file; the integrity checker's `tracked_files` and `report_total` expectations are already stale at the tip (they want 78 and 49), so no new class of drift appears.

The exit codes are unchanged from tip (1 → 1) on every gate that was already red; the only movement is one more unindexed lesson file, which is the lesson file itself and not the row.

## 6. Q29 does not reach this cell (measured, with the counterexample)

Q29 requires a correction's stale phrase and declared result to be registered in `verifiers/check_correction_sweep.py`. That is impossible for the S050 cell without a second in-place edit: the sweep treats one table row as one block, and S050's row cannot gain the token `S061` without being edited again. Demonstration in the sandbox: a probe registry entry `{"id": "r54-probe-s050-anchor", "file": "corpus/SOURCES.md", "stale": r"\(frontmatter only differs\)", "declared": r"S061"}` → `check_correction_sweep.py --root .` exits **1** with `FAIL r54-probe-s050-anchor corpus/SOURCES.md:63 stale claim without the declared result`. The probe edit was reverted with `git checkout -- verifiers/check_correction_sweep.py` inside the sandbox; the delivered sandbox state runs exit 0 (table above).

Consequence for the L1: the S050 cell cannot satisfy Q29 by construction, so the record of this correction is the `supersedes S050` row plus the lesson paragraph, and the carried false parenthetical should not be counted as a Q29 failure. Whether S050's cell text should be left stale forever is an L0 question (ratify or retire the wording), not something this seat can fix without breaking rule 2 again.

## 7. Integration notes and lane state

- Insert S061 after S060 (defect-2's Gemini correction row) in `corpus/SOURCES.md` § Registry; the id is unused at tip (`grep -oE '^\| S[0-9]{3,}' corpus/SOURCES.md | sort | tail -5` → S048, S049, S050, S051, S052) and S053–S060 are reserved by `plans/round-54.md`'s dispatch rows for the seven C1 clients and defect 2.
- Add `corpus/lessons/round-54.md` to `corpus/README.md` § coverage map in the same commit, or the unindexed count goes to 2.
- Keep S061 as `mined` only if the lesson file exists in that revision; otherwise `queued` + `—` until it does.
- If the always-on knowledge entry's `source:` line is later repointed to S061, add that path to `used-by` (a permitted in-place change, logged old → new).
- Do not revert the in-place edit. S050 stands as committed; the correction row is the contract's mechanism and the reason the loss (`frontmatter only differs` is false) is now recorded rather than silently edited a second time.
- Lane working tree observed read-only at 21:2xZ: `M corpus/README.md` (one added coverage-map row for `lessons/round-53-verifier-spotcheck.md`, a peer's edit) and the untracked `.ufo/waves/round-54/` tree. This seat made no lane write other than this report; the sandbox-clone measurements above are against tip `7ad05d34`, i.e. without that peer row.

## 8. Calibration — what this report does not claim

- It does not claim the site renders from `cfb894a5`; it claims the served body is byte-identical to `docs/src/ai/instructions.md` at that revision, which is what was measured.
- It does not claim the served page is current relative to later Zed revisions; no later revision was fetched (freshness is out of scope this round).
- It does not claim the Zed loader's behaviour. The round-53 code reading at `cfb894a5` was not re-cloned or re-executed here.
- It does not claim the gateway `verify_corpus_integrity.py` is green anywhere; tip and draft both exit 1 on three carried DRIFTs.
- Times are the `date -u` readings bracketing each `curl`; content-type is recorded only for the 21:20:47Z pair (the earlier fetches requested bytes and digest only).
- The quote used is the 17-word `:25` sentence, so `teaches` is bounded to it; the nine-name list and the "never merges" paraphrase remain S050's cells and were not re-adjudicated by this seat.

## 9. Artifacts

- Report (this file): `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-54/build/ScribeS050Fix.md`.
- Fetched bytes and comparisons: `/fast/scratch/hyaku/kotoba-r54/ScribeS050Fix/fetch/` (`zed-instructions.md`, `zed-instructions-c2.md`, `zed-src-cfb894a5.md`, `zed-src-short.md`, `zed-src-c2.md`, `served-body.txt`, `src-body.txt`) — page `7c63efe035bf0638…`, source `1bc6e31274cb4f7…`, bodies `2ec79b6c0dce2739…`.
- Gateway logs (host `/tmp`, not part of the lane): `final_int.txt`, `final_int2.txt`, `final_ind2.txt` (draft), `tip_integ.txt`, `indep_tip.txt` (tip), `mut_integ.txt` (pre-edit mutation), `draft_integ.txt`, `indep.txt`, `sweep.txt`, `sweepst.txt`, `sweep_probe.txt` (Q29 probe).
- Sandbox clones: `/fast/scratch/hyaku/kotoba-r54/ScribeS050Fix/lane` (draft applied, `git add` inside the clone only) and `…/pristine` (mutation falsifier, restored with `git checkout -- corpus/SOURCES.md`).
- Tool installs or upgrades: none (nothing was missing).
