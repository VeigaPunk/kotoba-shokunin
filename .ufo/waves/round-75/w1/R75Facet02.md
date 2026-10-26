# R75Facet02 — facet 2: the threshold-disagreement paragraph in the skill-eval entry

Seat: `R75Facet02` (leaf, read-only, no delegation). Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe`
(`git rev-parse HEAD`); every cited path is clean against that commit (`git status --porcelain -- <paths>` printed
nothing, exit 0), so working-tree bytes = committed bytes. No scratch directory was created; nothing was written
outside this report.

## Facet under audit

| element | location |
|---|---|
| paragraph | `corpus/knowledge/skill-eval-artefacts-round70.md:56-72` (§ The one disagreement, and the action it implies) |
| its propagated rule | `SKILL.md:193` (bullet *Testing a skill — the Agent Skills guides' artefacts*) |
| evidence it rests on | F7/F8 rows at `corpus/knowledge/skill-eval-artefacts-round70.md:24-25` (fact table), source line 4 |
| snapshots read | `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md` (196 lines, sha256 `7cc54fbb…`), `…/S211-run_eval.py.txt` (sha256 `43e3b8f8…`) |

The paragraph asserts six things: (i) the guide passes a should-trigger query strictly *above* the threshold
(`:58`); (ii) `run_eval.py` passes it at `>=`, and a should-not-trigger query only at `<`, "matching the guide's
below" (`:59-60`); (iii) at equality the two disagree on should-trigger queries only (`:60-61`); (iv) the default
(3 runs, 0.5) never reaches the gap for a query listed once (`:62-64`); (v) an even run count opens it, and two
limits widen it — per-query-string division and non-default thresholds (`:64-70`); (vi) every disagreement runs
one way, `run_eval.py` passes and the wording fails (`:70`), with an action (`:71-72`).

## What holds — observed, each re-read from bytes

| claim | evidence | verdict |
|---|---|---|
| F7 quote is verbatim on the guide | `S210-optimizing-descriptions.md:92` — `A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default). A should-not-trigger query passes if its trigger rate is below that threshold.` | exact match for the first sentence; the second (should-not) sentence is **not** in any fact row |
| `run_eval.py` comparator | `S211-run_eval.py.txt:232` `did_pass = trigger_rate >= trigger_threshold`; `:234` `did_pass = trigger_rate < trigger_threshold` | confirmed, both branches |
| "lines 230–234" citation | `:230` `should_trigger = item["should_trigger"]`, `:231` `if should_trigger:`, `:232`, `:233` `else:`, `:234` | accurate branch region |
| "default 3 runs … line 266" | `:266` `--runs-per-query … default=3`; `:267` `--trigger-threshold … default=0.5` | accurate |
| "divides by the runs it collected per query string (lines 213–229)" | `:213` `query_triggers: dict[str, list[bool]] = {}`, `:215` `for future in as_completed(...)`, `:222`/`:225` append result or `False`, `:229` `trigger_rate = sum(triggers) / len(triggers)` | accurate; count is `len(triggers)` per query *string* |
| 3 runs at 0.5 gives {0, 1/3, 2/3, 1} | enumeration below | correct |
| every even run count hits 0.5 | n=2 k=1, n=4 k=2, n=6 k=3, n=8 k=4 | correct |
| "threshold × runs is a whole number" is the disagreement set | enumeration below, t ∈ {0.5, 1/3, 2/3, 0.25, 0} | correct, including the degenerate t=0 case |
| one direction only | at `rate == t`: `>=` True, `>` False; at `rate < t` both fail; at `rate > t` both pass | correct |
| duplicate listing at default → 6 runs, 3/6 = 0.5 | `:201` iterates `range(runs_per_query)` per list entry; `:213` dict keyed on the query string | correct |

Enumeration actually run (`python3 -`, no files written):

```
t=0.5 n*t=[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
   disagree at ['n=2:k=[1]', 'n=4:k=[2]', 'n=6:k=[3]', 'n=8:k=[4]']
t=1/3 n*t=[0.3333, 0.6667, 1.0, 1.3333, 1.6667, 2.0, 2.3333, 2.6667]
   disagree at ['n=3:k=[1]', 'n=6:k=[2]']
t=2/3 n*t=[0.6667, 1.3333, 2.0, 2.6667, 3.3333, 4.0, 4.6667, 5.3333]
   disagree at ['n=3:k=[2]', 'n=6:k=[4]']
t=0.25 n*t=[0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
   disagree at ['n=4:k=[1]', 'n=8:k=[2]']
t=0.0 n*t=[0.0, …]  disagree at ['n=1:k=[0]', …, 'n=8:k=[0]']
```

No factual error was found in the paragraph's arithmetic or its line citations. The exposure is elsewhere.

## Finding F1 — the disagreement is an inference from English, printed in the register of a counted fact (calibration)

Observation. The paragraph opens directly under a table whose eight rows are counted by
`verifiers/check_skill_evals.py`; it then states "The guide says … **above** … skill-creator's `run_eval.py`
passes it at **`>=`** … so at a rate equal to the threshold the two disagree". That conclusion needs the page to
mean strict `>`. The page never says so.

Measured sweep for a stated comparator on the guide's snapshot:

```
grep -nEi 'strictly|more than|at or above|>=|equal to|exceed|meets|at least|beyond' \
  .ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md
→ only line 19 ("…capabilities beyond what they can handle alone"), unrelated to the threshold
```

`grep -n 'threshold' …S210…` prints exactly one line, `:92`, whose wording is "above a threshold" and "below that
threshold" — the equality case is never addressed, and the page's own example (20 queries × 3 runs, `:94`) cannot
distinguish `>` from `>=`. So "the two disagree" is a reading of colloquial prose, not a located rule; `SKILL.md:193`
then hands the executing agent the same reading as instruction ("the guide passes a should-trigger query only
*above* the threshold").

Inference (labelled). A reader who parses "above" as "meets or exceeds" — a normal reading of a sentence that
offers 0.5 as a default for a 3-run rate — gets no disagreement at all, and the paragraph's headline is then
false. Nothing in the lane turns red in that world.

Why this is a calibration finding rather than a defect: Q23 asks a rule attributed to an authority to carry a
located quote; the quote is located (F7) but does not decide the comparator, and no counter measures the inference
(Q26/Q31 bind counter descriptions and headlines, and the entry's headline does not assert the disagreement). The
paragraph is therefore true-under-an-unstated-reading, printed as if settled.

## Finding F2 — the should-not half of the claim is pinned nowhere (control weakness)

Observation. The paragraph's clause "while it passes a should-not-trigger query only at `rate < threshold`,
matching the guide's below" (`:59-60`) has two anchors:

- guide side: `S210-optimizing-descriptions.md:92`, **second sentence** — absent from the F7 quote
  (`…round70.md:24`, which stops at "(0.5 is a reasonable default).");
- code side: `S211-run_eval.py.txt:234` `did_pass = trigger_rate < trigger_threshold` — absent from both counters'
  pinned quotes. `verifiers/check_skill_evals.py:208` pins
  `"        if should_trigger:\n            did_pass = trigger_rate >= trigger_threshold\n"`; `check_skill_evals_v2.py:345`
  pins the same two lines; the `SNAP_TEXT` self-test fixtures (`check_skill_evals.py:198-208`,
  `check_skill_evals_v2.py:344-359`) likewise stop before the `else:` branch.

Consequence: if the guide reworded its second sentence, or upstream changed `:234` to `<=`, every counter still
exits 0 and the paragraph would silently state a false agreement (a `<=` there would make the two agree at
equality on should-not queries — the paragraph's "only" and "matching" clauses both become wrong). The snapshot
sha256 pin catches tampering with the *committed* snapshot, not a page or upstream change the `--fetch` path is
meant to catch, because the fetch only checks pinned quotes.

## Finding F3 — a duplicate-listing consequence the paragraph does not name (scope, low)

Inference from code reading (not executed — running `run_eval.py` calls `claude -p`, which is a model experiment
and out of this seat's bounds):

- `:201` submits `runs_per_query` futures per **list entry**, so a duplicated query string yields 6 futures at the
  default; `:213-225` accumulates them into one list keyed on the string;
- `:218` `query_items[query] = item` is unconditional inside the `as_completed` loop (`:215`), so with two entries
  carrying different `should_trigger` labels the reported label at `:237` depends on completion order — the score
  direction flips run to run;
- `:240` `"runs": len(triggers)` reports 6, and `:232`/`:234` score over 6.

The paragraph's "de-duplicate query strings" advice cures all three, so the action stands; but the observable that
exposes a duplicate (`runs` ≠ `runs_per_query`) is not named, and the label nondeterminism is a harder failure
than the rate inflation the paragraph describes.

## Finding F4 — readability nit that matters to a description audit (scope, low)

`:64-66` reads "It opens with an **even** run count: at 2 or 4 runs …" after `:62-64` has just fixed the default at
3 runs. The gap does not open by itself: 2 and 4 require a non-default `--runs-per-query`, and the guide's own
example uses 3. The parenthetical "(every even run count, not only 2 and 4)" is correct; the opening clause is
not self-bounded. Adjacent, outside this facet: the entry header's `recheck:` (`:7`) names
`verifiers/check_skill_evals.py` (8 facts) while the registered successor `check_skill_evals_v2.py` carries 10 —
a reader following the recheck runs the weaker counter.

## Concrete checks / controls (each cheap, none run here)

1. **C-a comparator sweep arm** (closes F1). Add to the eval counter (v2 or a successor): the S213/S210 snapshot
   must contain no equality wording in the threshold paragraph; the predicate is
   `grep -nEi 'at or above|or above|>=|at least|equal to|no less than' <snapshot>` returning no hit in the
   `:88-95` window, else exit 2 with "re-open: the guide now settles the equality case". Self-test arms: a fixture
   whose paragraph gains "at or above" must read exit 2; today's snapshot must read exit 0.
2. **C-b pin the should-not branch** (closes F2). Extend the S211 pinned quote to
   `"        if should_trigger:\n            did_pass = trigger_rate >= trigger_threshold\n        else:\n            did_pass = trigger_rate < trigger_threshold\n"`,
   and add the second sentence of `S210:92` as the S213 side of the same row; mutant: on a scratch copy, rewrite
   `:234` to `<=` and require the row to fail, and remove the `else:` bracket and require the same. (Snapshot
   hashing alone does not substitute: the point is that a *live page* change must reach a verdict.)
3. **C-c freeze the arithmetic** (makes F1's inference recomputable). Ship the enumeration above as a self-test
   table in the counter: for `t ∈ {0.5, 1/3, 2/3, 0.25, 0}` and `n ∈ 1..8`, assert the disagreement set equals
   `{(n,k) : k/n == t}`. Red on any `>=`→`>` claim inversion. This converts prose into a counter and lets the
   paragraph cite it (Q25).
4. **C-d duplicate observable** (closes F3). Assert in any report that cites a trigger score:
   `runs == runs_per_query` for every result row (`:240`), and that query strings are unique in the eval set
   (`len({q}) == len(eval_set)`). Both are one-line checks over the eval set and its output JSON.

Wording for the description audit (if the paragraph is revised): move "the two disagree" behind an explicit marker —
"the guide's prose does not settle the equality case (no comparator wording anywhere on S213's 196-line snapshot;
`run_eval.py:232` settles it at `>=`); on the strict reading the two disagree at equality, and `SKILL.md`'s
non-integral-product rule holds under either reading" — and keep the action sentence unchanged, since it is
correct under both readings.

## Risks and limits

- I did not run `run_eval.py` (needs `claude -p`; model experiments are out of bounds), so F3 is code-reading
  inference, and every `>=`/`>` result above is arithmetic on the pinned source, not a measured run.
- The live pages were not fetched (no live fetch this round); all quotes are from the committed round-70 snapshots
  whose sha256 prefixes match the entry (`7cc54fbb…`, `43e3b8f8…`). A page that has since added a comparator is
  exactly what C-a would catch; I cannot exclude that from here.
- I read the paragraph as written; I did not audit the rest of the entry (F1–F6, the scope/refusal section) or the
  sibling paragraphs other r75 seats own. No conflict with another seat's finding was observed.
- No tool was installed; no scratch directory was created, so nothing needs removal.

## Provenance

Files read: `corpus/knowledge/skill-eval-artefacts-round70.md` (whole), `SKILL.md:188-196` and the full file,
`corpus/QUALITY.md`, `plans/round-74.md`, `verifiers/check_skill_evals.py:190-230`,
`verifiers/check_skill_evals_v2.py:325-365`, `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md`,
`.ufo/waves/round-70/snapshots/S211-run_eval.py.txt`.

Commands run (all read-only): `git rev-parse HEAD`; `git status --porcelain -- <cited paths>`; `git log -1`;
`sha256sum` on the two snapshots; `grep -n` line maps on the snapshots, the entry, `SKILL.md` and both counters;
`sed -n` range reads incl. `cat -A` on `:227-235`; the `python3` enumeration pasted in § What holds. No `git`/`jj`
mutation, no pacman, no build, no commit.
