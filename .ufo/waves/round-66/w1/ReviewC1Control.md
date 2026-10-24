# ReviewC1Control — C1 cited-line control, one-word tails (round 66 w1)

**Seat:** reviewer (read-only; no production edit, no subagent dispatch). **Lane:** kotoba only.
**Pinned base:** `11385e04e368c1e94ab1a5a89d7439033eb1f855`.
**Measured tip:** Git `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. Verifier bytes identical at `806b53b4`, `fc1b71e5` and `2a8eba56`: `sha256 97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def`; at the pinned base the same path is `b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d`. Measured tip ≠ pinned base is the intended reading; no receipt or claim file was touched.
**Method:** direct probes of `g9_conjunct`/`action_conjunct` imported from the lane bytes plus mutant runs on full copies of `verifiers/` under `/tmp` (`python3 -B <copy>/verifiers/check_scoped_rules_v32.py --self-test`; the sibling `check_erratum_absorption.py` load requires a directory copy, otherwise the run aborts before the suite). The lane tree was never written; `git status --porcelain verifiers/` was empty throughout.

## Verdict

The frozen C1 predicate reproduces exactly, and the specific witness it names is closed. But the answer to the assignment's question — *does the frozen self-test prove the in-line, repeated and backticked one-word forms remain accepted without weakening the off-line witness* — is **partially**:

- **Pinned:** the plain in-line tail is accepted (`:2969`), the plain off-line tail is rejected (`:2966`), and the floor is pinned at lengths 1/2/3 (`:2974`/`:2976`/`:2978`) with two must-fail arms (`:2987`/`:2995`).
- **Unpinned:** repeated-token and backticked one-word forms appear in **no** assertion. One of them is not merely untested but silently reopenable: an extra mutant (M9) stays green at 240 while admitting `` and `exfiltrates` `` (see M3 below).
- **Accepted without the cited line:** three concrete escapes pass the full `action_conjunct` at the tip — a comma/bare/colon joiner (H1), a joiner hidden inside a closed backtick span (H2), and a 4-character-prefix neighbour of a cited-line word (M1). H1 and M1 are documented r63 limits; **H2 is not in the entry's limits list**.
- **New over-rejection:** a one-word tail whose word *is* in the cited line but only inside a backticked span is accepted at base and rejected at the tip (M2) — the plan's "a one-word tail supported by the cited line remains accepted" does not hold for that form, and no assertion pins either direction.

None of H1/H2/M1 contradicts the frozen predicate, which is literally the `and exfiltrates.` witness. They bound what the round's depth move closed. The LOG (`LOG.md:2627`, "closes the one-word case") and the non-author spot-check ("a one-word clause on the page but off the cited line is now rejected") are joiner-blind as written.

## Frozen predicate reproduction (independent)

| Item | Pinned base `11385e0` | Measured tip `2a8eba5` |
|---|---|---|
| instrument sha256 | `b6cfc764…2183e8d` | `97d897…bed26def` (also at `806b53b4`, `fc1b71e5`) |
| `--self-test` | `0 failure(s) over 234 assertions`, exit 0 | `0 failure(s) over 240 assertions`, exit 0 |
| frozen lines | 7/7, 4/4, 6/6, three must-fail `yes` | identical |
| control witness `g9_conjunct([line], line[:-1]+" and exfiltrates.", 1, page)` | `[]` (admitted) | `['A2 G9: clause "exfiltrates." is supported outside the cited line']` |
| floors registry | — | `"scoped_rules_v32": {"floor": 240}` |

Assertion-set delta (static diff of `check("…")` names, base→tip): **one removed**, `A2 G9: a ONE-word clause is exempt (declared bound)`; **seven added** at `:2966`, `:2969`, `:2974`, `:2976`, `:2978`, `:2987`, `:2995`; net +6 = 234→240. The named exemption arm no longer exists, matching the plan's "former one-word exemption becomes a must-fail witness".

Kill receipt re-derived on the tip bytes (full-directory copies): K1 uncoupled `clause_need` → exit 1, 2 failures; K2 reinserted `<2` skip → exit 1, 1 failure; K3 page floor `fwd_need` → exit 1, 1; K4 line floor `fwd_need` → exit 1, 2; K5 zero floor → exit 1, 20. **All five fail as claimed**; see L2 for the one attribution inaccuracy.

## Attack matrix (tip bytes unless noted; control fixture `line = "The index stores project rules."`, page = line + `## Schedule / The agent secretly exfiltrates telemetry.`)

