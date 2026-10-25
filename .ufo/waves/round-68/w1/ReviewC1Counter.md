# Review C1 counter — contract attack (round 68, wave 1)

Seat: reviewer (read-only). 2026-10-24.

**The draft does not exist.** `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-68/w1/drafts/check_client_trust_gates.py`
→ `ERROR: ... does not exist`; `w1/drafts/` is absent (`ls` exit 2). Per instruction, **the CONTRACT is attacked instead**:
the frozen predicate `client trust gates backed N of 5` as frozen in `plans/round-68.md` L39–76 (three predicate lines L42/48/49,
counter-semantics L66–70, landed shape L59–63, bound L73–75). Every finding below cites plan lines or repo bytes; grep output is
reported literally, never as semantic proof.

## Ground verified at the base

- `git rev-parse --verify e94ae32a5cd8dc3ee8e2d247816784bec2750cc0^{commit}` → resolves (full hash echoed).
- `git grep -il <token> e94ae32a… -- corpus/` → **0 hits** for `vtcode`, `parallelworks`, `kilo\.ai`, `agent-framework`, `mistral`, `trust-gate`.
  The before-line (plan L52–57) is real: the do-nothing world cannot reach 5 of 5 at the base.
- Base `corpus/README.md` coverage map has no trust row (only unrelated hit: "trust input" in a round-41 row).

## Findings

### A1 — HIGH — `--fetch` input source is unpinned; the stub world can pass all three frozen lines
**Attacked:** copy-satisfiability of the frozen predicate.
**Evidence:** plan L49 pins `--fetch finds each of the 5 located quotes on its live page` — but not *whose* five quotes. If the counter
holds five quote strings as module constants, `--fetch` verifies the constants against live pages while the landed entry cites different
(fabricated) bytes; the `--rev` path is byte-local (plan L73–75, QUALITY Q33 — accepted documentary bound) and never compares to live
pages. Constructed world: fabricated `client-trust-gates-round68.md` with five rows + five fabricated `status mined` SOURCES rows
+ one coverage row → `--rev <rev>` = `5 of 5` exit 0, `--rev <base>` = `0 of 5` exit 1, constants-based `--fetch` green. Every conjunct
passes with no live page ever opening *for the landed claim*.
**Fix:** the contract must state `--fetch` extracts each quote from the **measured rev's own entry/anchor bytes** (same loader seam as
`--rev`), fetches the exact canonical URL from the row's source cell, and exits nonzero when any quote is absent; the claim receipt runs
`--fetch` against the landed rev.

### A2 — HIGH — `--fetch` has no pinned exit code and no 404/boilerplate/redirect discrimination
**Attacked:** discrimination power of the fetch arm; the exit-1/exit-2 boundary.
**Evidence:** plan L49 is the only predicate line with **no exit code** (contrast L42 exit 0, L48 exit 1). Unspecified cases:
(a) a ≤25-word quote containing client boilerplate ("skills", "untrusted", "instructions") substring-matches a navigation menu,
breadcrumb or related-articles block — including on a *different* page of the same domain if URL equality is not pinned;
(b) a soft-404 (HTTP 200 + "page not found" template) passes a status check and "finds" any quote present in the site template;
(c) a cross-host redirect to a domain root makes a quote count as "on its live page" when the cited page is gone.
Also unpinned: quote-absent-on-200-page (content verdict — must exit 1) vs transport failure (environment — exit 2). Plan L66–70
classifies only rev-path cases; the fetch arm inherits exactly the R67-1 ambiguity the round exists to close.
**Fix:** pin — fetch the row's canonical URL verbatim (reject cross-host redirects), require HTTP 200, case-sensitive verbatim
substring of the anchor-cell quote; quote absent on a 200 page → exit 1 (content), network/transport error → exit 2 with **empty
stdout**; report which of the five failed. 404 on a cited URL should be treated as content evidence against the row, not "unreachable".

