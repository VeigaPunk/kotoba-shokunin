# ReviewNoHarmC1 — round-66 C1 false-red review (read-only seat)

Seat: reviewer (leaf; no dispatch, no production edits). Lane: kotoba. Date: 2026-10-24.
Axes inspected: depth (C1). Nothing here is a score, a claim edit, or an admission.

| Role | Value |
|---|---|
| Pinned base (`plans/round-66.md:3`) | `11385e04e368c1e94ab1a5a89d7439033eb1f855` |
| Measured tip (lane Git HEAD) | `2a8eba56b3f9321b70c569fa2816d42237ca49a2` |
| Instrument blame commit | `806b53b` "round-66: land G9 coupling and integrity fixes" |
| Committed instrument sha256 | `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` (equals `C1-measure.txt` and `C1-landed-measure.txt`) |
| C1 diff | `git diff 11385e04..HEAD -- verifiers/check_scoped_rules_v32.py` → 49 insertions, 16 deletions |
| Base ancestry | `git merge-base --is-ancestor 11385e04 2a8eba56` → true |

Method: base bytes were extracted with `git archive 11385e04 | tar -x -C /tmp/...` and measured
there; tip bytes were imported read-only from the lane file (`python3 -B`,
`importlib.util.spec_from_file_location`). No lane file, index, jj state, claim, counter,
threshold or receipt was written or changed. No tool was installed.

Caller/definition-check tooling (recorded per role): **no `lsp` device exists in this session's
tool registry** (available: `read`, `bash`, `edit`, `eval`, `glob`, `grep`, `task`, `wait`,
`web_search`, `write`, plus `xd://ast_edit` / `xd://debug`). Caller checks therefore used
module-level import plus `grep -rn` over `*.py`; grep output below is textual, not semantic
proof. The two names C1 introduces or deletes were checked by import, which is the strongest
available substitute: nothing imports `clause_need` or `g9_conjunct`, and `MIN_CLAUSE` has no
code reference at all.

## Verdict

C1 is confined to one-word clauses: `clause_need(n) = min(fwd_need(n), n)` equals `fwd_need(n)`
for every `n >= 2`, so no multi-word clause can change verdict. I found **one false-red class**
introduced by the coupling — a one-word clause whose only support at the cited line is inside a
backtick span is rejected (pure green→red flip; §F1) — which `ReviewC1ExistingWorlds` F3
reported first; F1 here adds the exhaustive trigger condition, the full-path flip, and the
negative bounds. I found **no page-absent double-report** (§F2) and **no `n >= 2` threshold
delta** (§F3, proven and measured). At the measured tip the change has **zero effect on
committed rows** (4 G9 calls, 7 clauses, no one-word clause; base and tip instruments produce
identical judge output).

## F1 — False red: one-word clause supported at the cited line only inside a backtick span

**Severity: Low (latent), invariant-level.** Reachability is low; the frozen invariant in
`plans/round-66.md:11` ("a one-word tail supported by the cited line remains accepted") is
universal, and this class falsifies it.

Minimal case (single-line page, `L = 1`), measured on committed tip bytes vs base bytes:

```
line  = "The tool runs `audit` checks."
page  = line
cell  = "The tool runs `audit` checks and audit."

base g9_conjunct  -> []
base action_conjunct -> []
tip  g9_conjunct  -> ['A2 G9: clause "audit." is supported outside the cited line']
tip  action_conjunct -> ['A2 G9: clause "audit." is supported outside the cited line']
```