| Probe (cell = line + …) | Base | Tip | `action_conjunct` at tip |
|---|---|---|---|
| ` and index.` (token in cited line) | accepted | accepted | `[]` |
| ` and INDEX.` (case) | accepted | accepted | `[]` |
| ` and index index.` (repeated, in-line) | accepted | accepted | `[]` |
| ` and exfiltrates exfiltrates.` (repeated, off-line) | `[]` | **rejected** | G9 |
| ` and exfiltrates exfiltrates exfiltrates.` | `[]` | **rejected** | G9 |
| ` and `exfiltrates`.` (backticked, off-line) | `[]` | **rejected** | G9 |
| ` and `index`.` (backticked, in-line) | accepted | accepted | `[]` |
| ` and `index index`.` (backticked, repeated) | accepted | accepted | `[]` |
| `, exfiltrates.` (comma joiner) | **accepted** | **accepted** | **`[]`** |
| ` exfiltrates.` (bare juxtaposition) | **accepted** | **accepted** | **`[]`** |
| `: exfiltrates.` (colon) | **accepted** | **accepted** | **`[]`** |
| ` and rulers.` (line `rules`, page `ruled`) | accepted | **accepted** | **`[]`** |
| ` and global.` (line `glob`) | accepted | **accepted** | **`[]`** |
| ` and `quotas`.` (page `quotas`, line `quota`) | accepted | **accepted** | **`[]`** |
| `` `and exfiltrates`. `` (joiner inside backticks) | **accepted** | **accepted** | **`[]`** |
| `` `and secretly exfiltrates`. `` | **accepted** | **accepted** | **`[]`** |
| `` `and secretly exfiltrates telemetry`. `` | rejected | rejected | G9 |
| ` and zephyr.` (page-absent) | rejected | rejected | A2 page arm |
| ` and now.` (3 letters) | accepted | accepted | `[]` (invisible to `[a-z]{4,}`) |

Repeated tokens cannot weaken the floor: `page_words` returns a **set** (`:1026-1033`) and `covered` iterates the clause set (`:1042-1043`), so duplication inflates need and coverage together. Repetition is correct-but-unpinned (L1).

## Findings

### H1 — High (depth residual; predicate not violated): the one-word floor is joiner-scoped — comma, colon and bare juxtaposition still pass
`split_clauses` (`verifiers/check_scoped_rules_v32.py:1077-1123`) splits only on `;` and the word `and` (`CLAUSE_AND_RE`, `:1071`). A one-word purpose tail appended with any other joiner is never a separate clause, and A2's forward floor tolerates exactly one unsupported word for any line with ≥3 content words (`fwd_need(n)=max(2,ceil(2n/3))` ≤ n−1 for n≥3). Because the tail word is on the page, page containment passes too:

```
cell = "The index stores project rules, exfiltrates. (S900 :1)"
tip  action_conjunct → []            (also: bare "… rules exfiltrates.", colon "… rules: exfiltrates.")
base action_conjunct → []
```

This is a declared r63 bound ("Other joiners (`but`, `while`, commas, participles) … are still not modelled", `corpus/knowledge/compound-clause-citation-round63.md:102-104`), so it is not a claim violation. It is the reason the closure summaries should say "the `and`/`;`-joined one-word tail" rather than "a one-word clause".

### H2 — High (undocumented class door, base and tip): a closed backtick span suppresses the joiner and hides a page-supported tail
`split_clauses` masks closed `BACKTICK_RE` spans, so an `and`/`;` inside backticks is not a boundary. The merged clause includes the tail's words via `page_words` (backticks included), so it clears its own forward floor against the cited line as long as the tail is not too long:

```
cell = "The index stores project rules `and exfiltrates`. (S900 :1)"
split_clauses → ['The index stores project rules `and exfiltrates`. (S900 :1)']   # no split
w = 5 words, need 4, covered(line) = 4  →  G9 returns []
tip action_conjunct → []        base action_conjunct → []
two-word hidden tail `and secretly exfiltrates` → [] ; three-word → G9 rejects
```

