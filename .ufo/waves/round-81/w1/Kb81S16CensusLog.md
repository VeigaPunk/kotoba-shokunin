# Kb81S16CensusLog — seat report (round 81, w1)

Leaf seat: no subagents, no background jobs. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
base `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Assignment: the census **old→new log** for every
`corpus/SOURCES.md` cell round 81 changes, in the round lesson's `## Gate` paste-ready form, plus the
before/after row-count lines with their commands.

## Behavior delivered

1. **The ledger** — `.ufo/waves/round-81/build/Kb81S16CensusLog.md`. §1 paste-ready Gate block,
   §2 per-cell ledger (S248 one cell, S249 and S250 eleven cells each), §3 row-count lines and the
   histogram with commands, §4 the constraints the cells were written against, §5 the one measurement
   this seat did not perform.
2. **Authoritative row text** — `Kb81S05SourcesEdits.patch` (sha256 `6d0d5717…`, `+4 −2`). It landed
   while this seat was working; every value in the ledger is transcribed from it and **re-measured by
   this seat** at fixture rev `c5753ac89eb00b6f5f3ba53ea1f2dba567c97aad` (clone of base + that patch +
   empty placeholders for the two `used-by` targets). This seat's own independently derived row set
   (`Kb81S16CensusLog-SOURCES-rows.superseded.patch`, sha256 `5e2c141b…`) is kept only as the derivation
   record; the four design deltas are named in the ledger §4.
3. **Measured numbers** (delivered patch): rows `174 → 176`; census `exit 0, ok, 31 W04 → exit 0, ok,
   32 W04, 0 E-codes`; histogram `A 135→137, B 22, C 17, mined 149→151, queued 8, rejected 17`;
   `commit_total` 46 unchanged, `report_total` 111 unchanged, `commit_truncated` 0→1 (not a baseline key),
   `.ufo/reports/` pointers 0→0.

## Gates run (each command's own exit; no pipeline verdicts)

| command | result | receipt |
|---|---|---|
| `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` (lane, base) | **exit 0**, `kotoba ok`, 31 W04, 174 rows | `build/Kb81S16CensusLog-census-base.txt` |
| `sources-census.sh census --root … kotoba` | exit 0, `rows 174`, A 135 / B 22 / C 17, mined 149 / queued 8 / rejected 17 | same |
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `174` exit 0 | same |
| `git apply --check` + `git apply` of `Kb81S05SourcesEdits.patch` at base (scratch clone) | exit 0 / exit 0 | `build/Kb81S16CensusLog-census-S05.txt` |
| `sources-census.sh validate --root … <fixture>` | **exit 0**, `ok`, **32 W04**, **176 rows**, **0 E-codes**, 11 cells on each touched row | same |
| `sources-census.sh census --root … <fixture>` | exit 0, `rows 176`, A **137** / B 22 / C 17, mined 151 / queued 8 / rejected 17 | same |
| `verify_corpus_integrity.py --repo <fixture>` | exit 1 on pre-existing drifts only; `report_dead=1/111`, `commit_total=46`, `unresolvable=2`, `nonhash=0` — identical to base | same |
| `verify_corpus_independent.py --repo <fixture>` | `report_dead 0 PASS`, `commit_total 46 INFO`, `commit_unresolvable 2 DRIFT` (the R2 blocker), `commit_nonhash 0 PASS`, `unindexed 3 DRIFT` | same |
| quote-span check on the committed `snapshots/S249.md` (28,395 B, `ac62c2df…`) | S05's 10-word span: `occ=1` under link-preserving **and** label-only views, raw 0, line 348; draft's 23-word span: `occ=0` / `occ=1` respectively | `build/Kb81S16CensusLog-s249-quotes.txt` |
| read-only ref re-derivation (`git ls-remote`, 2026-10-28T02:33:14Z) | mistral-vibe `refs/heads/main` = `7bb48f21…`; pi-mono `refs/heads/main` = `a9228305…`; pi-mono 4,120 refs, **0** carrying the token | `build/Kb81S16CensusLog-lsremote.txt` |

No tool was installed or upgraded; `pacman` was not run (host-wide pause respected).

## Findings