This is a *pure* verdict flip: the cell is fully green at base (A2 forward `3/3 >= fwd_need(4)=3`,
page containment, reverse coverage, G7 all pass), and the tip rejects it only through G9. The
word `audit` is literally present in the cited line's raw text; the tip's message ("supported
outside the cited line") is false for this cell.

Trigger condition, exactly: a word that occurs in `lines[L-1]` **only inside a closed
`BACKTICK_RE` span**. Proof from the committed code: `content_words` (`:1008-1015`) applies
`BACKTICK_RE.sub` then `CITE_RE.sub` then `[a-z]{4,}` minus `STOPWORDS`; `page_words`
(`:1026-1034`) applies only `CITE_RE.sub` plus the same token rule. `CITE_RE` (`S\d{3,}\s*:\s*\d+`)
cannot match an `[a-z]{4,}` run, and `STOPWORDS` is applied identically on both sides, so the only
raw-line content word missing from `line_w` (`:1132`) is one inside a closed span. The clause side
(`:1145-1148`) counts spans, so the span word is page-supported and G9 fires.

Corpus-wide confirmation of that exhaustiveness: over the 119 tracked `SKILL.md` and
`corpus/**/*.md` files (17,498 lines), all **28,615** `[a-z]{4,}` token occurrences that
`content_words` drops from their own line lie inside a closed `BACKTICK_RE` span — **0**
outside-span (or citation-covered) misses. There is no other loss channel.

Negative bounds measured at the tip (same shape, one change each):

| Variant | Tip result |
|---|---|
| Word outside the span on the same line (`... \`audit\` checks nightly and checks.`) | `[]` |
| Unpaired backtick on the cited line (`The tool runs \`audit checks.`) — no closed span | `[]` |
| Word in a second closed span (`... \`audit\` checks and \`quota\` limits.`) | both span words stripped for the line side |
| Tail word from a multi-word span (`The tool runs \`alpha beta\` nightly.` + `and beta.`) | two reasons; the *verbatim first clause* is also red — that first-clause red is present at base, so the cell verdict is not flipped by C1 |
| Plain tail supported at the line (`and glob.`) or by 4-char prefix (`and scope.` for `scopes`) | `[]` — the landed control's direction holds |

Pinning gap: the only added positive control (`:2969-2973`) uses the unbackticked word `glob`
from `g9_line`, so the backticked boundary is unstated; the negative must-fail arms (`:2980-2998`)
use a page-present, line-absent tail and cannot see it either.

The asymmetry is in the *line* set only. G7 already carries the raw-line escape
(`token not in raw_line`, `g7_conjunct` `:1052-1054`); G9 has no equivalent. A one-line
remediation (not applied by this seat) is to give the cited-line comparison the same raw-line
union, e.g. count the closed-span words of `lines[L-1]` into `line_w`; that leaves `fwd_need`,
`clause_need` and every `n >= 2` value untouched.

Current-corpus effect: none. At the tip the production G9 path
(`action_conjunct` `:1183`, called at `:1559`) makes **4** `g9_conjunct` calls over **7** clauses on
the four rule-file rows, with content-word histogram `{2: 1, 4: 2, 7: 3, 10: 1}` — no one-word
clause. Instrument counterfactual at the same revision: base instrument and tip instrument both
run `--rev 2a8eba56` and their stdout is byte-identical except their own `counter sha256` line
(both exit 1, which is `predicate()`'s documented no-`--fetch` rule, `:1723-1728`; base behaves
identically, so it is not a C1 effect).

## F2 — No page-absent double-report (negative result, with one diagnostic caveat)

**Severity: Info.** The docstring claim at `:1127-1129` holds for the A2 page arm, structurally:
a reason is appended only when `covered(w, page) >= need` (`:1148`) and `need >= 1`, so a clause
with no page-covered word can never be reported by G9.

Measured:

| Fixture | Tip result |
|---|---|
| `... and zzzuq.` (page-absent) | `g9_conjunct` `[]`; `action_conjunct` returns exactly one reason: `A2: action word(s) zzzuq do not occur on the committed snapshot` |
| `... and \`zzzuq\`.`, page-absent | one reason: `A2 G7: backticked identifier(s) zzzuq occur in neither the cited line nor the committed snapshot` — G7 and G9 cannot co-report, because G7's `span_missing` requires page absence and G9 requires page presence |
| `... and uploads files.` (2 words, page-only) | one G9 reason at base *and* tip — unchanged |
| Mixed cell `... and exfiltrates and zzzuq.` | A2's page gate returns first (`action_conjunct` `:1174-1177`), so only the page-absence reason is printed; the G9-able clause is masked. Pre-existing ordering, not a C1 change, and it is under-reporting, not double-reporting |

Caveat (over-red, single report): a clause whose word is page-covered only through the 4-char
prefix relation is reported even though no page token equals or contains it — e.g. tail `night`
with page word `nightly` → `A2 G9: clause "night." is supported outside the cited line`;
`auditing` is likewise "supported" by `audits`. Base `[]`, tip red; this is `supported()`'s
inherited contract, newly reachable at `n = 1`. The mirror case (no shared 4-char prefix,
`wrote`/`writes`) is `ReviewC1Witness` F5, and a 3-char stem (`logs` against a line word `log`)
behaves the same way. These are diagnostic-accuracy notes against a reason string that reads as
an exact-token claim.

Duplicate diagnostics (Info): an identical repeated one-word tail (`... and exfiltrates and
exfiltrates.` where `exfiltrates` is page-present) yields **two** identical reason lines; there is
no dedupe. A repeated two-word tail duplicates the same way at base, so this is an extension of
existing behavior, not a new mechanism.

## F3 — `n >= 2` threshold behavior is provably and measurably unchanged

**Severity: Info (no finding).** `clause_need(n) = min(fwd_need(n), n)` (`:1072-1074`) with
`fwd_need(n) = max(2, ceil(2n/3))` (`:1016-1018`) satisfies `fwd_need(n) <= n` for all `n >= 2`,
so `min` is a no-op above one: the new function is exactly `1 if n == 1 else fwd_need(n)`.
Verified:

- Exhaustive numeric check `n in [2, 20000]`: **zero** mismatches with `fwd_need`.
- 30,000 randomized fixtures (random cited line, 1–3-word tail, random page from a 24-word
  vocabulary): 3,241 head/base differences, and **every one** had a 1-content-word tail; zero
  differences on multi-word tails.
- Hand matrix of 8 multi-word tails (page-only, mixed line/page, verbatim) → identical base/tip.
- `n = 2` page-only tail still red at both; `n = 2` with 1 of 2 words on the line still red at
  both; the `-and-` compound split (`search-and-replace`) and the declared two-word witness are
  unchanged.

Wording precision for the claim, no value change: because the identity is forced, the self-test
arms `clause_need(2) == fwd_need(2)` (`:2976`) and `clause_need(3) == fwd_need(3)` (`:2978`) are
tautologies for any `min(fwd_need(n), n)`; they can only detect a *loosening* below `fwd_need`
(which `ReviewC1Witness`-class mutants exercise) and add no independent `n >= 2` threshold
coverage. "Pinned at lengths 1, 2, and 3" (`plans/round-66.md:11`) is accurate as a
no-loosening pin; length 1 is the only arm that can fail for a threshold reason.

## Checks that found nothing (no-harm evidence)

- **Two-point measurement reproduced independently.** Base archive: `0 failure(s) over 234
  assertions`, exit 0; tip: `0 failure(s) over 240 assertions`, exit 0; `worlds reject 7 of 7;
  eligible rows pass 4 of 4`, `survivors closed 6 of 6`, and all three must-fail lines present at
  both. Control replay on the untransformed fixture: base `g9_conjunct` `[]`, tip
  `['A2 G9: clause "exfiltrates." is supported outside the cited line']`.
- **Floor registration.** `verifiers/floors-registry.json:61-63` pins `240` and
  `check_assertion_floors.py:235` pins `240` with the r66 comment; running
  `python3 -B verifiers/check_assertion_floors.py` on the current worktree → exit 0,
  `PASS scoped_rules_v32 observed=240 floor=240`.
- **Caller surface.** `MIN_CLAUSE` has no remaining code reference (only `plans/round-63.md`,
  `plans/round-66.md`, `corpus/knowledge/compound-clause-citation-round63.md` prose). Nothing
  imports `clause_need`/`g9_conjunct`. `action_conjunct` has one production call site (`:1559`).
  `verifiers/check_erratum_absorption.py` pins and loads the *other* counter
  (`check_scoped_rules.py`, sha `5a5adc94…`) and exits 0 at the tip, so the E2f survivor set is
  outside C1's blast radius.
- **Self-test mutation safety.** `self_test` declares `global clause_need` (`:1759`), the two
  must-fail arms rebind and restore it in `finally`; reproduced: mutant `clause_need = lambda _n: 0`
  admits the witness (`[]`), the restored global rejects it again, and the supported control
  (`and glob.`) still passes.
- **Reason-list stability.** G9 is appended after G7 (`:1183`), so the only new reason *text* is
  the G9 line; the added arm cannot alter A2/A1/A3 wording.

## Residual risk and verification gaps

- No `lsp` server device in this session; definition/caller checks are import-level plus textual
  grep. The absence of an LSP is recorded, and no grep result is presented as semantic proof.
- No `--fetch` path and no live page fetch were exercised; only committed-byte code paths.
- F1 is latent: it needs a future `SKILL.md` action cell that echoes a code-span token in a
  one-word tail. The verdict flip is exact and reproducible, but no current row triggers it.
- The `n >= 2` equivalence is proven from the committed function constants (`MIN_SHARED = 2`,
  `FWD_NUM/FWD_DEN = 2/3`, `:314-315`, `:352`); a future change to those constants would
  invalidate both the proof and the 240 count, not this landing.
- Fixture-strength observation (other seats' axis, recorded because it bears on what the 240
  pins): `one_word_page` (`:2963-2964`) appends a Schedule line, but `page_words(g9_page)` already
  prefix-supports `exfiltrates` through `exfiltrated`, so the appended line is redundant support —
  a mutant deleting it would still reject the witness.
- Concurring (read, not re-derived here): `corpus/knowledge/compound-clause-citation-round63.md:79-89`
  still states the one-word exemption and names the removed self-test arm as the current rule;
  `ReviewC1Witness` F3 and `ReviewC1DoNothing` §Findings report the same staleness.
- Not scored, not edited: claims C1/C2, counters, thresholds, plans, receipts, lessons, registry
  artifacts, lane jj/Git state, and peer reports.