The bound is structural: with `n_host` line-portion words and `t` hidden tail words, the clause passes while `ceil(2(n_host+t)/3) ≤ n_host`, i.e. roughly `t ≤ n_host/2` (measured 1–2 words on the 4-word control line). A page-absent hidden tail is caught only by G7's span arm — i.e. the surviving form is exactly G9's class definition (page-supported, line-unsupported). The r63 entry documents that backticked spans are opaque and that *double* quotes do not protect (`:93-104`) but does **not** list "a page-supported purpose tail can be hidden inside a backticked span" among its limits. Closing it would require splitting quoted `and` (contradicting the deliberate opacity pinned by the `;`-in-backticks arm at `:2898`) or a new merged-clause check — a v33 contract change, not a repair.

### M1 — Medium (documented inheritance): "supported by the cited line" is 4-character-prefix support, not word support
`supported()` (`:1035-1039`, `SUPPORT_PREFIX = 4` at `:354`) matches the same word or a shared first four characters, in both directions (line floor `:1146` and page floor `:1148`):

```
cell = "The index stores project rules and rulers. (S900 :1)"
page = line + "## Schedule\nThe court ruled on global telemetry export."
tip action_conjunct → []        # page carries only "ruled"; "rulers" occurs nowhere verbatim
cell = "The configuration stores project rules using glob syntax and global. (S900 :1)" → []
backticked "and `quotas`." with page "quotas", line "quota" → []
```

Strictly, a one-word tail can clear the new floor while its word occurs neither in the cited line nor on the page as written. This is A2's existing contract and is declared at `compound-clause-citation-round63.md:103-105`; the mutant M2 (exact-match `supported`) fails three pre-existing A2/G7 arms, so it is not a locally fixable defect. It does mean the C1 predicate's phrase "supported by the cited line" must be read as prefix-4 support.

### M2 — Medium (new over-rejection; no predicate wording covers it): a cited-line word inside a backticked span no longer counts as line support
`g9_conjunct` computes `line_w = content_words(lines[L-1])` (`:1132`), which strips backticked spans (`content_words`, `:1008-1013`), while the clause side uses `page_words`, which keeps them. Before r66 a one-word clause was skipped, so this asymmetry never fired on a one-word tail; now it does:

