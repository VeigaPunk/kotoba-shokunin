# MutV2Regress — v2 conjunct regression ground for the C1 counter-v3

Seat: `kotoba-r61-wave-MutV2Regress` (mutation tester, leaf). Date: 2026-10-23.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only to this seat).
Base: `f3246d1493b60ea1c0d947a19c39f9e08e92f326`.
Detector: the committed counter's own bounded behavioural test,
`python3 -B <copy of verifiers/check_scoped_rules.py> --self-test`
(no network; `run_curl` is monkeypatched by the self-test; temp repos under
`tempfile.TemporaryDirectory`).

Scratch (untrusted, not evidence): `/fast/scratch/hyaku/kotoba-r61/MutV2Regress/`.
No lane, fleet, sibling, `.ufo/state`, jj, or git-index file was written. The only
read-only git commands used were `git show <base>:<path>` and
`git status --porcelain <path>`; no git/jj mutation, no dispatch, no ask tool.

## Target under attack

The claim that the v2 counter's five conjuncts are *tested* — i.e. that if a
draft v3 silently drops one while the redesign replaces the self-test, the v2
detector would have caught it. Method: take a byte-identical copy of the
committed v2 counter, drop exactly one conjunct per copy, and run the same
`--self-test` on pristine and mutated bytes. Each mutant is killed iff the
self-test exits non-zero and names the lost conjunct's assertions.

Two conjuncts have a second code site in v2 (E1's live-fetch gate; the
snapshot-quote check alongside the Gate-section quote check), so those were
probed at both sites: 5 assigned mutants + 2 site variants = 7.

