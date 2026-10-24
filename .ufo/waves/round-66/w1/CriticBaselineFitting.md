# CriticBaselineFitting — round-66 w1 falsification of the D2 re-pin

**Scope:** attack `verifiers/check_r66_routed_repairs.py` (frozen bytes, sha256 `3129c0d7…3141`, self-test `0 failure(s) over 14 assertions`) — can a bad baseline, an omitted index row, or a hidden defect still print `r66 routed defects closed 2 of 2`, exit 0?
**Base:** `11385e04e368c1e94ab1a5a89d7439033eb1f855` (pinned control, scores 0 of 2 — confirmed).
**Anchor tip:** `fc1b71e56fda86fefe672f2cae90a62318d34449` (receipt tip; real gate 9/9 there — mutants are carved from it so gate redness attributes to my change only).
**Sandbox:** `/tmp/r66-falsify`, `git clone --no-hardlinks` of the lane; all worlds are real commits there. Lane repo untouched. Verifier recipe per world: `git archive <rev> | tar -x -C /tmp/wtree`, then `python3 -B verifiers/verify_corpus_integrity.py --repo /tmp/r66-falsify` from the extracted tree.

## Headline survivor (no mutation needed)

At the unmutated lane tip `2a8eba56b3f9321b70c569fa2816d42237ca49a2` the counter prints `2 of 2`, exit 0, while the real gate prints `5/9 checks pass`, exit 1 — DRIFT on `tracked_files 119≠118`, `unindexed 1≠0` (`corpus/lessons/round-66-verifier-spotcheck.md`), `report_total 82≠79`, `commit_total 38≠37`. The counter certifies `fc1b71e`-era claim bytes at a measurably different tree. (Independently reported by `ExecRoutedCounter`; my run reproduces it.)

## Root cause

`check_d2` never executes anything and never compares a blob to the tree. It is three substring/equality tests over committed bytes: `path in readme` for the four spotcheck names, `checks.<key>.expect == <frozen int>` for seven keys, `EXPECTED_NOTE in notes`, and four source-text tokens in `verify_corpus_integrity.py`. Every arm can be satisfied by bytes that lie about the tree.

## Survivor table (counter `2 of 2` / exit 0 everywhere)