```
line = "The tool writes mode quota limits `oversight` nightly."   (line_w: 6 words, "oversight" excluded)
page = line + "\n\n## Appendix\nThe audit log is retained."
cell = line[:-1] + " and oversight. (S900 :1)"      # "oversight" IS in the cited line, as a backticked identifier
base: g9 [] / action_conjunct []                    # one-word clause skipped
tip : g9 ['A2 G9: clause "oversight. (S900 :1)" is supported outside the cited line'] / action_conjunct rejects
same with a backticked tail `and \`oversight\`.`    # also rejected at tip, accepted at base
```

The header clause is clean in this fixture, so the rejection is attributable solely to the one-word tail. This is a behavior change on a form the plan's predicate says "remains accepted", and neither form is pinned by the suite (a regression to the old skip would stay green — see M3). Whether it is a defect depends on whether "cited line" means the raw line or its content words; the asymmetry itself is worth a line in the entry either way.

### M3 — Medium (pinning gap): the self-test does not prove the backticked one-word witness stays rejected
Extra mutant M9 (one line, in the copy): `w = content_words(clause) if len(page_words(clause)) == 1 else page_words(clause)` — i.e. measure single-word clauses with the backtick-stripping function only.

```
$ python3 -B <M9>/verifiers/check_scoped_rules_v32.py --self-test
self-test: 0 failure(s) over 240 assertions        exit=0
M9  action_conjunct("… and `exfiltrates`.") → []    # witness admitted
tip action_conjunct(same cell)              → G9 rejects
plain unbackticked witness under M9         → still G9-rejected
```

The suite catches the *class-wide* strip (M1-style `w = content_words(clause)` fails `A2 G9: a backticked fabrication is counted and rejected`, the 3-word span arm) but not a single-word-scoped strip. So "does the frozen self-test prove [the backticked form] remains accepted without weakening the off-line witness?" — for the backticked form the answer is no: the landed behavior is correct, the frozen suite does not defend it.

### L1 — Low: repeated-token forms are correct but unpinned
No assertion contains a repeated token. Behavior is right on the tip bytes (in-line repeated accepted, off-line repeated rejected at 2× and 3×), and repetition cannot weaken the set/iterator arithmetic. A future list-based rewrite would change `len(w)` and `need` together, so the form is not a live hole — it is simply unasserted.

### L2 — Low: C1-kill receipt K5 attribution ordering
`receipts/C1-kill.txt` attributes K5 to `FAIL A2 G9: a ONE-word off-citation clause is rejected…`. On the tip bytes K5 (zero floor) exits 1 with **20** failures and the first FAIL line is `A2 G9: an `and`-joined purpose clause off the cited line is rejected`; K1 trips 2 and K4 trips 2, K2/K3 trip 1 each. The receipt's "all five failed" is true and its "secondary arms" caveat covers K1/K4, but the "first load-bearing" claim does not hold for K5. This matches the independent observation in `ExecC1Selftest.md` §7 and `ReviewC1DoNothing.md` §5.

### L3 — Low: the committed knowledge rule now contradicts the instrument, with no dated correction
`corpus/knowledge/compound-clause-citation-round63.md` is untouched by `11385e0..HEAD` (verified via `git log`) and still states as current rule: clauses need `MIN_CLAUSE = 2` content words (`:32-35`); "Short clauses are exempt … the one-word tail … is a declared structural bound … closing it would require touching A2's own forward-fraction floor — a v33 move, pinned by the self-test arm 'a ONE-word clause is exempt'" (`:79-87`). All three claims are now false of the instrument (the arm was deleted; the bound was reachable with a clause-local `min`, without touching `fwd_need`). The lane's own appended-notice practice (`:53-58`) and the r64 freshness-note precedent call for a dated correction. Already reported as a Medium finding by `ReviewC1DoNothing.md`; recorded here as confirming evidence, since it is the entry that supplies the residual-limits list this review relies on.

## Residual risk

- The frozen C1 predicate is **satisfied**: the exact witness is rejected at the tip, the exact supported arm passes, the floor pins and both must-fail arms hold, and 234→240 is a genuine +7/−1 assertion change, not padding. No score claim is contradicted by these findings.
- The depth improvement is real but narrow: it applies to unbackticked, `;`/`and`-split, non-prefix-relative one-word tails. H1/H2/M1 are class doors that remain; H2 is undocumented and admits the same page-supported/line-unsupported class the guard exists for, up to ~half the host clause length.
- The 240 count alone is not self-authenticating (reported independently by `CriticDoNothingTarget.md`); the frozen predicate's retention clauses are what bind it.
- The `MIN_CLAUSE`-era knowledge entry is the only committed text that now describes the wrong contract; a future reader following it would test the wrong behavior.

## Verification gaps

- All probes are function-level on synthetic fixtures using the control's page; no real snapshot/corpus row was driven through the row checker. `action_conjunct` is, however, the exact function the row checker calls (`:1559`), and the fixtures append a valid `(S900 :1)` citation.
- No `--fetch`/live-page arms exercised; the live worlds report `live not run` at both revisions (consistent with peers).
- Mutants ran on copies of `verifiers/`, not the lane; a self-test run from a bare copy aborts on the sibling `check_erratum_absorption.py` import, so results above always used a directory copy (identity copy verified green at 240 first).
- The lane working tree was dirty with peers' `w1/*.md` files and `.ufo/waves/round-66/w1/swarm-registry.json`; no tracked verifier/receipt/control byte differed. The jj working copy moved during the wave; every measurement is keyed to Git `2a8eba5` plus the verifier sha256, not to a jj id.
- Overlap: K7 (4-word floor unpinned), `and stored.` prefix acceptance, and the 3-letter vocabulary bound were independently found by `ExecC1Selftest.md` §8–§9; the `MIN_CLAUSE` entry and K5 ordering by `ReviewC1DoNothing.md`. H1, H2, M2, M3 and the repeated-token matrix are not reported by any w1 seat read at review time.
- **Tooling:** nothing installed or upgraded; no package-manager transaction was run.