**F1 — calibration: the lesson draft's round-start W04 count is a line count.** `Kb81S01Lesson.md:33`
prints "32 W04 duplicate-URL warnings, 174 rows". Measured: `receipts/census-before.txt` has **32 lines =
31 W04 + the `ok` line**, so the warning count at round start is **31**
(`grep -c $'\tW04\t' …census-before.txt` → `31`, exit 0; re-run `Kb81S16CensusLog-census-base.txt`).
32 is the **after** count. S05's own receipt §3 reaches the same diagnosis independently. Fix: 31 before,
32 after — both already in the paste-ready block.

**F2 — consistency: one placeholder and one view-fragile quote in the lesson draft.** (a)
`Kb81S01Lesson.md:18` still carries `pinned at {{HASH}}`; the pin is
`ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` (this seat's own fetch of the URL
reproduced 28,395 B and the same digest, so the pin is fetcher-independent). (b) The same line quotes a
23-word span that occurs **0** times under the link-preserving text view the C2 probe declares (the page
wraps the key in a Markdown link, so the link target splits "skill's" from "frontmatter") and only once if
the view also strips link targets. The S249 row already quotes the 10-word
`the allowedTools option (allowed_tools in Python) in your query configuration`, which occurs once under
**both** shapings; the lesson text should quote that span so Gate and row agree and conjunct (d) cannot
turn on an undeclared view. Not repaired here (the lesson is another seat's file).

**F3 — consistency: S248 is `queued` while carrying a real `used-by`.** `CORPUS.md` § SOURCES.md defines
`mined` as "cited by ≥1 path in `used-by`", but the delivered row keeps `status=queued` with
`corpus/knowledge/allowed-tools-sdk-round81.md` in `used-by` (and the lesson draft asserts no status cell
changes). No census code fires: E11 skips non-`mined` rows, W03 covers only the inverse (`mined` + `—`).
L1 decision: flip `queued → mined` (legal in place under rule 2, one extra old→new line — the only line in
the ledger that would change) or keep `queued` and accept the latent mismatch.

**F4 — operability: the new W04 line is by design; the E04 trap is next to it.** S249 is the same page as
S248 at a different scope, so the census emits one warning. Copying S248's scope cell verbatim would be an
`E04` **error** (duplicate URL + identical scope + `teaches` not opening `supersedes S24?`,
`scripts/sources-census.sh:646-649`) and would also violate the C2 counter's canonical-URL conjunct.
Measured on the delivered rows: 0 E-codes.

**F5 — token and pointer accounting: no counted citation, one new truncated token.** `commit_total` stays
`46`; the single added ``commit `<hex>` `` shape is `commit `25cc5c7b…`` (truncated) which lands in the
existing `commit_truncated` class (`0→1`) — an INFO/observable counter, not a baseline key
(`verifiers/corpus-baseline.json` holds only `commit_total` / `commit_unresolvable` / `commit_nonhash`).
`report_total` stays `111`; `UFO_POINTER_RE` (only `.ufo/reports/round-N/*.md`) matches 0 in all three
touched rows. So the R4 refresh is driven by `tracked_files`/`unindexed` and the r80 lesson's index row,
not by these cells.

**F6 — freshness is now three-legged.** The SDK page is byte-identical across the r80 scout fetch, the r81
entry seat's two fetches and this seat's fetch (`ac62c2df…`, 28,395 B). mistral-vibe's `main` has not moved
across r79 → r81 (`7bb48f21…`). pi-mono's head moved `bb65e3e4…` (r79, committed note) → `85c2ee3e…` (r80
reopen, committed `Kb80R03ReopenSix-S230.fetch.json`) → `a9228305…` (now, this seat's own `ls-remote`), and
the token is absent from all 4,120 advertised refs plus the GitHub commits API (HTTP 422, S05 receipt) and
the commit-pinned raw path (HTTP 404, same receipt). The S250 `teaches` states exactly this.

**F7 — provenance: two independent derivations, one authoritative.** `build/` carried no SOURCES-edits
output when this seat read it; S05's patch landed at 23:33 and is authoritative. The four deltas against
this seat's derivation are recorded in the ledger §4 (S249 tier A vs B — the delivered A is justified by
scope and is contract-conformant; S250 `own-work` probe vs `code` repo — the delivered form adds the 422
disproof and the 301 alias and is strictly stronger; S248/S250 `used-by` composition). Nothing was merged
silently; the superseded artifacts carry the `.superseded` suffix.

