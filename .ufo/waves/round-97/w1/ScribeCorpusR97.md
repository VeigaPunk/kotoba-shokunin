# ScribeCorpusR97 — SOURCES rows S273/S274 and the round-97 lesson scaffold

Round 97, wave r97-w1, seat ScribeCorpusR97 (scribe). Scratch clone
`/fast/scratch/hyaku/kotoba-r97/ScribeCorpusR97/repo` at the freeze commit
`148395bf42af97436b1b832a97a175515f981939` (`git rev-parse --show-toplevel` asserted equal to the
clone root before any write). The lane repo was never written by this seat; no git/jj write outside
the scratch clone; no subagent dispatch (leaf member).

## Behaviour

1. Read the plan, the pre-data receipts, the SOURCES contract (`CORPUS.md` § SOURCES.md), the last
   registry rows, the round-96 lesson and its verifier spot-check, and `considerthese/2026-10-26.md`.
2. Re-opened the S273 source independently of the L1 receipt and verified every cell it grounds.
3. Polled for `w1/ScoutSourcesR97.md`; it landed at 01:08-03:00 with S273 confirmed byte-identical
   and **S274 admitted** (GoogleTest § Shuffling the Tests), plus two rejects (pytest `tmp_path`,
   pathlib `is_dir`). Re-opened the admitted and rejected pages myself.
4. Appended S273 and S274 to `corpus/SOURCES.md` (inside `## Registry`, after S272), wrote
   `corpus/lessons/round-97.md` as the scaffold, and added one index row to `corpus/README.md`.
5. Ran the census validator before and after; generated the patch from the clone; proved it applies
   on a second fresh clone at the freeze commit and removed that clone.

## Evidence (commands and observed lines)

- S273 fetch: `curl -sS -L -o bazel-test.html -w 'HTTP %{http_code} bytes %{size_download}'
  https://bazel.build/reference/test-encyclopedia` → `HTTP 200 bytes 223640`;
  `sha256sum` → `6b07e08f0f4bae537544eac1afc64d98f0b19a9ae7408b8e6482f56e134d5346`
  (equal to `.ufo/waves/round-97/receipts/sources-opened.txt`).
  Heading `id="test-interaction-filesystem"` at HTML line 656; quote at HTML lines 659-661;
  `printf '%s\n' "<quote>" | wc -w` → `21`. Second locators verified at HTML lines 559, 574, 622-623.