### A3 — MEDIUM — endpoints pinned, middle cases not: the present-but-hollow entry
**Attacked:** the R67-1 non-recurrence requirement (missing entry → `0 of 5`, exit 1).
**Evidence:** the contract does pin the missing-entry endpoint (plan L66–70) and the base genuinely exercises it (0-hit grep above).
Unpinned: entry exists but empty / without a table; 3-of-5 client rows; `SOURCES.md` blob missing at the rev; Registry heading renamed;
non-UTF-8 bytes. The landed r67 counter treats ANY unreadable blob as environment:
`verifiers/check_instruction_authority.py:71: raise EnvError(f"cannot read {path} at {rev}")` — a byte-for-byte repeatable defect one
file over. The r67 receipt (`.ufo/waves/round-67/receipts/C2-authority-measure.txt`) shows the base control printing
`environment error: cannot read …` + `exit=2` where the frozen line should have printed.
**Fix:** pin — every *readable* revision yields a content verdict (`client trust gates backed N of 5` on stdout, exit 1 when N<5)
regardless of which lane file is missing or hollow; exit 2 only for unresolvable revision / git failure / decode failure; stdout empty
on exit 2. The base-control receipt must show the exact line `client trust gates backed 0 of 5`.

### A4 — HIGH — `--self-test` seam unspecified; "breaks each conjunct" permits the r67 blind spot
**Attacked:** whether the self-test can be green while the `--rev` path is red.
**Evidence:** contract says only "`--self-test` that breaks each conjunct" (plan L62–63). Proof this is insufficient: the r67 receipt
shows `self-test: 0 failure(s) over 10 assertions` in the same file as the base control's `exit=2` — the r67 self-test never drove the
public `--rev` path, so the loader's misclassification was invisible to it. The corrected seam exists in the r67 draft
(`.ufo/waves/round-67/w1/drafts/check_instruction_authority.py` L424–469): monkeypatch `load_blobs`, drive public
`main(["--rev", rev, …])`, assert exact stdout line and exit codes 0/1/2.
**Fix:** the r68 contract must require the self-test to (a) drive public `main()` with the loader substituted at the same seam `--rev`
uses, (b) include the entry-absent world asserting the exact line `client trust gates backed 0 of 5` + exit 1 (the R67-1 regression
case), (c) assert exit 2 + empty stdout for unknown-revision and loader-failure worlds, (d) include a broken `--fetch` world if fetch
is a conjunct.

### A5 — MEDIUM — N's counting rule and the five client identities are outside the predicate
**Attacked:** what `N of 5` counts.
**Evidence:** the five clients (`vtcode`/`parallelworks`/`kilo.ai`/`agent-framework`/`mistral-vibe`) are named only in the Why paragraph
(plan L54–55), not in the frozen predicate. Nothing prevents five rows all citing one client, or one SOURCES row reused by two client
table rows, reaching `5 of 5` with fewer than five distinct grounded (client, source) pairs.
**Fix:** pin N = count of the five named clients, each backed by its own distinct SOURCES row whose anchor cell contains the entry's
located quote for that client; duplicates collapse N.

### A6 — MEDIUM — base-control ordering trap: a working-tree-reading counter passes both frozen lines
**Attacked:** rev-scoping enforcement of the base control.
**Evidence:** the before-line is "measured at the base e94ae32a" (plan L56) — i.e. **before landing**, when even a counter that ignores
`--rev` and reads the worktree prints `0 of 5`. After landing, that same broken counter prints `5 of 5` for `--rev <base>`, silently
voiding conjunct two — unless the receipt re-runs the base control post-landing, which nothing requires. The lane's own r66 cure:
`verifiers/check_r66_routed_repairs.py` L28 `BASE_REV_LITERAL = "11385e04e368c1e94ab1a5a89d7439033eb1f855"` with docstring L5–7
"the counter refuses to certify unless that base scores exactly 0 of 2".
**Fix:** require the r68 counter to hard-pin the base SHA as an internal conjunct, or require the landed receipt to re-run
`--rev e94ae32a5cd8dc3ee8e2d247816784bec2750cc0` **after** landing and show `0 of 5` / exit 1.