**F8 — consistency: S248's `used-by` value differs between the patch and the lesson draft.**
`Kb81S05SourcesEdits.patch` writes `corpus/knowledge/allowed-tools-sdk-round81.md` (entry only);
`Kb81S01Lesson.md:35` states `corpus/knowledge/allowed-tools-sdk-round81.md, corpus/lessons/round-81.md`.
Both satisfy C2 conjunct (e), but the Gate must print the value that actually landed, so the lesson line
needs correcting to entry-only (or the patch's cell widened — then E11 needs the lesson too, which lands in
the same commit anyway). Recorded, not repaired: the row is S05's file.

**F9 — freshness nit in a peer receipt.** `Kb81S05SourcesEdits-census.txt` names the patch under test as
sha256 `142c9ea6d8201a586dface732b9a3c2ef1f66c81cb0d5756fc4aa8f169e8024f`, while the delivered patch hashes
`6d0d571795341fb99bb2ce326e48a3c6f805857376e0b93d06b5d4848ecea2c0` — the receipt predates the anchor
rewrite S05's report describes. The counts are unaffected, and this seat re-measured them on the delivered
bytes (rows 176, 32 W04, 0 E, A 137 · B 22 · C 17), so the ledger does not rest on the stale digest.

## Touched surfaces

Written (only these, all under the round-81 wave dir):
`.ufo/waves/round-81/build/Kb81S16CensusLog.md`, `Kb81S16CensusLog-census-base.txt`,
`Kb81S16CensusLog-census-S05.txt`, `Kb81S16CensusLog-census-after.superseded.txt`,
`Kb81S16CensusLog-committokens.superseded.txt`, `Kb81S16CensusLog-lsremote.txt`,
`Kb81S16CensusLog-s249-quotes.txt`, `Kb81S16CensusLog-SOURCES-rows.superseded.patch`, and this report
`.ufo/waves/round-81/w1/Kb81S16CensusLog.md`. Scratch under
`/fast/scratch/hyaku/kotoba-r81/Kb81S16CensusLog/` was removed after the receipts were copied out. No lane
file was edited; no git/jj mutation outside the scratch clone; lane git used read-only. The lane tip moved
during this seat's run from `b2842231` to `e6d48e6a9b11da4660df8145bd2f28c3238c5b83` (the L1's plan-freeze
commit: `plans/round-81.md` +62, nothing else — `git diff --stat b2842231..HEAD -- corpus/ verifiers/`
prints nothing), so every base reading above still applies unchanged to the tip, and `corpus/SOURCES.md`
at the tip is still 174 rows with no S249/S250 (the integration is the L1's, not this seat's).

## Out of scope (other seats / L1)

The C2 counter and its self-tests (C2 seats), the C2 knowledge entry text (`Kb81E08C2Entry`), the
`external-commits.json` manifest and the two gate patches (C1 seats), the R4 baseline refresh and index
row (L1/R4), the `## Search log` prose note for this round's bounded SDK search (rule 5 — no seat in
`build/` has produced one; a bounded search that adds S249 should carry one), and the `## Gate` paste
itself (`Kb81S01Lesson`, which still carries `{{HASH}}`, the 23-word quote and the entry+lesson `used-by`
line named in F2/F8).

VERDICT: The census old→new ledger is complete and re-measured on the delivered `Kb81S05SourcesEdits.patch` (sha256 `6d0d5717…`) — 174→176 rows, 31→32 W04, 0 E-codes, exit 0, `commit_total` 46 and `report_total` 111 unchanged, one new truncated-token INFO — with one changed cell (S248 `used-by` `—`→entry) and two 11-cell new rows (S249 `docs/A/mined` on the view-safe 10-word SDK quote against the pinned snapshot; S250 `own-work/A/mined` opening `supersedes S230 —` with the commits-API 422 + 301-alias disproof), and four defects reported to their owners rather than repaired: the lesson draft's 32-vs-31 round-start W04 (it counts the `ok` line), its `{{HASH}}` pin and 23-word quote that fails the declared link-preserving view, its S248 `used-by` value disagreeing with the patch, and S248's `queued` label surviving a real `used-by`.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S16CensusLog.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S16CensusLog-census-base.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S16CensusLog-census-S05.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S16CensusLog-s249-quotes.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S16CensusLog-lsremote.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S16CensusLog-SOURCES-rows.superseded.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S16CensusLog.md
