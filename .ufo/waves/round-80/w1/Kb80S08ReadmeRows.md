# Kb80S08ReadmeRows — coverage rows + Frontier note (round 80, w1)

Seat: `Kb80S08ReadmeRows` (scribe, leaf). Date: 2026-10-27.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; lane HEAD at write time `c2f69d4` (freeze commit; base is its parent, `git merge-base --is-ancestor 398cbe1… HEAD` exits 0).
Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80S08ReadmeRows` (four clones at base, removed after receipts were copied).

## Assignment and delivery

Item: the three `corpus/README.md` coverage-map rows for the round-79 closure spot-check, the round-80 lesson and the round-80 `allowed-tools` entry (plan § C1 repair 3's row half), plus the append-only `## Frontier` note recording the C2 ground entering Core and what stays open, existing rows intact.

Delivered as drafts and a patch, not as lane edits (freeze discipline):

- `.ufo/waves/round-80/build/Kb80S08ReadmeRows.md` — the paste source: three rows (verbatim match to the patched README, checked), the Frontier note (verbatim match, checked), per-row evidence and the dependency list.
- `.ufo/waves/round-80/build/Kb80S08ReadmeRows.patch` — README-only unified diff against base: 1 file, 5 insertions, 0 deletions (3 rows + blank + note). `git apply --check` exit 0 on a fresh base clone; applied `corpus/README.md` sha256 `9db6cc91a6942679c45d118896ee4780563da859b43defcac65b6935355d75a1`, identical in the generating clone and in a second fresh clone. Patch sha256 `10117e66ea3c3fb0a15d0a2657565da9b719a1edcd601a771e94a17494613f5c` (23 lines, 7,941 bytes).
- Receipts: `Kb80S08ReadmeRows-index-test.txt`, `Kb80S08ReadmeRows-c2-base-draft.txt`, `Kb80S08ReadmeRows-integrity-base.txt`, `Kb80S08ReadmeRows-integrity-with-rows.txt`.

Placement: rows at the end of `## Coverage map` after the `| Round-79 lessons | …` row (base line 156); note after the Round-74 note (base line 239), before `## Known gaps`.

## Behavior (what the rows and note assert, and on what bytes)

- Row 1 (`lessons/round-79-verifier-spotcheck.md`): read the whole file at base. `rejected-honest-stop`; both claims `unprovable`; §3 has a header plus nine data rows (six admits S226–S231, three rejects — counted `grep -c '^| '` = 10); §4 expansion/quality `unchanged`, discernment `improved`; §5 routes R79-D1–R79-D4; best committed repair world 3 of 6 (its own §2 sentence). Landed without an index row before this one — this row is what closes the base gate's `unindexed 1`.
- Row 2 (`lessons/round-80.md`): written against the actual lesson draft `.ufo/waves/round-80/build/Kb80S01Lesson.md`, not a hoped-for shape — C1 base reading admitted, after-value deferred to the L1; six re-opened rows with quotes/snapshots/`used-by` moves; S232+ rejections and assimilation marked pending; the R79-D2 `census-final.txt` correction as an append-only notice; `## Mistakes` M80-1 (pipeline-read verdict, receipt `.ufo/waves/round-80/receipts/m80-1-pipe-vs-direct.txt`) and M80-2 (range end pattern matching its own start line: 17 B vs 24,897 B by line range). **No after-value is asserted.**
- Row 3 (`knowledge/allowed-tools-surfaces-round80.md`): form-level only, S226–S231. Every quoted page string was located in a committed snapshot: `S226-spec.md:35,176,177,179-183`; `S227-claude.md:404,405,617,420-425,432`; `S228-factory.md:254,282,298,235-238`; `S229-msaf.html:820,825`; `S230-pi.md:78`; `S231-vibe.md:712,725-728,969,972-976,1039-1040`. The four grant labels (`pre-approves`, `metadata-only`, `experimental`, `unstated`) match `Kb80S10Province.patch`, and the `../SKILL.md` § Frontmatter craft reference matches `Kb80S09SkillRule.patch` (rule inserted after the Portability-floor paragraph).
- Frontier note: C2's documented form enters Core in part (three value forms, four grant readings, snapshot-pinned, form-only counter), the grant-semantics rider is exploratory with the round-80 non-author closure as reviewers of record, and the open list keeps measured client behaviour, parser acceptance (Vibe's tension), the restricting-mechanism map, the silent-client question and **`Per-render consumption`** open — the two existing Frontier rows are untouched.

