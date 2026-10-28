# Kb81S11GateQuotes — seat report (kotoba round 81, w1)

Leaf scribe, located-quote ledger. Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Access date 2026-10-27 local (fetch instants 2026-10-28T02:27–02:32Z, TZ −03).
Full ledger: `.ufo/waves/round-81/build/Kb81S11GateQuotes.md`.

## What was measured

**S249 — located quote.** The row as S05's patch writes it carries
`located quote "the allowedTools option (allowed_tools in Python) in your
query configuration"` — 10 words, contains `allowedTools`, snapshot
`.ufo/waves/round-81/snapshots/S249.md` (28 395 B, sha256 `ac62c2df…`).
It occurs **1** time in the declared Markdown text view (view line index 234,
char 18 963; `grep -cF` on `Kb81S11GateQuotes-S249.view.txt` = 1) and **0**
times in raw bytes (backticks). Raw provenance: line 348, `allowedTools` at
byte 19 928. Q70 passes (first heading at view index 3, quote at 234).

The entry's primary quote (`frontmatter or with the allowedTools option
(allowed_tools in Python) in your query configuration`) is 13 words, 1 view
occurrence at char 18 943, same raw line.

The 23-word round-80 line-348 quote ("In SDK sessions … with the allowedTools
option") occurs **0** in raw and **0** in the declared view; only a
link-stripping view makes it 1. E08's draft avoids it and records it as an
inherited S248 defect.

Snapshot provenance: this seat fetched the page independently at
`2026-10-28T02:27:03Z` — HTTP 200, 28 395 B, sha256 `ac62c2df…`, `cmp` vs the
landed snapshot rc=0. E08's fetch record (`:27:26Z`) and R03's two fetches
agree; the r80 committed copy `Kb80S05-agent-sdk-skills.md` is byte-identical.

**S250 — supersede row's located fact.** The row (own-work, tier A, mined)
carries the hash once and states, in 15 words quotable from the row itself:
"that commit is mistralai/mistral-vibe's refs/heads/main (ls-remote
2026-10-28T02:28:05Z) and absent from pi-mono (GitHub commits API 422)".
Grounds, re-measured by this seat: `git ls-remote` mistral-vibe → `7bb48f21…`
`refs/heads/main` (rc 0); pi-mono full advertisement → 4 120 refs, **0** hits,
head `a9228305…`; commits API `badlogic/pi-mono` at that sha → HTTP **422**;
commit-pinned mistral-vibe README at that sha → HTTP 200, 77 634 B,
`fc48a5db…`, `cmp` vs `S231-vibe.md` rc=0. The committed r79 record
`S231.fetch.json` binds the hash to the repo in its own note (quote 10 words,
1 occurrence); the lane and fleet both return rc=128 for the object
(`git cat-file -t`). E03's manifest entry and S05's binding receipt agree.
pi-mono heads are dated: `bb65e3e4` (r79 fetch, committed note), `85c2ee3e`
(r80 reopen, committed), `a9228305` (r81 live).

**Rows and where their bytes live.** S248 (queued; `used-by` → the new entry):
claims the same 28 395 B / `ac62c2df…` page, bytes at `S249.md` and the
committed r80 copy; its 23-word quote is the 0-occurrence one. S249 (mined,
tier A): anchor pins `S249.md` + `S249.fetch.json`, quote as above. S250
(mined, tier A): anchor/teaches pin the binding to committed
`S231.fetch.json`/`S230.fetch.json` plus the r81 ls-remote receipts and E03's
manifest. S230 (unchanged audit trail, line 171): 4 793 B / `5b980552…`,
quote `Experimental pre-approved tool list` (line 78, byte 3 578, 1
occurrence); its commit attribution is the defect S250 corrects.

At read time `corpus/SOURCES.md` still has 174 rows and no S249/S250 — the row
bytes live only in `Kb81S05SourcesEdits.patch`; `S249.*` is untracked; the C2
counter `verifiers/check_sdk_allowed_tools.py` and the entry
`corpus/knowledge/allowed-tools-sdk-round81.md` do not exist. The ledger
therefore verifies working-tree snapshot bytes, not a committed tip; L1 must
commit `S249.md` unmodified.

## Findings

1. **F1** S248's 23-word line-348 quote is 0 in the declared view; the entry
   must use the 10/13-word query-config span. E08 agrees; S248's anchor is not
   rewritten this round.
2. **F2** S248 and S249 share a URL. Census E04 fires only when URL+scope
   repeat without `supersedes S###`; measured on synthetic rows (same scope →
   E04; different scope → W04; same scope + `supersedes S248` → no E04).
   Landed S249 uses a different scope, and S05's census run exits 0 with W04
   32 vs 31. Any later scope copy into S249 without a supersedes clause fails
   the census.
3. **F3** E08's `entrycheck` reports 11 MISS spans that do occur in the
   declared view (`grep -cF` = 1 for the tested line-46/line-389 strings); its
   checker drops backticked token content. The primary quote reads OK occ=1.
   The C2 counter's `(d)` reviewer should use the declared view.
4. **F4** Snapshot, receipts, rows and entry are uncommitted at read time; the
   C2 claim's `(c)` pin depends on L1 committing `S249.md` byte-for-byte.
5. **F5** The row's `fetched 2026-10-27` is local (−03); the UTC instant is
   `2026-10-28T02:27:26Z`. Both are true of one fetch; date-stamp any copy.
6. **F6** "Absent from pi-mono" is evidenced by the advertised-ref sweep
   (bounded: unreferenced objects are not observable) and the commits API 422.

## Receipts

`.ufo/waves/round-81/build/`: `Kb81S11GateQuotes.md` (ledger),
`Kb81S11GateQuotes-verify.py|.json|.txt`,
`Kb81S11GateQuotes-S249.view.txt`, `Kb81S11GateQuotes-grep.txt`,
`Kb81S11GateQuotes-binding.txt`, `Kb81S11GateQuotes-census-dup.txt`,
`Kb81S11GateQuotes-final-sweep.txt`. Consumed: E03 manifest + ls-remote
receipts, E08 snapshot/fetch/probe/entry, S05 patch + binding + census
receipts, R03 reopen report, S16 quote receipt. No tool installed; no pacman;
scratch `/fast/scratch/hyaku/kotoba-r81/Kb81S11GateQuotes/` removed.

VERDICT: S249's 10-word row quote and 13-word entry quote each occur once in the declared view of the pinned snapshot (line 348, `ac62c2df…`, independently re-fetched), S250's binding is verified against mistral-vibe primary bytes and pi-mono's 422, the 23-word inherited quote is 0 in view and unusable, and all these bytes remain uncommitted at read time.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S11GateQuotes.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-verify.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-verify.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-verify.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-S249.view.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-grep.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-binding.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-census-dup.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S11GateQuotes-final-sweep.txt