| World | Rev (sandbox) | Mutation over fc1b71e | Counter | Real gate on that tree |
|---|---|---|---|---|
| w0 live tip | `2a8eba5` | none — actual lane state | 2/2 exit 0 | 5/9 exit 1 |
| w1 stale claims | `27b7c71e` | +`corpus/knowledge/rogue-unindexed.md` (tracked, unindexed); baseline/README kept | 2/2 | 7/9 exit 1 (tracked 119, unindexed 1) |
| w2a prose rows | `b04b16e0` | all four FILE-column rows deleted; same four strings in a basis/prose cell | 2/2 | 8/9 exit 1 (unindexed 4) |
| w3 fenced rows | `c288f718` | four rows deleted; strings inside a ```` ```text ```` fence | 2/2 | 8/9 exit 1 (unindexed 4) |
| w2c files gone | `60833c4a` | w2a + `git rm` all four spotcheck files entirely | 2/2 | 6/9 exit 1 (114≠118, plus pointer drifts) |
| w4 stub script | `8f8ea3bb` | `verify_corpus_integrity.py` → 10-line stub carrying all four tokens + `sys.exit(0)`; hidden unindexed file added | 2/2 | stub prints `9/9`, exit 0; real script on same tree: 7/9 exit 1 |
| w4b gutted resolver | `ee5650e3` | real script, body of `commit_resolves` → `return False`; all tokens retained | 2/2 | 8/9 exit 1 (`commit_unresolvable 37`) |
| w5a/b/c notes containers | `61a7ef8b` / `9b4387a6` / `7b675d94` | `notes` = bare string `"…round66_rerecord…"` / list `["round66_rerecord"]` / `{"round66_rerecord": null}` | 2/2 each | — (claim-text forgery; the "measured re-record" reduces to key/substring presence) |
| w6 forged provenance | `9e9d4814` | `measured_against.head` all-zeros, `as_of` year 2031, every `mode` flipped to `zero`, note says "fitted" | 2/2 | 9/9 exit 0 — both instruments blind |
| w7 forged registries | `2cde408f` | D1 blobs → `{"seats": [], "wave": "kotoba-r00-w9"}` and `{"x": 1}` | 2/2 | — (any nonempty JSON dict passes `tracked_nonempty_json`) |
| w8 no lineage | `15f1e5c7` | orphan commit (0 parents, `%P` empty), vandalized tree, stub integrity | 2/2 | — (no `is-ancestor` / lineage check on `--rev`) |

## Boundary / non-survivors (informative kills)

- **w9 honest-future kill** (`0456f884`): add an indexed file + row, re-record `tracked_files 119` truthfully → gate 9/9 exit 0 but counter `1 of 2` exit 1. The pin cannot distinguish *reconciled* from *carries the r66 constants*; a strictly better world fails. Same pin fragility as `ExecRoutedCounter`'s `expect=119` kill.
- Baseline `mode` fields are dead bytes for both instruments (verdict modes come from the script's own `CHECKS` table); deleting zero-mode keys (`stale_patterns`, `missing_paths`) or planting contradictory `observed` fields next to `expect` is invisible — inert, not a survivor.
- `EXPECTED_NOTE in notes` on a dict is exact-key membership (a `round66_rerecord_x` key fails) — precise; the hole is container-type blindness and ignored values.
- `tracked_nonempty_json` correctly kills `{}` (peer-confirmed) and non-dict JSON.
- Counter self-modification (e.g. re-pinning `EXPECTED_COUNTS`) is outside its own view; the `C2-counter-selftest.txt` sha pin is the only guard — a meta-control, not the counter.

## Impacted axes

- **Calibration (primary):** the counter measures claim text, not corpus state; it passed every lie that preserves the seven numbers and four substrings, and already passes at a live tip where the gate is red.
- **Consistency (D2 arm):** "all four lessons indexed" is falsifiable by text placement alone; "commits resolve lane→fleet" is satisfiable by a stub or a gutted function.
- **Depth (minor):** the counter's own check depth is lexical; nothing in the counted predicate reaches behavior.

## Smallest safe corrections (fixable defects — none require widening the claim)

1. Replace the `checks.*.expect` match with a measurement: extract `<rev>`'s tree (archive/`git ls-tree`) and run the integrity script there, or minimally verify `tracked_files` directly — it is a tree property: `git ls-tree -r <rev> corpus --name-only | wc -l` must equal the pinned 118 (kills w0/w1/w2c/w9-class drift without executing code).
2. For each `lessons/round-6N-verifier-spotcheck.md`: require it inside a coverage-map FILE-column cell (or at least backticked at a table cell boundary) **and** `git cat-file -e <rev>:corpus/lessons/round-6N-verifier-spotcheck.md` — kills w2a/w3/w2c.
3. `git merge-base --is-ancestor BASE_REV <rev>` before scoring — kills w8.
4. `notes` must be a dict with a non-empty string value for `round66_rerecord` — kills w5a/b/c; D1 blobs must carry a non-empty `members` object (schema pin) — kills w7.
5. Token checks for the hop should at least require the markers *outside* comments/strings of a self-test-less script — or execute `verify_corpus_integrity.py --self-test` and `--repo` on the rev tree, which kills w4/w4b outright (the stub has no self-test; the gutted resolver's own suite goes red).

Items 1–3 close the live divergence at tip `2a8eba5`; until then `2 of 2` certifies a snapshot, not a state. This report records counterexamples only — admission judgment belongs to the canonical seat.

**Tooling:** none installed (host pacman pause respected); system `git` + `python3` only. Sandbox `/tmp/r66-falsify` retained for rev verification; all mutant revs reproducible from the one-line recipes above.