## Gates run (own exit status; no pipelines for verdicts)

| command | observed |
|---|---|
| `git -C clone apply --check Kb80S08ReadmeRows.patch` (fresh base clone) | exit 0; then `apply` exit 0; README sha256 `9db6cc91…` |
| `git -C clone diff --cached --binary --src-prefix=a/ --dst-prefix=b/` | exit 0; `5 insertions(+)`, `5 0 corpus/README.md` in `--numstat` |
| `verify_corpus_integrity.file_column_tokens` on patched README | the three intended paths present, one token each; 169 → 172 column-2 patterns |
| coverage-map shape splitter, patched vs base | no new off-shape row (the two 4-cell rows at 12 and 18 exist at base too) |
| `cd clone3 && python3 -B verifiers/verify_corpus_integrity.py` (base, direct capture) | `tracked=152 unindexed=1 stale=0 missing=0 (169 patterns)`, exit 1 |
| same gate, patch + the two indexed targets present (stubs, committed in clone2) | `tracked=154 unindexed=0 stale=0 missing=0 (172 patterns)`, exit 1 — remaining DRIFTs `tracked_files` baseline + four `corpus.pointers.*` |
| `python3 -B verifiers/check_allowed_tools.py --repo clone --rev 398cbe1…` (r79 draft counter placed in the clone) | `allowed-tools surfaces backed 0 of 6`, `script-only world: 0 of 6`, `entry … absent at 398cbe1…`, exit 1 |

The index class the rows exist to move (`unindexed`) reads 1 → 0; the `tracked_files` drift is the baseline refresh's (E03/L1 at the final pre-report commit), and the four pointer DRIFTs are repairs 4–5's (E04/E05). Nothing red in either run is attributable to the new rows.

## Touched surfaces

Written: `.ufo/waves/round-80/build/Kb80S08ReadmeRows.md`, `.ufo/waves/round-80/build/Kb80S08ReadmeRows.patch`, four receipts under the same directory, and this report. Nothing else in the lane, the fleet repo, `verifiers/`, `corpus/`, `SKILL.md`, `PROVINCE.md`, `MANIFEST.json`, `templates/`, `scripts/`, `.ufo/state/` was written; the lane's `corpus/README.md` is unchanged on disk (the change is only the patch). No git mutation in the lane (read-only `git log/merge-base/ls-tree` only); all clones are `--shared` copies under `/fast/scratch/hyaku/kotoba-r80/Kb80S08ReadmeRows` with `rev-parse --show-toplevel` asserted.

Coordination: replied to `Kb80E10Battery` that this seat owns none of E01–E06 and publishes only the README rows + note + patch.

## Out of scope / deliberately not done