- S274 fetch: `curl … https://google.github.io/googletest/advanced.html` → `HTTP 200 bytes 214623`;
  sha256 `7317f5e7d59afb22c2bd9550122f55b38c60d28865d7522664972769b2fd16c5` (equal to the scout's).
  Heading `id="shuffling-the-tests"` at HTML line 2110; quote at HTML lines 2112-2113; `wc -w` →
  `25`; `grep -c 'gtest_shuffle'` → `1`; seed sentence at HTML lines 2117-2119; `wc -w` → `18`;
  footer at HTML lines 2601-2606 carries no version marker.
- Reject (pytest): `curl … https://docs.pytest.org/en/stable/how-to/tmp_path.html` → `HTTP 200 bytes
  40121`; sha256 `dbc7d4b7e96ff939428f8bd3b0ce09e20fee4be5912427833fb9170d675c8df2`; heading at HTML
  line 313; quote at HTML lines 314-315; `wc -w` → `8`.
- Lead (pathlib): `curl … https://docs.python.org/3/library/pathlib.html` → `HTTP 200 bytes 271233`;
  sha256 `b55e4f2852c8fc1a2ef215fb1383fd184a73dc0003a211e9b0c94008fcc2dc14`; `is_dir` entry at HTML
  line 1365; quote at HTML lines 1367-1369.
- Registry duplicate check before the appends: `grep -c 'bazel.build'` → `0`, `grep -c
  'google.github.io'` → `0`, `grep -cF 'docs.pytest.org/en/stable/how-to/tmp_path.html'` → `0`,
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|[^|]*https://docs\.python\.org'` → `6`.
- Round-96 routed defect 1: `.ufo/waves/round-96/receipts/sources-opened.txt` line 12 reads
  `lines 790-791 (located quote, 19 words): "The parameter name or symbol can be enclosed in braces,
  which are optional except for positional parameters with more than one digit"`; the same string
  measures `22` (`printf '%s\n' "<quote>" | wc -w` → `22`).
- Census before: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file
  "$D/corpus/SOURCES.md"` → **rc 0**, 34 `W04`, 0 `E` codes, 198 rows.
- Census after: same command → **rc 0**, **34 `W04`** (no new one; the warning list names neither
  S273 nor S274), 0 `E` codes, **200 rows**.
- Patch: `git -C "$D" add -A -- corpus/SOURCES.md corpus/lessons/round-97.md corpus/README.md`;
  `git -C "$D" diff --cached --binary 148395bf… > …/ScribeCorpusR97.patch` → 26266 B, sha256
  `3f2712c471c814b31300af5caf7df59a8de8aac8f24cb3a77c184e94681b4902`, 3 file diffs.
- Patch proof on a second fresh clone at the freeze commit: `git apply --check` → rc 0; `git apply`
  then `diff -q` on each of the three files → identical; verify clone removed.
- `SKILL.md` measurements for § Considerthese at the freeze commit: 600 lines, 92672 B, 165 lines
  >120 chars, 94 >300, longest 1491 chars at line 518; `## Gate registry` at line 443 to EOF =
  43723 B (47.2 %); description 1021 chars, first sentence 151 chars.

## Gates

- Census `validate` rc 0, no new `W04`, no `E` code — PASS.
- Patch applies on a fresh clone at the freeze base and reproduces the authoring files byte for byte
  — PASS.
- Owned-file scope: only `corpus/SOURCES.md`, `corpus/lessons/round-97.md`, `corpus/README.md`
  changed (`git status --porcelain` in the clone shows exactly those three) — PASS.

## Touched surfaces

- `corpus/SOURCES.md` — two appended rows (S273, S274) inside `## Registry`; no existing row edited.
- `corpus/lessons/round-97.md` — new scaffold: `## Gate`, `## Corrections`, `## Mistakes`,
  `## Status changes`, `## Considerthese`, `## Settlement`.
- `corpus/README.md` — one index row (`Round-97 lesson`).
- Receipts under `.ufo/waves/round-97/w1/ScribeCorpusR97/`: `ScribeCorpusR97.patch`,
  `census-before.txt`, `census-after.txt`, `source-digests.txt`, `patch-check.txt`.

## Out of scope / not done

- No `corpus/knowledge/` entry was admitted (the round's claims are instrument claims, not knowledge
  entries).
- No `## Paths` or `## Search log` edit: this seat's ownership is append-rows-only, and the search
  log note for the round's bounded search is the scout's report, not a registry row.
- No settlement content: `## Settlement` is the L1 placeholder by design.
- No tool installs, no package transactions, no network beyond the four documented fetches.

## Findings

- **F1 — S273 re-open is clean.** My own fetch is byte-identical to the L1 receipt (223640 B, same
  sha256), so the plan's HTML line numbers hold and C2's sourcing needs no correction.
- **F2 — S274 is admitted and grounds v5 rule 6.** The counter's header rule 6 (lines 31-33) and its
  seed handling (lines 341-345) match the page's mechanism: shuffle, print the seed, replay it
  (`KOTOBA_R97_SEED`). The row is the only cited authority for that rule; the page is unversioned, so
  the anchor pins the fetch date and digest.
- **F3 — the scout's seed-sentence locator was one line short.** The scout wrote HTML lines 2117-2118
  for the 18-word seed sentence; in my bytes the sentence ends at line 2119 (`later.`). The lesson
  and the row record 2117-2119. This is a locator precision note, not a disagreement about the quote.
- **F4 — the scout's pathlib line for the legacy baseline is off by one.** The scout wrote
  `legacy.is_file()` at line 246; the file has it at line 247 (`base.is_file()` is line 234). The
  lesson records 234 and 247. No row depends on it (pathlib is a lead, not a row).
- **F5 — census counts.** 198 → 200 rows; the 34 `W04` warnings are the pre-existing duplicate-URL
  set and neither new row appears in it.
- **F6 — the round-96 receipt defect is confirmed and corrected append-only.** C97-1 in the lesson
  points at the frozen receipt and states the measured 22 words; the receipt is not edited.

## Risks

- The S274 quote is exactly at the 25-word ceiling; any shaping change that adds a word would break
  the ≤25 rule, so the row's anchor records the shaping explicitly.
- The GoogleTest page has no version marker; `recheck: on-release` is the only cadence that can
  detect a reword, and the digest is the fallback locator.
- The lesson's `## Mistakes` row cites scratch-only round-96 worlds (patches under
  `.ufo/waves/round-96/w1/ExecCounterForgeryR96/`), which are wave artifacts, not registry rows; the
  fix is cited to the committed v5 counter and the `c2-v5-as-v4.txt` receipt.
