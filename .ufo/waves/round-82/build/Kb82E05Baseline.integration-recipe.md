# Kb82E05Baseline — round-82 corpus-baseline integration recipe

Companion to the w1 report `Kb82E05Baseline.md`. Everything below was measured on
2026-10-30 at base `47dbe8781657de563ff867caca6244d28e3db504` in scratch clones
(root `/fast/scratch/hyaku/kotoba-r82/Kb82E05Baseline/`); no lane file was mutated,
no count was invented, production was not re-baselined.

## 1. What the committed baseline records vs what base observes

Committed `verifiers/corpus-baseline.json` (sha256 `fd747ca4d4aa439bd82ee6ca24e5c7bbd924d8112fb19db19a09e8c8f6b3b22f`)
was refreshed at `6f92535` ("round-81: align lesson evidence draft with landed text") and
expects `tracked_files 157 / report_total 113 / commit_total 47`, all six zero classes `0`.

At base `47dbe87` the lane's own gates observe (receipts `.ufo/waves/round-82/receipts/before-integrity.txt`,
`before-independent.txt`; re-derived independently in this seat's clone):

| class | mode | expect | observed (lane) | observed (/fast clone) |
|---|---|---|---|---|
| corpus.index.tracked_files | equal | 157 | 158 | 158 |
| corpus.index.unindexed | zero | 0 | 1 | 1 |
| corpus.index.stale_patterns | zero | 0 | 0 | 0 |
| corpus.index.missing_paths | zero | 0 | 0 | 0 |
| corpus.pointers.report_total | equal | 113 | 117 | 117 |
| corpus.pointers.report_dead | zero | 0 | **0** | **1 (phantom)** |
| corpus.pointers.commit_total | equal | 47 | 50 | 50 |
| corpus.pointers.commit_unresolvable | zero | 0 | 1 | 1 |
| corpus.pointers.commit_nonhash | zero | 0 | 0 | 0 |

The `report_dead` row is host-layout-dependent: `corpus/lessons/round-81.md:29` cites
`../../.ufo/reports/round-76/kotoba.md`, which resolves through the *tracked* symlink
`.ufo/reports/round-76/kotoba.md -> ../../../../.ufo/reports/round-76/kotoba.md`. In the
lane that symlink reaches the fleet file (8,128 B, `## SHONEN`, alive). In any clone not
checked out at the lane's directory depth the same symlink dangles and both corpus gates
read `report_dead 1` — a phantom that must never be carried (W0/W1 receipts).

## 2. Exact drift attribution (6f92535 -> 47dbe87, verified by diff + gate)

- **tracked_files 157 -> 158 (+1):** `corpus/lessons/round-81-verifier-spotcheck.md` (closure
  spot-check, landed at `47dbe87`, non-author).
- **unindexed 0 -> 1:** that same file awaits one `corpus/README.md` coverage-map row.
- **report_total 113 -> 117 (+4):** round-81.md rewrite +2 (`../../.ufo/reports/round-76/kotoba.md`,
  `.ufo/reports/round-77/kotoba.md`), spot-check +3 (`round-77` x1, `round-81` x2), one round-76
  token removed in the rewrite: net +4.
- **commit_total 47 -> 50 (+3):** `086e48c3e95f058866c2301cb66337eca94566aa` (fleet-only — the
  round-81 report's fleet commit), `a597a15da200d1b3be38b0e1b567c9944c5ecb00` (lane),
  `e3841861da1738bcbefd9dacd8f4ac8f8be343b7` (lane). The other new 40-hex tokens
  (`f7388d3b…`, `4488e7f0…`) are `rev \`…\`` forms and `b3449ee2…` has no `commit ` prefix, so
  `COMMIT_RE` never harvests them — they are not citations and need no action here.
- **commit_unresolvable 0 -> 1 (the only true zero-mode residual):**
  `corpus/lessons/round-81.md:8` — "W-A builds a real commit
  `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1` in a dead clone (lane and fleet both
  `cat-file` rc 128)". Re-verified today: lane MISS, fleet MISS. The token matches the gate's
  citation shape (`commit \`<hex>\``) and will never resolve; it is the documented W-A
  forged-commit evidence. Options for L1:
  - **(a) carry** `(corpus.pointers.commit_unresolvable, 1)` — the r80-precedent shape, now
    machine-verified by the pair updater; or
  - **(b) content repair** (lesson-owner choice): rewrite the citation so it no longer matches
    `COMMIT_RE` (e.g. `rev \`8b1cc1b…\`` backtick form, like its siblings) — then zero classes
    are all green and no carry is needed. Editing landed lesson text is not this seat's call.

## 3. The integration recipe (order matters — the self-reference loop)

1. **Land all round-82 corpus content first** (README coverage row for the round-81 spot-check;
   any round-82 lesson/knowledge/SOURCES rows; S251 entry). Nothing in `corpus/` may change
   after step 4. `unindexed` must read 0 — an index class is never carried.
2. At the clean content tip T (`git status --porcelain` empty), read the drift:
   `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json`
   Expect exactly: `tracked 158, unindexed 0, stale 0, missing 0, report_total 117,
   report_dead 0, commit_total 50, commit_unresolvable 1, nonhash 0` (adjust equal counts if
   round-82 content adds corpus files; the updater prints old -> new and refuses on any
   surprise). Measure where the lane's fleet-hop symlinks resolve (`--repo .` on the lane, or a
   clone whose depth makes `../../../../.ufo` reach the fleet); never measure a layout that
   reads the phantom `report_dead 1`.
