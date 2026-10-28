# Kb80E04DeadPointer.blob — what the published sha means

`Kb80E04DeadPointer.blob` (one line) holds the **git blob sha1 of
`verifiers/verify_corpus_integrity.py` after the E04 dead-report-pointer repair
applied to the round-80 base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`**:

    051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f  verifiers/verify_corpus_integrity.py

Derived by: `git -C <scratch clone> hash-object verifiers/verify_corpus_integrity.py`
after `git apply .ufo/waves/round-80/build/Kb80E04DeadPointer.patch` on the base,
committed as `83f6dc055308d889bf91a229457149cde61d38a0` in the scratch clone
(`/fast/scratch/hyaku/kotoba-r80/Kb80E04DeadPointer`, removed at yield).

## Why this sha alone may not be the pin the counter needs

The tip battery's `instrument-pin` guard compares the blob **at the measured rev**
against a tuple of allowed blobs (`verifiers/check_tip_battery.py:310-314`,
`if blob not in allowed`). If the grammar-class repair (E05, § C1 repair 5 —
"both corpus gates") also edits `verifiers/verify_corpus_integrity.py`, then the
TIP blob of that file is the **E04 ∘ E05 combined** content, not the E04-only
blob above.

The guard's test is membership in a TUPLE and the shipped table already lists
several blobs per path (e.g. `check_assertion_floors.py` has three), so
`INSTRUMENT_PINS["verifiers/verify_corpus_integrity.py"]` may carry BOTH the
E04-only blob and the combined blob; the pin then holds for either stack.

To compute the combined blob for any grammar patch (one command, and the result
is order-independent — measured in both orders):

    bash .ufo/waves/round-80/build/Kb80E04DeadPointer/compute-combined-blob.sh <grammar-patch>

It prints the combined integrity blob, the patched independent blob, and the
six-instrument `git diff --numstat` against the pinned battery base
`072048fa8e8a52c707d25f7079772fa317244eb7` (the number the `instrument-size`
guard sums).

COMPOSED value (E04 ∘ grammar class), measured from the published stack
`.ufo/waves/round-80/build/Kb80Y01-simplified.patch`, which embeds my E04 hunk
byte-identically (Y01's "@@ -272,6 +274,12" hunk's added lines == my patch hunk #1's
added lines, compared programmatically):

    cc182613a4d089c41e44f11b50e03b45ce582dd8  verifiers/verify_corpus_integrity.py
    89f392daab3e4181db3ded7676ca0879871ef7ff  verifiers/verify_corpus_independent.py

These are exactly the two values Y01's pin table appends; its tip battery at that
stack reads "guards 5 of 5; tip battery exit 0: 6 of 6", exit 0. The L1's plan
Addendum 1 states the integrity pin is the composed blob, not the E04-only value,
so `051b8c5f…` is the E04-only CROSS-CHECK value only.

Measured line budget (the plan's arithmetic "22 already spent at base + 17 E04 +
grammar ≤ 21 = 60"):

    22  3  verifiers/check_assertion_floors.py      (pre-existing at base)
    17  0  verifiers/verify_corpus_integrity.py     (E04)
    => 39 added / 3 deleted; 21 added lines remain for the grammar class
       across BOTH corpus gates under the erratum's cap of 60.
