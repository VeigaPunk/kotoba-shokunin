# Kb82E05Baseline — corpus-baseline updater: round-81 script inspection, integration recipe, carry-pair candidate

Role: executor, leaf. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only except the
named wave paths). Plan `plans/round-82.md` read first; base `47dbe8781657de563ff867caca6244d28e3db504`.
Round-82 routed duty owned here: "Re-baseline corpus equal-count drift only after content
integration, with zero classes never carried without exact documented evidence." Production was
**not** re-baselined; no count was invented; nothing here scores an after-value.

## 1. What was inspected

- `.ufo/waves/round-81/build/refresh-corpus-baseline.py` — byte-identical to the r79 and r80
  copies (sha256 `8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a`, 419 lines).
- `verifiers/corpus-baseline.json` (sha256 `fd747ca4d4aa439bd82ee6ca24e5c7bbd924d8112fb19db19a09e8c8f6b3b22f`)
  — recorded at `6f92535`, expects `157 / 113 / 47`, all zero classes `0`.
- The two corpus gates at base, in the lane receipts (`.ufo/waves/round-82/receipts/before-integrity.txt`,
  `before-independent.txt`) and re-derived in this seat's own clone.

## 2. Base drift, exactly attributed (all measured, none predicted)

Lane-measured at base `47dbe87` (clone readings identical except the one flagged row):

| class | expect | observed | attribution |
|---|---|---|---|
| tracked_files | 157 | 158 | +1 `corpus/lessons/round-81-verifier-spotcheck.md` (closure, landed `47dbe87`) |
| unindexed | 0 | 1 | that file awaits one README coverage-map row (never carried) |
| stale / missing / nonhash | 0 | 0 | — |
| report_total | 113 | 117 | round-81.md rewrite +2, spot-check +3, one token removed → net +4 (diff-counted) |
| report_dead | 0 | **0** (lane) / **1** (scratch clone) | clone-only phantom: the tracked symlink `.ufo/reports/round-76/kotoba.md -> ../../../../.ufo/...` dangles at any non-lane depth; `round-81.md:29`'s `../../` hop reads dead there, alive in the lane |
| commit_total | 47 | 50 | `086e48c3…` (fleet-only), `a597a15d…` + `e3841861…` (lane); the `rev \`…\`` tokens (`f7388d3b…`, `4488e7f0…`) and `b3449ee2…` are not harvested by `COMMIT_RE` (needs a literal `commit \`<hex>\`` shape) — not citations |
| commit_unresolvable | 0 | 1 | `round-81.md:8` cites `commit `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`` — the W-A forged commit; lane and fleet `cat-file` both rc 128 (re-verified 2026-10-30) |

## 3. Deliverables

| artifact | what it is |
|---|---|
| `build/Kb82E05Baseline.carry-pair-updater.py` | candidate updater, sha256 `1b59106f…`, 548 lines: the r79-81 script byte-derived with exactly two changes (below) |
| `build/Kb82E05Baseline.integration-recipe.md` | the exact integration recipe for L1 (§5) |
| `build/Kb82E05Baseline/` | 18 world receipts W0-W17, each with its own captured exit |
| `build/Kb82E05Baseline.MANIFEST.sha256` | digests of every artifact above |