- No after-value for either claim: the C1 tip battery (≈104 s, L1's post-integration measurement) was not run by this seat; the C2 tip score was not measured either.
- No live fetch: all page strings are quoted from committed snapshots; live re-open is R03's receipt.
- No edit to the lane's `corpus/README.md`, the two Frontier table rows, or any existing coverage row (the patch is add-only, 0 deletions).
- No counter scoring, no SCORECARD/LOG/MANIFEST writes, no pacman, no tool install.

## Findings for the closure

1. **Reconciliation duty on the counter labels (highest risk).** `.ufo/waves/round-80/build/check_allowed_tools.py` (mtime 20:19, sha256 `74e067cc…`) is **byte-identical to the r79 draft** (`cmp` exit 0 against `.ufo/waves/round-79/build/check_allowed_tools.py`): it prints `allowed-tools surfaces backed N of 6`, `TARGET = 5`, `ENTRY = corpus/knowledge/allowed-tools-surfaces-round79.md`, `script-only world`. The round-80 plan freezes different bytes (`documented N of 6`, `generator world: M of 6`, exit 0 iff N == 6), and row 3 / the Frontier note quote the plan's form. The lane has no `verifiers/check_allowed_tools.py`. If the draft is what lands, the C2 predicate is unmet by construction and row 3 must be reconciled; if the redesign lands, row 3 stands. A row that quotes a counter must match that counter.
2. **`MANIFEST.sha256` is not in `round-79/snapshots/`** — only the six per-file `S2xx.manifest` fragments. `Kb80N01Sentinel-MANIFEST.proposed` is the assembled six-line file; `Kb80S01Lesson-evidence.txt` records `sha256sum -c` over the six pins exit 0 and `Kb80K01-receipts.txt` gives live hashes. Row 3 and the note cite the assembled path because C2 conjunct (c) requires it; it is a landing dependency.
3. **`w1/Kb80ReopenSix.md` is not present at write time** (only `build/Kb80R03ReopenSix-S22*.fetch.json`). The rows do not cite that path, so they do not depend on its name.
4. **Pre-existing coverage-map shape defect**: lines 12 and 18 split into four cells at base as well. Not introduced or touched here, but a three-column reader will misparse them.
5. **Order matters for the baseline refresh**: running `refresh-corpus-baseline.py` before `corpus/lessons/round-80.md` and `corpus/knowledge/allowed-tools-surfaces-round80.md` land would bake in `tracked=152`; the plan's "final pre-report commit" ordering is load-bearing.
6. **Row checks that are cheap to re-run**: the nine discernment rows and the 3-of-6 best-world figure were measured from the committed spot-check; the lesson's M80-2 figures (17 B / 24,897 B) match the draft lesson. Rows are matched to the current files, not to a remembered version.
7. **Stray untracked directory in the lane**: `git status --porcelain` at write time shows `?? .ufo/wapes` (empty, 4 KiB dir block, `find` lists nothing inside). Not created by this seat — I wrote only under `.ufo/waves/round-80/build/` and `.ufo/waves/round-80/w1/`. It looks like a seat's typo; the integration should remove or account for it so the tip's tracked/untracked reconciliation is clean.
8. **Plan-vs-measurement conflict on C1's commit tokens (recorded, not mine to fix)**: `plans/round-80.md` § C1 names `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5` as the two `commit_unresolvable` subjects, but the gates' own detail reads `corpus/SOURCES.md:171` and `:172`, both token `7bb48f213ac677f943d5c791199ed3dddf302f00`; the plan's two are explicit `owner/repo@<hex>` citations the gates classify elsewhere. The fetch records resolve that hex: `S231.fetch.json` (ls-remote) makes it the mistral-vibe head, while `S230.fetch.json` records pi-mono's main as `bb65e3e4…` (r80 re-open `85c2ee3e…`) and its docs commit as `25cc5c7bf…` — so `:172` (S231) is right and `:171` (S230) carries the wrong repo's hash. A line-scope INFO class would silence that row-data defect, so C1's "2 → 0" must be reported classification-only with an appended correction row owed. Recorded verbatim with commands and receipt line numbers in `build/Kb80S08ReadmeRows-plan-conflict.txt` (Resolution section appended). It does not touch this seat's rows or patch.

## Limits

- The patch has not been applied to the lane; the L1 applies it (or pastes from `build/Kb80S08ReadmeRows.md`) in the integration commit, then runs the baseline refresh.
- Stub files used in the index test are fixtures and are named as such in the receipt; they are not proposed content.
- Scratch removed after receipts were copied (no residue claimed on trust: the removal is my own action, checked by absence).

VERDICT: three coverage rows + one append-only Frontier note delivered as drafts and a tested README-only patch (index `unindexed` 1 → 0 when their targets land; result README sha256 `9db6cc91…`; no after-value claimed; counter-label and MANIFEST dependencies named).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80S08ReadmeRows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S08ReadmeRows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S08ReadmeRows.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S08ReadmeRows-index-test.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S08ReadmeRows-c2-base-draft.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S08ReadmeRows-integrity-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S08ReadmeRows-integrity-with-rows.txt