### A7 — LOW — landed-shape promises not enforced by the predicate
**Attacked:** gap between "landed shape" (plan L59–63: coverage-map row, SKILL.md pointer) and what the predicate enforces.
**Evidence:** the three frozen lines need not check the coverage row or the pointer; a half-landed world (entry + SOURCES rows, no
coverage row) would still print `5 of 5`, exit 0. The r67 draft enforced coverage indexing as conjunct 07.
**Fix:** add a coverage-index conjunct (and optionally the pointer check), or state explicitly that the predicate deliberately omits them.

### A8 — LOW — `--fetch` flakiness vs receipt reproducibility
**Attacked:** determinism of the fetch measurement.
**Evidence:** five live pages; quotes vanish, sites restructure, redirects move — a receipt re-run days later can flip red with no lane
change. The contract sets no stability guidance and no `recheck` cadence for the five rows.
**Fix:** name `--fetch` a one-time in-round measurement recorded in the receipt + the lesson's `## Gate` (URL, access date, quote), set
the five rows' `recheck` cells accordingly, never wire `--fetch` into an always-on gate.

### A9 — LOW (cross-claim, concrete) — C1's landing can flip C2 red through the baseline
**Attacked:** sequencing interaction between the two claims.
**Evidence:** R67-4's repair re-records `verifiers/corpus-baseline.json` (plan L117–119); C1 adds tracked files (the new entry; SOURCES.md
is already tracked). If the baseline is re-recorded before the C1 entry lands, `corpus.index.tracked_files` observed exceeds expected and
the C2 conjunct `9/9` fails.
**Fix:** land C1 files first, then re-record the baseline, then run the three C2 conjuncts (or re-record last with a full-battery rerun).

## Direct answers to the five attack questions

1. **Copy-satisfiable?** At the byte level, yes — by design (documentary bound, plan L73–75, QUALITY Q33). A stub entry + five
   lane-authored SOURCES rows passes both `--rev` lines. The only live-page discriminator is `--fetch`, so as written (A1/A2) the whole
   predicate is copy-satisfiable via constant quotes + fabricated rows; it is not, once `--fetch` is rev-derived and discriminating.
2. **Does `--fetch` discriminate?** Unspecified by the contract; plain substring matching accepts nav-menu, related-content and
   soft-404-template occurrences (A2).
3. **Missing entry → `0 of 5` / exit 1?** Pinned (plan L66–70) and genuinely exercised at the base (0-hit grep). Residual risk: hollow
   entry / missing SOURCES / malformed table (A3), the class of the landed r67 defect at `verifiers/check_instruction_authority.py:71`.
4. **Exit 2 vs exit 1?** Pinned at the two rev-path endpoints only; unpinned for the fetch arm (quote-absent vs transport) and for
   stdout hygiene (A2/A3). The r67 receipt is the observable failure mode to regress against.
5. **Is `--self-test` real?** The contract language permits the check()-direct shape that was green in the same receipt where r67's base
   control exited 2. Must be pinned to public-`main()`-at-the-loader-seam with the exact-line assertions (A4).

## Residual risk and verification gaps

- No code exists to execute; every finding is a contract-level construction, not a run of the counter. All five findings become
  executable attacks the moment the draft lands (stub world, hollow-entry worlds, wrong-rev world, constants-based fetch).
- `--fetch` behavior against the five live pages was not measured (no counter, no fetch performed this seat); reachability of the five
  client URLs is unverified here and must come from the landed `--fetch` receipt.
- C1↔C2 baseline ordering (A9) is a sequencing risk only; not measured because neither change has landed.
