# ExecC1Fetch — round-68 wave 1 — the C1 counter's `--fetch` arm

Axes: depth (C1 instrument), freshness (live-page measurement). Seat role: executor (writing).

## Deliverable

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-68/w1/drafts/fetch-arm-execC1Fetch.py`
(21,095 bytes) — a self-contained counter variant whose `--fetch` arm is this seat's assigned move.

**Path deviation, disclosed.** The assignment names
`.ufo/waves/round-68/w1/drafts/check_client_trust_gates.py` as the target path. That path was
being rewritten by a concurrent seat while this seat worked: between 23:04 and 23:16 the file
changed at least three times (22:59 log stub → 15,767 B at 23:04 → 22,621 B at 23:16). This seat
wrote its arm to the assigned path at ~23:14 and the file was overwritten again before the next
process exec'd it (evidence below). To avoid clobbering a live worker, the arm is preserved at
`fetch-arm-execC1Fetch.py` for the L1 to merge. Nothing outside `.ufo/waves/round-68/w1/drafts/`
was written except this report.

## What the arm does (the assigned contract, exactly)

- For each cited row: reads the row's `source` cell, extracts the URL
  (`https?://[^\s,;)\]]+`), fetches with `curl -sSL --max-time 30` (urllib fallback only if
  curl is missing), and searches the fetched text for the entry's located quote after
  whitespace normalization. HTML pages are reduced to visible text first (`<script>`/`<style>`
  dropped, tags → spaces, entities unescaped) — measurement fidelity, not leniency.
- Quote resolution: the span after the explicit `located quote "` marker in the entry's
  `source:` line; fallback = the longest entry quote occurring in the row's `anchor` cell.
  (Preferring the marker avoids the section-name trap: `the "Trust" section` is also a quoted
  span that occurs in the anchor cell.)
- Prints one line per cited client — `S### <client>: found` / `NOT FOUND` /
  `FETCH FAILED <error>` — then `live quotes found N of 5`. The client name is the first
  ` — ` field of the row's `source` cell.
- A fetch failure is never counted as found and never crashes: each fetch is individually
  try/except'd; exit 2 is reserved for usage/environment errors of the counter itself.
- Exit codes: 0/1 mirror the content verdict (frozen predicate: exit 0 iff N == 5); the fetch
  block is a printed measurement. Documented in the docstring.
- Core deltas vs the installed `verifiers/check_client_trust_gates.py`, both disclosed:
  (1) `--rev` first runs `git rev-parse --verify <rev>^{commit}` so an unknown revision
  reports `environment error: unknown revision …` instead of surfacing as a misleading
  "cannot read corpus/SOURCES.md at <rev>"; (2) `--fetch` guards the entry/registry reads, so
  an entry-absent world prints `live quotes found 0 of 5` instead of tracebacking.

## Evidence (commands as run, output verbatim)

### 1. Dry run against the lane's current tree (live fetches, 2026-10-24 ~23:2x)

```
$ python3 -B .../w1/drafts/fetch-arm-execC1Fetch.py --fetch ; echo EXIT=$?
client trust gates backed 5 of 5
S198 VT Code: found
S199 Parallel Works: found
S200 Kilo Code: NOT FOUND
S201 Microsoft Agent Framework: found
S202 Mistral AI Vibe: NOT FOUND
live quotes found 3 of 5
EXIT=0
```

The task anticipated `0 of 5` (frozen before the L1 landed the entry, the five S198–S202 rows
and the coverage-map row; all three are in the working tree now). The content verdict is 5 of 5;
the live measurement is 3 of 5. Both numbers are reported; neither was adjusted.

### 2. The two NOT FOUNDs are representation gaps on the live pages, verified directly

- **S200 `https://kilo.ai/docs/customize/skills`** (HTTP 200, 138,104 B): the sentence exists
  but an inline code span splits it — the served HTML/JSON reads `Project skills (` +
  code-node `.kilo/skills/` + ` in a repository) and skills fetched from remote URLs never
  execute commands; their placeholders are replaced with a marker noting the skill is
  untrusted.` After tag-stripping the normalized text is `… Project skills ( .kilo/skills/ in
  a repository ) …`, so the staged contiguous span (16 words) does not occur.
- **S202 `https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md`** (HTTP 200,
  74,355 B): line 755 is `2. **Standard Agent Skills path** (project root, trusted folders
  only): …` — the `**` emphasis markers sit inside the staged 9-word span, so the contiguous
  whitespace-normalized span does not occur in the raw bytes. It does occur in the rendered
  page. A urllib fetch with the other arm's UA reproduces the same absence
  (`located quote present (urllib): False`) — not a transport artifact.
