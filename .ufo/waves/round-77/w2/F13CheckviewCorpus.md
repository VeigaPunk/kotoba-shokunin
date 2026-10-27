Seat: F13CheckviewCorpus — corpus README index review

## Scope and revision

Reviewed committed lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (the r77 freeze), not a landed claim-data tip. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --short --branch` showed tracked tree clean and HEAD at that revision; w1/build/receipt material was untracked. The requested `build/entry-draft.md` was not present at the named path. The round-77 plan says claims/data land only after controls and integration; no data commit is present at this HEAD. Therefore this is a blocker to falsifying *landed* C1/C2 or a new README row: no such landed artifact was available.

## Frozen counter runs

Counter byte pins match `plans/round-77.md` exactly (`sha256sum`):

- `verifiers/check_desc_craft.py`: `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`
- `verifiers/check_r75_routed_repairs.py`: `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`

Commands and direct exit statuses at revision `6523aced1ee0ebe07dca996213bdc645a6acbd1e`:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_desc_craft.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e
```
Output: `(a)`–`(f)` all fail; `description craft backed 0 of 6`. Exit 1. Thus the expected 6/6 claim is not landed/verified at HEAD.

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work /fast/scratch/hyaku/kotoba-r77/F13ReviewCorpus/work
```
Output: R1–R4 open; `r75 routed repairs closed 0 of 4`. Exit 1. Thus the expected 4/4 claim is not landed/verified at HEAD. No scratch clone was needed; `--work` was passed as requested.

## Corpus README index against verifiers

Read `corpus/README.md` and both verifiers (`verify_corpus_integrity.py`, `verify_corpus_independent.py`). The index coverage-map rows are read as promises by both instruments. Ran:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_integrity.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --json
```
Exit 1. Observed `tracked_files=146`, expected 144; `unindexed=2`, specifically `corpus/lessons/round-75-verifier-spotcheck.md` and `corpus/lessons/round-76-verifier-spotcheck.md`; stale patterns and missing paths are both 0. Baseline comparisons also drift: report pointers 102 vs expected 99, commit citations 44 vs expected 43; dead report pointers and unresolved/nonhash commits are 0.

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_independent.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokukin --json
```
The executed command used the lane path `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (not the typo above). Exit 1; independently observed the same two unindexed spot-check lessons, with 0 stale tokens, missing paths, dead pointers, unresolved commits, or nonhash commits. This corroborates the index coverage defect without treating either instrument's reported exit as proof of C1/C2.

Minimal repair for the index finding is to add coverage-map entries for those two tracked lessons, then reconcile the baseline's three changed aggregate counts against the actual intended corpus scope and rerun both corpus instruments at the final committed tip. The index omission harms corpus operability/integrity; it does not alter either frozen claim predicate, but the red no-harm gates prevent asserting a clean final state. I did not modify lane data or run mutation tests: the claim/data-bearing landed tip required for the requested w2 mutation/review is absent here.

VERDICT: BLOCKED — r77 HEAD is the freeze with no landed claim data; both pinned counters are red and both corpus verifiers independently report two unindexed lessons.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F13CheckviewCorpus.md