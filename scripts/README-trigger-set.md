# Trigger-set authoring preflight

From this repository root, with Python3 available:

    python3 -I scripts/lint_trigger_set.py train.json --validation validation.json --runs 3 --threshold 1/2

If Python3 or either requested input is missing, obtain the missing prerequisite before evaluation. The script reads local files only, never launches a model, modifies a dataset or chooses a label. Omit --validation if no held-out set is supplied. This is an authoring aid, not a client loader or a skill-routing evaluator. It is already read-only; no separate dry-run switch is needed.

Input is a nonempty JSON list of objects with a nonblank string query and boolean should_trigger. Extra keys are allowed. Strict JSON rejects repeated object keys and nonfinite constants. Limits:1MiB per file,1000 rows per set,10000 Unicode codepoints per query,1..10000 runs. Threshold is an unsigned integer, decimal or n/d in [0,1]; no spaces, signs or scientific notation. Each invalid input/settings result exits2 with one INVALID_INPUT diagnostic and no echoed query text. Train, validation, settings are checked in that order.

Exit0 means the bounded input contract passed, not that labels or queries are good. Exit1 means exact duplicate query strings or train/validation exact overlaps require author review. DUPLICATE_QUERY and CONFLICTING_LABELS pair each later occurrence with the first, using zero-based indexes. SPLIT_OVERLAP reports the first train index and current validation index. No whitespace/case/Unicode normalization is performed; paraphrases and semantic leakage remain human review. Do not silently select the first or last label to make a conflicting dataset green.

The boundary object reports exact rational equality reachability and the corresponding trigger count, including threshold0 and1. This is advisory, not an error. It does not select >= versus > for your runner; name the comparator you actually use. Outputs are deterministic JSON bounded by the record limits.

## Source and meaning
Historical lane source S211, pinned run_eval.py snapshot from round70, lines213–234, aggregates triggers by exact query but replaces the label-bearing item in completion order. Opposite labels can therefore leave a different final label depending on which task completes last. This statement describes those pinned bytes, not current upstream behavior or an executed client. The old round70 lesson already identified duplicate-denominator and equality hazards; that knowledge is not new here. This tool makes coherent authored input mechanically checkable and refuses an ambiguous label repair. The semantic quality and meaningful diversity of a trigger set remain outside its scope.

## Observed limitation from independent review

On the tested Python runtime, a runs argument made of5000 leading zeroes followed by3 satisfies the stated digit grammar and has value3, but the implementation returns INVALID_INPUT because Python's integer conversion limit is reached. Very long numeric settings can therefore be rejected despite grammatical/value validity. Use ordinary short settings. No universal numeric-string cap is asserted across Python runtimes. The original47-case mechanical result remains valid for its cases, while full unbounded-setting grammar conformance is withheld. This is a documented implementation limitation, not a changed input contract or a silently repaired first result.

### Same-round bounded correction

After the original failure was preserved, independent regression fixtures were committed and run red before repair. The revised implementation removes value-preserving leading zeroes before numeric conversion (and insignificant trailing fractional zeroes), and rejects out-of-range runs by normalized magnitude before conversion. This targets the observed defect without changing the input grammar or interpreter settings. The original paragraph above remains the first-candidate record. Arbitrarily long significant numeric values remain unproved; this is not an exhaustive grammar-completeness claim. Corrected results are recorded separately from the first47-case run.
