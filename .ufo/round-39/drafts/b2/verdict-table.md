# Round-39 per-axis verdict table — seat B2|scribe-shonen

> Measured at dispatch HEAD `1d027f2` (r38 publish), 2026-10-19 ~14:11-14:35Z, this wave.
> Before column = measured now. After column = `[PENDING]` — **no r39 work commit exists**, so no
> `improved` is claimable by this seat on any axis. Every before-cell carries the command that
> produced it.

| Claim | Axis | Measurement | Before (dispatch HEAD `1d027f2`) | After (round 39) |
|---|---|---|---|---|
| C1(a) | depth | laundering counter-probe: genuine `omp.offered.skills` disagreement (IND 5 vs live 7) | **exit 1**, named — `verdict: exit 1 — disagreements: omp.offered.skills (mode=equal: expected 5, observed 7)` | `[PENDING]` |
| C1(a) | depth | same payload **plus** a self-declared `SCOPED_OUT` on that row (both channels) | **exit 0 — `all checks agree, both instruments green`** — the laundering hole is LIVE | `[PENDING]` |
| C1(a) | depth | undeclared deletion of the row (no scope-out declaration) | **exit 2** `uncovered checks (in live, missing from independent): omp.offered.skills` — fail-closed | `[PENDING]` |
| C1(a) | depth | declaration-validation arms (4): scoped-row-hiding-`DERIVED`, empty `scoped_out`, ghost row, empty reason | all **exit 2**, each named (`… but its status is 'DERIVED'…`; `… present but empty…`; `… absent from its own payload…`; `… reason … is empty…`) | `[PENDING]` |
| C1(b) | depth | IND `oc.log.init_count_monotone` predicate on a strictly **increasing** log (no violation exists) | **IND = 1** (wrong; HAR = `[]`) — a constant, not a predicate | `[PENDING]` |
| C1(b) | depth | same on a **decreasing** log | IND = 1, HAR = `['3->2','2->1']` — IND cannot distinguish | `[PENDING]` |
| C1(b) | depth | IND's own self-test asserts 1 where the predicate requires 0 (`verify_harness_independent.py:1000`) | **green** — the self-test certifies the bug | `[PENDING]` |
| C1(b) | depth | `oc.log.init_count_max` adjudication in any r38 artifact (A1 ledger row 3 covers `monotone` only) | **absent** — no ruling; doc §3 files the pair under "Zero-delta representation rows (D5, cosmetic)" while the ledger rules `class: D1 / defect(independent) / settled` | `[PENDING]` |
| C1(c) | depth | doc references A1's ledger | `grep -c 'a1-adjudication-ledger' corpus/knowledge/harness-independent-round37.md` → **0** | `[PENDING]` |
| C1(c) | depth | doc §6 reproduce block verbatim | **runnable head green** (HAR `28/28` exit 0; IND exit 0; self-tests `0/10`, `0/86`; freeze sha `09fb71ca…` == doc's stamp); **6 legs dead** — `.ufo/round-38/drafts/w1/{R1-make_blind_tree.sh,null_echo.py,ind-bad-scope.json,ind-final.json,har-final.json,fixtures/oc-log-mutant.log}` all `No such file or directory` (pruned at r38 close) | `[PENDING]` |
| C1 | depth | comparator headline | **exit 0 — `24/24`, strict `19/24`, `disagree: 0`, `uncovered: 0`, `scoped-out: 4`** (live) | `[PENDING]` |
| C2 | operability | `pins` row **path → None** (well-formed 5-field tuple) on a copy | **exit 1, raw traceback** — `TypeError: unsupported operand type(s) for /: 'PosixPath' and 'NoneType'` at `paths = {name: repo / spec[0] …}` | `[PENDING]` |
| C2 | operability | `pins` row **floor → `(62,)`** (well-formed arity, malformed field) | **exit 2**, but prints the self-contradictory pair: `FAIL registry malformed row: pins (non-integer floor)` **plus** `FAIL registry floor drift: pins registry=62 expected=62 row=(62,)` | `[PENDING]` |
| C2 | operability | `pins` row **floor → `True`** (bool is an `int` subclass) | **exit 2**, contradictory: `floor drift: pins floor=True expected=62` **plus** `floor drift: pins registry=62 expected=62 row=True` | `[PENDING]` |
| C2 | operability | control (unmutated copy, same `--repo`) | **8 × PASS, exit 0** — the mutants are the only difference | `[PENDING]` |
| C3 | freshness | three exploit shapes end-to-end (throwaway git world; cmark 0.31.2 oracle) | **3 silent false-PASS**: `short-closer`, `info-closer`, `closer-trailing-text` → both gates `unindexed=0 rc=0` where cmark renders the row fenced; controls (`control-3backtick`, `control-legal-4`) agree `unindexed=1 rc=1` | `[PENDING]` |
| C3 | freshness | function-level (both instruments imported, cmark oracle) | same three shapes: `cmark=opaque`, `integrity=LIVE`, `independent=LIVE` | `[PENDING]` |
| gates | — | 8-instrument live battery at `1d027f2` | **ALL GREEN** — harness `28/28`; floors `8 × PASS` `10/119/59/87/1597/62/86/83`; checklist `10 × PASS` exit 0; corpus_integrity `9/9`; corpus_independent exit 0; surfaces `7 × PASS`; pins `OK 3/3`; fault `self-test: OK`. The r38 report's "5/8 green" state is resolved in committed bytes | `[PENDING]` |
| gates | — | all nine `--self-test` runs | `0 failure(s) over 10 / 68 / 1597 / 119 / 59 / 87 / 62 / 86 / 83`, all rc=0 | `[PENDING]` |

Axis verdicts (scribe's recommendation; the landing-commit re-run is the authority):

- **depth (C1) — `[PENDING]`; the before-state is materially worse than the r38 report's summary.**
  The laundering hole reproduces exactly (arm 2 → exit 0 over a real disagreement), the
  declaration-validation machinery is genuinely fail-closed (4/4 arms exit 2, named), the predicate
  defect is a **constant** on both an increasing and a decreasing log (not merely a wrong constant),
  and the doc/ledger divergence is live in both directions (no reference; contradictory class).
  With (a) a machine-checkable discriminator, (b) the predicate fix + the `init_count_max` ruling,
  and (c) the doc reconciliation, the exit 0 becomes earned. Not claimable by this seat.
- **operability (C2) — `[PENDING]`.** All three V4 arms reproduce on copies; the guard's control is
  green, so the arms are true discriminators of the defect, not of the harness. The `None`-path crash
  is a **raw exit 1 with an unnamed class** — the same shape the r38 C2 patch was meant to close one
  site over.
- **freshness (C3) — `[PENDING]`.** The three-shape exploit is proven end-to-end by this seat's own
  probe, with cmark as oracle and both controls agreeing. Zero live corpus incidence (V6b's F6) means
  the fix is debt-closing, not a live break.
- **consistency / coverage / calibration / adjacency — held** on the evidence measured, with one
  exception: **calibration carries the doc/ledger contradiction** (C1(c) rows above) — two committed
  artifacts make opposite claims about the same row's class, and the doc's §6 cannot be reproduced as
  written.
- **SHONEN — 4 × `[~]`, no `[x]`**; block at `drafts/b2/shonen-section.md`.