- Control: S198's raw page contains `untrusted resource data` (grep count 1); S198/S199/S201
  found by this arm.

**Not arm bugs; not fabrications.** The concurrent arm printed `fetch S200: found` /
`fetch S202: found` one minute earlier because its quote resolution takes the FIRST entry quote
that occurs in the anchor cell — the section-name spans `"Shell commands in skills"` and
`"Skill Discovery"` occur there and on the live pages (heading/TOC), so it "found" a section
name, not the located quote. This is precisely the discrimination the ReviewC1Counter seat was
asked to attack. The L1 must decide: either re-stage the two quotes to contiguous raw bytes
(S200: drop the code span from the staged span or quote the surrounding prose; S202: quote the
rendered page via its HTML URL, or include the `**` markers), or relax the matcher to ignore
markdown emphasis/inline-code markup. Both options are content/contract decisions above this
seat's scope; no row, entry or matcher behavior was changed unilaterally.

### 3. Crash-safety fixtures (the contract's hard clauses)

Entry-absent world (copy of lane corpus without the entry, `--repo` pointed at it):

```
fetch: no cited rows — corpus/knowledge/client-trust-gates-round68.md is absent; fetched nothing
client trust gates backed 0 of 5
  - entry missing: corpus/knowledge/client-trust-gates-round68.md
live quotes found 0 of 5
EXIT=1
```

Unreachable-URL world (entry citing `https://127.0.0.1:9/x`):

```
S198 VT Code: FETCH FAILED curl exit 7: curl: (7) Failed to connect to 127.0.0.1:9 after 0 ms: Could not connect to server
live quotes found 0 of 5
EXIT=1
```

No traceback in either; the fetch failure is not counted as found; exit 2 was not used.

### 4. Self-test of the variant core (offline; the counter-test seat's arm, unchanged in shape)

```
PASS honest world: backed 5 of 5
PASS broken world rejected: (10 worlds: entry missing, no source line, id does not resolve,
  row not mined, source cell absent from the entry, no verified-at, no recheck,
  no coverage-map row, quote not in the anchor cell, table row loses the quote)
PASS missing-entry classification: backed 0 (content verdict)
self-test: 0 failure(s) over 12 assertions
SELFTEST-EXIT=0
```

### 5. Collision record (why the deliverable path moved)

Four concurrent processes against the assigned path in one batch returned three different
behaviors: the dry run printed `fetch S198: found` (no client name — the concurrent arm's
format); a fixture run tracebacked at `line 268` reading the entry unguarded (the concurrent
arm's shape); the self-test printed `48 assertions` with world names
(`client-name-absent`, `class/unknown-rev/git-init`) that exist in no version this seat wrote,
and was RED (`self-test: 5 failure(s)`) — the concurrent seat's own work-in-progress. `stat`
confirmed 22,621 B / mtime 23:16:14 at that moment. This seat then stopped writing the shared
path (never clobber a live worker) and preserved its arm at the variant path.

## Risks / hand-offs for the L1

1. **The C1 `--fetch` conjunct does not hold at 5 of 5 today** under a strict located-quote
   reading: 3 of 5 (S200, S202 are representation gaps, evidence above). The frozen plan's
   `--fetch` sentence ("finds each of the 5 located quotes on its live page") needs either
   re-staged quotes or a markup-aware matcher before the round claims it. Do not ship the
   concurrent arm's `5 of 5` as the freshness receipt: its first-match-in-anchor logic can
   "find" a section heading.
2. The assigned drafts path is a live-edited shared file; whoever installs to `verifiers/`
   must pick one arm. Merge surface of this variant: `_http_get`, `_visible`, `_client_name`,
   `_located_quote`, `fetch`, `_verify_rev`, `_default_repo` (draft-relative `--repo` default),
   plus the docstring's fetch contract.
3. Exit-code semantics of this arm: fetch results never change the exit code (0/1 = content
   verdict; 2 = counter usage/environment). If the round wants `--fetch` to fail hard on
   <5, that is a one-line change the L1 must freeze deliberately.
4. `--self-test` here covers `check()` only; the fetch arm is covered by the live dry run and
   the two fixtures above, not by an offline self-test (a local-HTTP fixture would be the
   mutation-tester seat's move).
