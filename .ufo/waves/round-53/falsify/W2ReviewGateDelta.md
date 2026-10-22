Result: MIXED — the M41 fix instrument `verifiers/check_gate_finding_delta.py` HOLDS on every assigned attack (self-test 0 failures over 9 assertions; pair 1 exactly as expected; pair 2 run clean; byte-identical output lane vs sandbox; byte-identical to the wave-1 draft shown able to fail), but it exposed a HIGH round-content defect (the committed tip is corpus-red with a NEW finding id vs base: `corpus/SOURCES.md:63` cites the foreign Zed commit `cfb894a5` as a bare token), and the instrument has defects of its own: MEDIUM exit-1 misattribution on gate/environment failure, and an unstated gate contract that non-corpus gates crash through (LOW-MEDIUM with the docstring gap).

## Target and provenance

- Judged file: `verifiers/check_gate_finding_delta.py`, 171 lines, sha256
  `1c41414eff46bdf7850963c98535c09a86f90bde1764da18f92159ad6853f41a` (measured on the lane at
  `c775d6823bfca8f0de8c0874032a954438b38edc`). Byte-identical to the draft `.ufo/waves/round-53/build/ScribeMistake.md:40`
  records as "shown able to fail" — the landed instrument is exactly the one demonstrated red at `0c9180a6`.
- The M41 lesson row landed at `corpus/lessons/round-53.md:12`; `corpus/README.md:82` (uncommitted worktree edit at
  review time) points the fix at this file.

## Assigned runs (all commands + observed output + exit code)

Host: python3 3.14.8, git present. No installs or upgrades were made.

1. `python3 -B verifiers/check_gate_finding_delta.py --self-test` (from the lane checkout) →
   `self-test: 0 failure(s) over 9 assertions`, exit **0**. The printed count matches the 9 `eq(...)` calls in the source.
2. Pair 1, lane, read-only: `python3 -B verifiers/check_gate_finding_delta.py --repo . --base c8579a4c5b48789e56fb9060ddd48f33569e1215 --head 0c9180a69017c47d36b5f032c4bb27ed1d131908`
   → `new: corpus.pointers.commit_total`, `resolved: corpus.index.unindexed`, base drift 4 / head drift 4,
   `finding delta: new 1, resolved 1`, exit **1**. Exactly the assignment's expectation and exactly the M41 row
   (`corpus/lessons/round-53.md:12`): same pass count (5/9 both sides), changed set.
3. Pair 2, lane, read-only: `--base e78dff667237fba2e3cf9eccb802eff5bc9ea302 --head c775d6823bfca8f0de8c0874032a954438b38edc`
   → `new: corpus.pointers.commit_unresolvable`, `resolved: corpus.pointers.report_dead`, base drift 5 / head drift 5,
   exit **1**. See F1: the round's own tip carries a new corpus-integrity finding id.
4. Sandbox cross-check (clone `/fast/scratch/hyaku/kotoba-r53/w2/W2ReviewGateDelta` at `c775d68`, clean):
   both pairs re-run with `--json`; drift sets, new/resolved and exit codes byte-equal to the lane runs.
   Pair-1 JSON: base drift {tracked_files, unindexed, report_dead, report_total}, head drift
   {tracked_files, commit_total, report_dead, report_total}. Pair-2 JSON: base drift
   {tracked_files, unindexed, commit_total, report_dead, report_total}, head drift
   {tracked_files, unindexed, commit_total, commit_unresolvable, report_total}. Gate exit codes recorded in JSON: 1 on both sides of both pairs.
5. Lane cleanliness: `git status --porcelain` before my runs listed 10 lines; after my runs the lane was unchanged by
   them — the count later moved to 9 then 14 lines because an external actor (the L1's integration) committed
   `b5dc7dcf` and kept editing while I worked; my runs pinned explicit revisions via `git archive` and are unaffected.
   The instrument's writes stay under the system temp (`GIT_INDEX_FILE` → `/tmp/finding-delta.*`, extracted trees in a
   `TemporaryDirectory`); no lane index or jj state was touched.

## Findings

**F1 — HIGH (round content, caught by the new instrument).** At the judged tip `c775d682` the corpus gate is red with
a finding id base `e78dff66` did not have: `corpus.pointers.commit_unresolvable`, observed 1. Site:
`corpus/SOURCES.md:63` — SOURCES row S050 (Zed) cites the upstream docs-source commit as bare `` `cfb894a5` `` in the
committed text; `git cat-file -t cfb894a5` → `fatal: Not a valid object name …`, exit 128. The worktree edit prefixes
it to `zed-industries/zed@\`cfb894a5\``, which the gate excludes as a foreign pointer — but that edit is **uncommitted**,
and the bare token is still committed at the newer tip `b5dc7dcf` too (verified with `git grep -n cfb894a5 b5dc7dcf -- corpus/SOURCES.md`).
Both sides of pair 2 read 4/9 pass — the exact M41 signature (same count, changed set), recurring inside the round that
fixed M41. Plan routed defect 2 said "re-record the baseline last, after every round file has landed"; corpus files
(S050 row, C2 knowledge entry, C1 census entry, floors-commit line) landed after the `aeed089` re-record, and the
baseline at the tip is stale again (tracked_files 77/72, report_total 49/46, commit_total 32/30 at the committed tree).
The instrument is the only assigned check that saw this: the no-harm exit-code comparison reports exit 1 → exit 1 as
"unchanged". For the L1: commit the SOURCES fix (or re-record last at closure) or the round closes on a red corpus gate
with a new finding id.