## Baseline (unmutated, on the lane bytes)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T19:12:06Z
$ python3 -B verifiers/check_scoped_rules.py --self-test
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions
exit=0
```

Baseline is green, so every kill below is attributable to the mutation, not to
a pre-existing failure. The same command was run twice with identical output
(the second timestamped above, the first saved at scratch
`baseline.out`: exit 0, 0 failures, 318 assertions); a byte-identical copy at scratch
(`/fast/scratch/hyaku/kotoba-r61/MutV2Regress/v2_pristine.py`, sha256
`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`) also ran
green with exit 0, which is the copy-control for the mutants.

Environment: `Python 3.14.8`.

## Mutants, exact diffs, hashes, results

All mutants are `cp v2_pristine.py v2_mN.py` plus one hunk. `diff v2_pristine.py
v2_mN.py` output is the hunk shown. Failure counts are from
`self-test: N failure(s) over 318 assertions`; every mutant exited 1.

| # | Conjunct dropped (site) | Mutant sha256 | Exit | FAILs | Verdict |
|---|---|---|---|---|---|
| M1 | `scope_conjunct` (static judge) | `cb381bd35c60efc0e9ffe8c9ffb6e298d3c22152970a4d0292b5f71666e982c2` | 1 | 9 | killed |
| M2 | `action_conjunct` (static judge) | `03868a12662cabc525e3110afb242d3839f44036ac75bf77ffdc4d4d432d7135` | 1 | 8 | killed |
| M3 | E1 re-open gate (static judge) | `74989e4e226382f1ca50e89ef034e595d7ef23f96c858510115173a1082ad494` | 1 | 9 | killed |
| M3b | E1 base-key gate (live fetch) | `4421430f2671e558063fd7b13daa7fad0379f8f6bfbba0a0e6c2bb2910b4cbe6` | 1 | 2 | killed |
| M4 | sha256 pin equality | `458039f655a7ec240d70236ae1e0f580d63bcbdcaa3b5d6cd196e8240a513cd8` | 1 | 2 | killed |
| M5 | Gate-section quote requirement | `72805d0091aa39f5f91255d8af8bc433a31cd393dbd83262ea0a074471b6262e` | 1 | 7 | killed |
| M5b | snapshot quote occurrence | `db3fa640ec4168249f21a6955f517bea642f161ad4e29af25361139c1a7898f8` | 1 | 2 | killed |

No mutant survived, so no survivor is reported as a coverage finding. The
deliverable is the killing-assertion set v3 must carry over.

### M1 — scope conjunct dropped (`return []` folded in at the top of `scope_conjunct`)

```
916a917
>     return []  # M1: the scope conjunct dropped
```

Killing assertions (9):

```
FAIL a scope key on a line with no pattern drops the row
FAIL the no-pattern key is reported with its key and line
FAIL a description whose value mentions a pattern still fails
FAIL the Cursor table-cell line is not a key form for description
FAIL the Cursor table-cell line is not a key form for alwaysApply
FAIL a key only inside a longer identifier drops the row
FAIL an off-by-one citation to a line without the key drops the row
FAIL the off-by-one is reported at the cited line
FAIL a block value four lines down drops the row
```

### M2 — action conjunct dropped (`return []` folded in at the top of `action_conjunct`)

```
898a899
>     return []  # M2: the action conjunct dropped
```

Killing assertions (8):

```
FAIL an action on a citation line out of range is not backed
FAIL an action sharing one content word is not backed
FAIL the action shortfall is reported with its counts
FAIL an action with two content words is not backed
FAIL the thin action is reported with its count
FAIL a longer action needs half of its words, not two
FAIL the half threshold is reported with its counts
FAIL action: one shared word fails: got [], expected ['action cell shares 1 of its 4 content word(s) with line 1 (need >= 2)']
```

### M3 — E1 re-open gate dropped (static judge; base-URL rows no longer inspected)

```
1054c1054
<                 if url_key(url) in base_urls:
---
>                 if False and url_key(url) in base_urls:  # M3: E1 re-open gate dropped
```

Killing assertions (9):

```
FAIL a base URL is not backed
FAIL a base URL reached by a path-case alias is not backed
FAIL v2: base URLs without the re-open prefix are not backed
FAIL v2: the missing re-open is named
FAIL v2: the re-open prefix is a prefix, not a mention mid-cell
FAIL v2: a re-open naming a base row whose URL differs is not backed
FAIL v2: a re-open whose base row line already holds K is not backed
FAIL v2: the key collision is named
FAIL v2: a re-open naming a non-base id is not backed
```

Note: the v2 self-test's *accept* assertions ("a base URL re-opened by its base
id backs", "a plain hyphen is the same re-open separator") did **not** fail
under M3 — dropping a rejection cannot break an acceptance, so the accept set is
the other half of the constraint and must also be ported. Also, these assertions
exist and still W1/W2 met the v2 predicate per the plan: the gate is present and
tested, but its criterion (`url_key` normalisation + prefix match) is what v3
A3 replaces. That is a criterion weakness the regression ground confirms is
*tested*, not a missing test.

### M3b — E1 dropped at the live-fetch site (base-key redirect gate)

```
1218c1218,1219
<             if (base_keys is not None and url_key(final) in base_keys
<                     and url_key(final) != own_key):
---
>             if False and (base_keys is not None and url_key(final) in base_keys
>                     and url_key(final) != own_key):  # M3b: fetch-side E1 dropped
```

Killing assertions (2):

```
FAIL fetch: a redirect to a base SOURCES URL fails
FAIL fetch v2: a redirect to a different base key fails
```

Both sites must be ported: the static gate and the live-fetch gate are tested by
disjoint assertion sets (M3 never fails M3b's assertions and M3b never fails
M3's).

### M4 — sha256 pin dropped (recorded sha no longer compared with snapshot bytes)

```
1078c1078
<                     if got != sha:
---
>                     if False and got != sha:  # M4: the sha256 pin dropped
```

Killing assertions (2):

```
FAIL a snapshot whose sha256 differs is not backed
FAIL a snapshot sha mismatch is reported as such
```

The enclosing `if not sha: ... "prints no full 64-hex sha256"` rejection was
left intact; this mutant isolates only the equality conjunct. The plan's A4
also adds a rule v2 has no assertion for — "the earliest commit introducing
those bytes must be no older than the row's recorded open date" — so the M4
set cannot be the whole A4 regression ground; v3 must add a first-commit probe
for its own new clause (v2 has no counterpart to port).

### M5 — Gate-section quote requirement dropped (`quote_in_gate` returns True)

```
741c741
<     return ws(quote) in gate_raw or ws(quote.replace("`", "")) in gate_plain
---
>     return True  # M5: the Gate quote requirement dropped
```

Killing assertions (7):

```
FAIL quote absent from the Gate
FAIL an empty Gate records no quote
FAIL a quote missing from the Gate is not backed
FAIL the Gate failure is reported as such
FAIL the broken world exits 1
FAIL the broken world prints the three-of-four line
FAIL the broken world names the Gate on the reject line
```

### M5b — snapshot quote occurrence dropped (`quote_why` returns `[]`)

```
959a960
>     return []  # M5b: the snapshot quote check dropped
```

Killing assertions (2):

```
FAIL quote absent from the page
FAIL a snapshot without the quote is reported as such
```

## The set v3 must keep (mapped to the frozen arms)

The v3 predicate in `plans/round-61.md` measures `--self-test` printing
`worlds reject 7 of 7; eligible rows pass 4 of 4`. That replaces the v2
self-test's free-standing assertion list, so nothing here is ported
automatically: the L1 must re-assert these behaviours inside v3's own
self-test (or carry the v2 assertions forward), or the redesign can be green
while a v2 conjunct is gone.

| v3 arm (plan wording) | v2 assertions that pin its predecessor | Port requirement |
|---|---|---|
| A1 semantic scope-key (canonical key set; path-like value on cited line) | all 9 M1 assertions | keep: non-key line rejects; key-only-in-longer-identifier rejects; table-cell (non key form) rejects; off-by-one citation rejects; block value rejects; and the reason names key/line |
| A2 semantic action supported by cited text (not vocabulary alone) | all 8 M2 assertions | keep: out-of-range rejects; one-shared-word rejects; <3 content words rejects; half-threshold rejects; reason names counts; **plus** the new non-vocabulary probe (v3's actual change) |
| A3 URL byte-identical on re-open | all 9 M3 + 2 M3b assertions, and the v2 accept assertions | keep static: base URL requires re-open; prefix anchoring; target must be a base row; target's URL must match; base row must not already carry K; non-base id rejects. Keep fetch: final URL on a base key rejects unless it is the row's own key. **v3 must tighten** `url_key` equality to byte equality (W2 is the target). |
| A4 snapshot provenance (sha = committed bytes, quote verbatim, first-commit older bound) | M4's 2 + M5b's 2 | keep pin-mismatch rejection, the missing-pin rejection (assertion `a SOURCES row without a full 64-hex sha256 is not backed`, untouched by M4), snapshot-quote absence rejection; **add** two new probes v2 lacks: first-commit older than recorded open date rejects, and the declared wall-clock limit is stated in the receipt |
| inherited, unnamed by A1–A4: round lesson `## Gate` carries the quote | all 7 M5 assertions | v2 inherited this rule from the r59 counter (`git show f3246d14:verifiers/check_hook_files.py`: `quote_in_gate`, `gate_section`, `"round-59 Gate does not record this quote"`). The r61 arm spec does not name it. If v3 keeps v2's unchanged rules (as v2 did with r59's), the 7 assertions must be ported; if it is intentionally dropped, that is a contract change that must be declared before the measurement, not a silent deletion. This seat does not change the contract. |

