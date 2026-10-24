# MutC2CodeSpan — round 66 C2 code-span exclusion mutant

Result: **killed** — removing the `inside_code_span` exclusion resurrects the r54
meta-token as a live unresolvable citation; the named self-test arm
`cites/commit-context/code-span-excluded` is the first red.

Seat: mutation-tester (leaf, no subagent dispatch). Assigned item only:
`inside_code_span` exclusion in `verifiers/verify_corpus_integrity.py` and the exact
r54 meta-finding fixture. No claim, counter, threshold, plan or receipt was changed;
no production/lane file was edited. This is observed evidence, not a rubric ruling.

## Revisions and bytes

| item | value |
|---|---|
| plan base (pinned) | `11385e04e368c1e94ab1a5a89d7439033eb1f855` |
| lane git HEAD at measure (measured tip) | `2a8eba56b3f9321b70c569fa2816d42237ca49a2` ("round-66 verifier spot-check (integrator, hyaku)") |
| lane jj `@` at measure | `98c994b017ca`; only `.ufo/waves/round-66/w1/swarm-registry.json` modified (not cloned; irrelevant to the mutant) |
| sandbox | `/fast/scratch/mutc2-r66/repo` — `git clone --no-hardlinks` of the lane, temporary |
| pristine `verifiers/verify_corpus_integrity.py` sha256 | `febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534` (equals the value in `.ufo/waves/round-66/receipts/C2-integrity-selftest.txt`) |
| `corpus/lessons/round-54-verifier-spotcheck.md` sha256 | `2a5d41d90ee3c8b3088c285c4eb4188021d75d8072b2061a4bb2848dfedea3e0` |
| exact fixture line 147, its own sha256 | `946ab5ba24e1b0276ee23520c865375d46181f560e71bc98a17c18c0b69b759c` — identical bytes at pinned base `11385e04…` and at measured tip `2a8eba5…` |

The fixture is the literal line, not a paraphrase:

```
`` commit `451a02ff` `` grammar in the new entry) was fixed in `cae8f2ea`. At the tip the entry reads
```

`COMMIT_RE` matches `commit `451a02ff``; `match_inside_code_span = true` because the outer
double-backtick run opens before `commit` and a width-2 run closes after the inner single backtick.
`451a02ff` is the upstream google-gemini/gemini-cli pin from S060, so it is absent from both the
lane and the fleet repository.

## Mutant (smallest behaviour-bearing point)

`citation_findings`, commit loop — deleted the `inside_code_span` disjunct only:

```python
# pristine
if (inside_quotes(line, match.start(1), match.end(1))
        or inside_code_span(line, match.start(0), match.end(0))):
# mutant
if inside_quotes(line, match.start(1), match.end(1)):
```

`inside_quotes` is untouched, so the double-quoted meta-finding class is unchanged and the blame is
isolated to the code-span class. `inside_code_span` remains defined but is no longer reached from
`citation_findings`. Mutated sha256:
`73df5f719b4322bb9d4ee661db0e38beb901fa8d22ed41c4e453901a68ff5305`.

## Detector (identical on pristine, mutated, restored bytes)

1. `python3 -B verifiers/verify_corpus_integrity.py --self-test` (the integrity self-test).
2. `/fast/scratch/mutc2-r66/probe.py` — loads the sandbox module, reads the exact line 147 bytes
   from `corpus/lessons/round-54-verifier-spotcheck.md`, runs them through `citation_findings`, and
   resolves with the module's own `commit_resolves(hex_id, lane_repo)` (lane-first, fleet-root
   fallback at the declared `/home/vgpnk/Projects/shokunin`, read-only `git cat-file`).
3. Full-corpus gate `python3 -B verifiers/verify_corpus_integrity.py [--json]` on the same sandbox.

## Baseline (pristine, `febfa57e…`) — detector green

```
self-test: 0 failure(s) over 161 assertions
exit=0
```

Probe:

```
match_inside_code_span = true
lane_resolves_451a02ff = false
exact-r54-line: commit_total=0 commit_unresolvable=0 commit_quoted_excluded=1
  detail: corpus/lessons/round-54-verifier-spotcheck.md:1: 451a02ff (quoted meta-finding)
```

Full gate at measured tip (pristine) — **already red for reasons that predate this mutant**:
`tracked=119 unindexed=1` (`corpus/lessons/round-66-verifier-spotcheck.md`, committed at the
non-author tip after the C2 pin), `report_dead=0/82`, `commit_total=38 unresolvable=0`,
`quoted-excluded=6`, 5/9 checks pass (drift: tracked_files, unindexed, report_total, commit_total).
So the full-corpus gate is **inconclusive as a kill criterion** at baseline; only its delta across
mutated/restored bytes is used below. The self-test and the exact-fixture probe are green at
baseline, so they carry the kill.

## Mutated (`73df5f71…`) — detector red

```
FAIL cites/commit-context/code-span-excluded: got 0 want 1
FAIL cites/commit-context/live-citation-counted: got 2 want 1
FAIL cites/commit-context/detail: got [] want ['corpus/lessons/context.md:1: 451a02ff (quoted meta-finding)']
self-test: 3 failure(s) over 161 assertions
exit=1
```

158 of 161 assertions still pass; the double-quoted arms (`cites/quoted-excluded`,
`cites/quoted-detail`, `cites/commit-total`…) stay green, so the three reds are attributable to the
removed exclusion alone.

Exact r54 fixture on mutated bytes — the meta-token becomes a live, unresolvable citation:

```
exact-r54-line: commit_total=1 commit_unresolvable=1 commit_quoted_excluded=0
  detail: corpus/lessons/round-54-verifier-spotcheck.md:1: 451a02ff
```

Same sandbox, full corpus, mutated (`--json`, `observed.corpus`):

```
commit_total=39  commit_unresolvable=1  commit_quoted_excluded=5
unresolvable_detail: ['corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff']
quoted_detail r54: []
```

Delta against pristine: `commit_total` 38→39, `commit_unresolvable` 0→1, `quoted-excluded` 6→5,
with the moved site exactly `round-54-verifier-spotcheck.md:147`. Exactly one commit token in the
tracked corpus relies solely on the code-span exclusion, and it is the r54 meta-finding the round's
D2 closure classified as context — the exclusion is load-bearing for precisely that token.

## Verdict

- Verdict: **killed** (caught at the assertion level, not merely by a count drift).
- Named arm: **`cites/commit-context/code-span-excluded`** (`got 0 want 1`), with companion arms
  `cites/commit-context/live-citation-counted` and `cites/commit-context/detail` red on the same
  bytes.
- Expected-vs-observed: expected a live unresolvable citation for `451a02ff` on the exact r54 line
  and a red code-span arm; both observed.
- Does not judge the claim, the 2-of-2 predicate, or corpus counts.

## Restoration evidence

`git checkout -- verifiers/verify_corpus_integrity.py` in the sandbox, then the same detectors:

```
sha256  febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534
self-test: 0 failure(s) over 161 assertions
exit=0
probe: match_inside_code_span=true lane_resolves=false
       exact-r54-line commit_total=0 commit_unresolvable=0 commit_quoted_excluded=1
       detail: corpus/lessons/round-54-verifier-spotcheck.md:1: 451a02ff (quoted meta-finding)
gate (--json): commit_total=38 commit_unresolvable=0 commit_quoted_excluded=6
       r54:147 present in commit_quoted_detail, absent from commit_unresolvable_detail
```

Byte hashes across the probe: pristine `febfa57e…` → mutated `73df5f71…` → restored `febfa57e…`
(identical to the recorded receipt hash). The lane working tree was not modified by this seat (the
pre-existing `swarm-registry.json` modification and other seats' untracked `w1/*.md` reports are
untouched); no branch, index, jj state, fleet root, or sibling lane was written. Sandbox
`/fast/scratch/mutc2-r66` is disposable.

## Tooling

No install or upgrade was needed; nothing to record.