**F2 — MEDIUM (instrument).** Gate or environment failure exits **1** — the "new finding" code — with a raw traceback,
instead of the documented exit 2 ("environment unreadable"). Three reproduced paths (each once, in the sandbox):
(a) unknown revision: `--base 0000000000000000000000000000000000000000` → `CalledProcessError` from `git archive`
(`check_gate_finding_delta.py:56-58`, `check=True`), exit 1; (b) gate prints non-JSON with exit 0 → `JSONDecodeError`
at `findings()` `json.loads` (`:47`), exit 1 (stub probe); (c) gate prints JSON without a `results` key → `KeyError`
(`:49`), exit 1 (stub probe, and for real on both gates in F3). Only `returncode ∉ {0,1}` and empty stdout are mapped
to exit 2 (`:47-52`). The whole point of M41 was that lane no-harm checks trust exit codes; an instrument that can
raise a false "new finding" on a broken gate fails in the fail-noisy direction of the same trust. Not triggered on the
canonical pairs.

**F3 — LOW-MEDIUM (instrument + docstring).** Docstring vs code vs reach, on the assigned question "general or
corpus-integrity only":
- Code: `red = [r["check"] for r in doc["results"] if r["verdict"] != "PASS"]` (`:49`) — every non-PASS verdict is a
  finding. Docstring (`:10-11`) says it "compares the DRIFT check ids". Stub proof: a gate emitting
  `{"results":[{"check":"z","verdict":"OBSERVE"}]}` at head only prints `new: z`, exit 1. On the corpus gate with a
  recorded baseline no OBSERVE rows occur, so the canonical pairs are unaffected; the mismatch is doc/code.
- Generality: the docstring never says "corpus-integrity only", but it also never states the contract a foreign gate
  must honor (`--repo` + `--json`, top-level `results[].check`/`results[].verdict`, exit ⊆ {0,1}, stdout pure JSON).
  Empirically: `--gate verifiers/verify_corpus_independent.py` on pair 1 **works** (base drift 5, head drift 4,
  resolved `corpus.index.unindexed`, exit 0 — mechanically general to the second corpus gate). `--gate
  verifiers/verify_surfaces.py` and `--gate verifiers/verify_skill_checklist.py` on pair 1 both **crash**:
  `KeyError: 'results'`, exit 1 (their `--json` shapes have no top-level `results`) — i.e. outside the corpus pair the
  tool fails in F2's misattributing direction. A gate without `--repo` fails cleanly: `--gate
  verifiers/verify_alwayson.py` → `could not evaluate … exit 2` (and the file does not exist in pre-C2 trees anyway),
  exit 2. Verdict: general by flag and by defaulting to the corpus gate; proven for the two corpus gates; broken
  (crash, exit 1) for the lane's surfaces and checklist gates; the docstring must state the contract or the
  corpus-only scope — today it says neither.

**F4 — LOW (instrument, self-test coverage).** `--self-test` exercises `delta()` (5 arms) and `findings()` over stub
trees (4 arms) but never `extract()`, `revision_env()` or `run()`'s return: the exit arms recompute
`1 if delta(...)[0] else 0` — the same expression `run()` uses — so an inverted or dropped return in `run()` would
pass self-test. The pair runs cover that plumbing externally (this review). Minor: the "over 9 assertions" count is
hardcoded (`:142`), unlike the corpus gate's dynamic count.

**F5 — INFO (edge, not hit).** A revision without `verifiers/corpus-baseline.json` evaluates all rows OBSERVE
(`verify_corpus_integrity.py:679`), which this tool counts as drift ids; a baseline-less/base-ful pair would report
spurious `new`/`resolved`. The canonical gate contract implicitly requires a recorded baseline at both revisions;
the docstring does not say so.

## Residual risk and verification gaps

- The surfaces/checklist crash (F3) was reproduced once per gate; I did not inventory their JSON shapes beyond the
  failing key, and did not probe any gate outside `verifiers/`.
- Pair 2 reflects committed trees only. The worktree diverges (uncommitted SOURCES/knowledge/README edits fix the
  token but leave the baseline stale), and HEAD advanced to `b5dc7dcf` during review; my findings are stated against
  the judged revision `c775d6823` (the bare token persists at `b5dc7dcf` as committed).
- I did not verify whether OBSERVE-mode rows can occur on the corpus gate with the tip's recorded baseline beyond
  observing none in six gate runs.
- F1's severity assumes the corpus gate's finding-set semantics are themselves sound; that gate is outside my target
  and was used as given (its own self-test and floors are other seats' scope).

## Bounds compliance

Single lane write: this report. All probes, stubs and the clone live under `/fast/scratch/hyaku/kotoba-r53/w2/W2ReviewGateDelta/`
and the system temp; git writes only inside the clone; no jj commands; no installs or upgrades (python3 3.14.8 and git
already present); no paid model calls, no `model` parameter, no `ask`.