3. Run the updater with the exact documented pair:
   `python3 -B .ufo/waves/round-82/build/refresh-corpus-baseline.py --repo . \
        --note-key round82_rerecord --carry corpus.pointers.commit_unresolvable=1`
   (choose option (b) in §2 instead and drop the `--carry`). Exit must be 0 with
   `post-refresh: 8/9 checks pass … drift: corpus.pointers.commit_unresolvable` and
   `independent: exit 1` on the same residual. Any other drift refuses or exits 3 — stop.
4. Commit **only** `verifiers/corpus-baseline.json` (baseline-alone commit; no amend). The
   recorded `head` is T, the content tip — the baseline commit itself adds zero counted
   tokens because the gates scan `corpus/**` only.
5. Re-run both corpus gates and keep the receipts: integrity exit 1 with exactly the one
   carried DRIFT row `{"check": "corpus.pointers.commit_unresolvable", "mode": "zero",
   "observed": 1, "expected": "0 / empty", "verdict": "DRIFT"}` (measured W16); independent
   exit 1 on the same class. A green corpus is NOT claimed; the residual is named.
6. If any `corpus/` byte lands after step 4, the equal counts move and the baseline is stale
   by construction — re-run the whole recipe at the new final tip (this is exactly what
   round 81 tripped on: `daac4cc` refreshed at `6f92535` and four later commits kept landing
   content, leaving base with 4-5 DRIFT rows).

## 4. When a "true final content tip" can be measured

Only when (a) every planned corpus byte for the round is committed, (b) the tree is clean,
(c) every cited commit resolves in lane or fleet (no clone-only objects — hence the updater's
honest "detached measurement commit" label when measuring in scratch), (d) the fleet-hop
symlinks resolve at the measuring location, and (e) nothing under `corpus/` changes
afterwards. The baseline's `measured_against.head` always names the pre-write content tip;
the baseline commit is metadata-only and changes no counted class, so the record is a true
description of that tip — until the next content commit, which is an ordering violation, not
a baseline defect. `report_total`/`commit_total` can never describe "the tip that includes
the baseline itself" without chasing its own tail; the record stops one commit earlier by
design.

## 5. The candidate updater

`Kb82E05Baseline.carry-pair-updater.py` (sha256 `1b59106fdaede7310b1e27026693d152b052c572a01f3d6eadcef44d3242afa8`,
548 lines) is the r79/80/81 script (sha256 `8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a`,
419 lines) byte-derived with exactly two changes:

1. `--carry` takes `CHECK_ID=EXPECTED_COUNT` pairs. Verified fail-closed: bare name, wrong
   count, equal-mode class, unknown check, index class, duplicate, or inert (observed 0) pair
   all refuse exit 2 before any write; the carried residual is stamped
   `observed N (documented N)` in `measured_against.note`. A carried class can no longer
   silently grow a second defect — the round-81 lesson's own "carry is class-level and
   count-unbounded" finding, closed.
2. Scratch-honesty preflight: a `report_dead` detail whose cited path dangles as a symlink
   inside the measuring clone refuses as an environment hazard (naming the repair), so the
   phantom layout reading can never be fixed or carried as if it were the tree's defect.

Unchanged: dirty-tree/untracked refusal, gate self-test precondition, hard/soft cross-checks,
TMPDIR-only temporaries (`--keep-temp` receipt shows the dir under the scratch TMPDIR; W12
confirms zero `/tmp/refresh-corpus-baseline.*` leakage), baseline-alone write never through a
symlink, post-condition that the only drift is a named carry, exit 0/2/3 contract.

Worlds (all receipts under `build/Kb82E05Baseline/`): W0 r81 script on unfixed clone (refuse,
phantom mixed into zero classes); W1 candidate on unfixed clone (preflight refusal); W2 no
carry after hop repair (refuse, index class first); W3 wrong count; W4 bare carry; W5
equal-mode carry; W6 inert carry; W7 index carry; W8 unknown carry; W9 duplicate carry; W10
dry-run correct pair (exit 0, `157->158 / 113->117 / 47->50`); W11 real write (exit 0,
`post-refresh: 8/9 … drift: corpus.pointers.commit_unresolvable`, independent exit 1); W12
TMPDIR leak check 0; W13 dirty tree refuse; W14 not-a-repo refuse; W15 written baseline note;
W16 final integrity 8 PASS + 1 carried DRIFT, exit 1; W17 final independent exit 1.