**Change 1 — `--carry` becomes a verified `(check_id, expected_count)` pair.** Refuses exit 2
before any write: bare name (W4), wrong count (W3: "documented 2 does not equal the observed
1"), `equal`-mode class (W5), unknown check (W8), index class (W7), duplicate (W9), inert pair
on an observed-0 class (W6). The round-81 lesson's own finding "baseline carry is class-level
and count-unbounded — a second defect in a carried class has no gate-visible signature" is
closed: the residual is stamped `observed 1 (documented 1)` in the note (W15). Nonzero zero
classes without a pair still refuse (W2: index class first).

**Change 2 — scratch-honesty preflight.** A `report_dead` detail that is a dangling symlink
inside the measuring clone refuses as an environment hazard naming the repair (W1), against
the contrast W0 where the r81 script would process the phantom reading as if it were the
tree's own defect. This is the "honors scratch" axis: TMPDIR-only temporaries were already
honored (`--keep-temp` dir landed under the scratch TMPDIR; W12 counts 0
`/tmp/refresh-corpus-baseline.*` leaks).

Unchanged and regression-checked: dirty-tree refusal (W13, incl. the just-written baseline in
the dirty list), not-a-repo refusal (W14), gate self-test precondition, hard/soft cross-checks,
never writes through a symlink, post-condition that the only drift is the named carry, exit
0/2/3 contract, detached-head honest label.

**Positive world** (emulated content landing in the sandbox: fixture README row + repaired
fleet hop, both fixture-only commits after `rev-parse --show-toplevel` assertions):
W10 dry-run exit 0 prints `tracked_files 157 -> 158`, `report_total 113 -> 117`,
`commit_total 47 -> 50`, `carried red: corpus.pointers.commit_unresolvable observed 1`;
W11 real write exit 0, `post-refresh: 8/9 checks pass, exit 1, drift:
corpus.pointers.commit_unresolvable`, `independent: exit 1` on the same class (both
instruments agree — no divergence to adjudicate); W16 the exact carried DRIFT row;
W17 final independent exit 1. The base sandbox clone's `verifiers/corpus-baseline.json` is
byte-identical to the lane's after every run (sha256 `fd747ca4…` both) — the lane was never
re-baselined.

## 4. The self-reference loop, and when a true final content tip can be measured

`report_total`/`commit_total` count tokens in `corpus/**.md` only; the baseline file lives in
`verifiers/` and is never scanned. The updater records `measured_against.head` = the pre-write
HEAD T (the content tip); its own write + commit T+1 adds zero counted tokens, so the record is
a true description of T's corpus bytes — until any `corpus/` byte changes again, at which
point it is stale *by construction* (ordering violation, not instrument drift). Round 81
tripped exactly here: `daac4cc` "refresh corpus baseline at final content tip" measured at
`6f92535`, and four later commits (`e49dbbd`…`47dbe87`) kept landing corpus content — the
"final" tip was not final, which is the entire current equal-mode drift. There is no coherent
way for the record to name "the tip that includes the baseline itself": the sha does not
exist before the file is written, so chasing it is an infinite regress; the honest stopping
point is one commit earlier, which is what the updater's label encodes.

A true final content tip is measurable only when all five hold: (a) every planned corpus byte
for the round is committed (lessons, knowledge, README rows, spot-checks, SOURCES rows);
(b) `git status --porcelain` is empty; (c) every cited commit resolves in lane or fleet — no
clone-only objects, hence the honest "detached measurement commit; resolvable in the measuring
clone only" label when measuring in scratch; (d) the tracked fleet-hop symlinks resolve at the
measuring location (else `report_dead` is a phantom, W1); (e) nothing under `corpus/` changes
afterwards — otherwise re-run the whole recipe at the new tip. For round 82 that tip is
"after the round-81 spot-check row and any S251/round-82 corpus entries land, before the
baseline commit" — the recipe in §5 of the build file states it as executable steps.

## 5. Risks and blockers (honest)

1. **The carried residual is permanent unless content changes.** `8b1cc1b0…` exists only in
   the W-A dead clone; it will never resolve. Option (a) carry `(corpus.pointers.commit_unresolvable, 1)`
   keeps the gate red on exactly one documented row forever; option (b) — lesson-owner rewrite
   of the citation into a non-`COMMIT_RE` form — makes all zero classes green but edits landed
   lesson text, which is not this seat's call. The recipe gives L1 both.
2. **Equal counts in the recipe are base values.** If round-82 content adds corpus files or
   citations, the observed equal counts move; the updater prints old -> new and refuses on
   surprises, and the L1 must re-derive the pairs from a fresh `--no-baseline --json` read at
   the actual content tip — never from this report's numbers.
3. **Do not run the refresh in a scratch clone without the hop repair.** Any clone not at the
   lane's directory depth reads the phantom `report_dead 1`; the r81 script would let it be
   named/carried, the candidate refuses. If L1 measures in scratch, repair
   `.ufo/reports/round-76/kotoba.md` to an absolute fleet target as a fixture-only commit
   first (W-world recipe: `ln -sfn /home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md
   .ufo/reports/round-76/kotoba.md`, commit, verify the gate reads `report_dead 0`).
4. One residual note-shape defect observed, not fixed (out of scope): the updater's
   `notes[note_key]` template still says "round 79 C1 repair" — cosmetic, inherited verbatim
   from the r79 script; flagged for L1.

## 6. Hygiene

Scratch root `/fast/scratch/hyaku/kotoba-r82/Kb82E05Baseline/` (clone + w2 nested clone +
tmp + receipts) deleted after all receipts were copied out. Every git mutation happened inside
the sandbox clones after a `rev-parse --show-toplevel` assertion, with scratch identity, and
every one was a fixture-only commit. No lane file was edited; lane `git status` shows only the
pre-existing wave build/receipt untracks. No tool installed or upgraded; pacman untouched; no
network fetch. Disk guard checked before heavy work (all roots <50%).

VERDICT: Round-81 script and baseline inspected and the base drift attributed token-for-token
(158/117/50 + one documented W-A residual, and one clone-only phantom report_dead); the
candidate updater refuses nonzero zero classes, honors scratch (TMPDIR + dangling-hop
preflight), and machine-verifies (check_id, expected_count) carry pairs — 18 worlds, 9 refusal
shapes + positive write, all exits captured; the self-reference loop is explained and the
integration recipe states exactly when and how the true final content tip can be measured.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E05Baseline.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E05Baseline.carry-pair-updater.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E05Baseline.integration-recipe.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E05Baseline.MANIFEST.sha256, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E05Baseline/ (W0-W17)
