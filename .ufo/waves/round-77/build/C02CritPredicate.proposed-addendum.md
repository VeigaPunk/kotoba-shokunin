# Proposed text — `plans/round-77-addendum-1.md` (pre-data)

Date: 2026-10-27. Author: L1 `KotobaR77`.

## Predicate identity and frozen-counter disclosure

The round-77 operational predicates are the two complete sentences in `plans/round-77.md` §§ C1 and C2, including the r77 base `2f675548eaad2a037a899d39247c1fd7a88aaf48` and the printed red result. The counter files are frozen unchanged from r76; their docstrings therefore retain the r76-base description `b7f13f4b39cbd43076a85568adca763a6f674e7a`. This is a disclosed historical-base difference, not a change to either counter's logic or success condition: both counters were directly run at both bases and print the specified `0 of 6` / `0 of 4`, exit 1. Do not describe the byte-frozen docstring as quoting the full r77 sentence verbatim.

For the r77 record, each receipt and SCORECARD row must record the exact r77 operational sentence verbatim, plus its command's measured revision/output/own exit status. A command-only receipt label is not a predicate quotation. Existing r77 base receipts record command, frozen-counter digest, measured revision, output and direct exit status; they do not contain the full predicate sentence. Add that sentence to any subsequent r77 receipt/SCORECARD draft before data, without altering counter bytes or historical receipts. The r76 SCORECARD draft and r76 receipts are historical evidence and retain their r76-base sentence/results; they are not the r77 SCORECARD row or receipt.

The requirement in round-76-addendum-2 §5 that the canonical sentence include the full base hash and be quoted verbatim by unchanged counter docstrings cannot hold across a new round with a different base. This addendum supersedes only that cross-round identity requirement; it does not change conjuncts, repair checks, success outputs, exit conditions, or r76 records.

## No-harm prerequisite

At frozen r77 HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`, `check_gate_registry.py --rev HEAD` reports `60 of 62 lane verifiers; phantom 0`, exit 1. The frozen floors check also exits 1, and the tip battery exits 1 (six constituent failures). These are pre-data defects, not harmless undisclosed hygiene. Before claiming no-harm, the integration must resolve the missing gate-registry rows and investigate/repair the floors and battery failures, then capture direct-status receipts. Do not infer closure from round-76 addendum-6 prose.