Also unchanged-in-v2 and *not* covered by any mutant here because they were not
assigned: token grammar, foreign-client marker, host pins, tracker/change-note
URL rejection, quote word bounds, `Rule files` exact match, base-row/`mined`
status. They remain v2 asserted behaviours; the L1 should not read this report
as clearing or condemning them.

## Contract observations for the L1 (no judgment on fitness)

1. **A3 is narrower than E1 as implemented.** v2's E1 has three static
   sub-rules — prefix anchoring, target-is-base-row-with-this-URL, and
   base-row-must-not-already-carry-K — plus the live-fetch own-key gate. The
   plan sentence for A3 names only "byte-identical to its base row's URL". The
   killing-assertion list above is the full v2 set; whether v3 keeps all five
   sub-rules is a declaration the arm spec currently leaves open.
2. **The Gate-quote rule is inherited and unnamed.** It is older than v2
   (r59), v2 kept it, and the r61 A1–A4 text does not mention it. Its removal
   would be visible only if v3's self-test omits the 7 M5 assertions — the
   exact silent-loss mode this regression ground exists to expose.
3. **The A4 first-commit bound has no v2 assertion to port.** It is new
   coverage; a v3 self-test that only ports v2 assertions will not exercise
   it. Conversely, v2's own tests cannot be used as evidence for the new
   clause.
4. **Assertion names are behavioural, not cosmetic, for the reporting ones.**
   Eight of the killing assertions check that a specific reason string appears
   (`the ... is reported ...`, `the missing re-open is named`, `the Gate failure
   is reported as such`). The frozen C1 predicate is exit-code based, so a v3
   redesign may legitimately reword reasons; if it does, the rejection
   behaviour must still be asserted, but the wording assertions need not be
   carried verbatim. Everything else in the table is behaviour.

## Restoration and read-only evidence

- Lane file before and after (sha measured when the seat took its copy and
  again at `2026-10-23T19:12:06Z`):
  `sha256(verifiers/check_scoped_rules.py) =
  ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`
  both times. It equals the base blob:
  `git show f3246d14:verifiers/check_scoped_rules.py | sha256sum` →
  `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.
- `git status --porcelain verifiers/check_scoped_rules.py` → 0 lines.
- Pristine scratch copy re-run after all mutations:
  `python3 -B v2_pristine.py --self-test` → exit 0,
  `self-test: 0 failure(s) over 318 assertions` (sha unchanged above).
- Mutant bytes were never copied into the lane; every mutant sha256 differs
  from the pristine sha256 and each differs from pristine by exactly one hunk
  (diffs pasted above).
- The lane's only untracked entries during this seat were sibling scribe
  reports (`ScribeC3.md`, `ScribeShonen.md`, `ScribeSkillReg.md`), none touched
  by this seat.

## Limits

- This is a self-test regression ground, not a world-fixture measurement: it
  proves which v2 assertion kills a dropped v2 conjunct. It does not prove v3's
  seven worlds reject or that its four eligible rows pass; those are the L1's
  integrated measurement.
- No mutant survived, so this probe yields no evidence about v3's *new* arms
  (A1's canonical key set, A2's non-vocabulary support, A3's byte equality,
  A4's first-commit bound). Those need their own detectors in v3.
- `--self-test` was the only detector run; no `--fetch`, no network, no live
  page.

Installs: no installs (Python 3.14.8 preinstalled; no pacman, no uv/npx).
Blockers: none.
Attacked: the v2 counter's five conjuncts by one-site-per-copy deletion (plus two second-site probes), yielding the killing-assertion set v3 must keep.
