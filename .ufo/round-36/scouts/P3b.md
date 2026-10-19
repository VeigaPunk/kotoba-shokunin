# Scout P3b

## Task
Claim P3, fix draft B — fence-aware coverage census, independent design from A/P2. /dev/shm only; HEAD `754197e` untouched. Trees `/dev/shm/p3b/{base,draftB}`, diffs `out/*.diff`, outputs `out/*.txt|json`.

## Commands
```
cp -a . /dev/shm/p3b/{base,draftB}; python3 - <<'PY'   # patch draftB
python3 verifiers/{verify_corpus_integrity,verify_corpus_independent}.py [--json|--self-test]
TMPDIR=/dev/shm python3 verifiers/check_assertion_floors.py
TMPDIR=/dev/shm bash verifiers/fault_injection_corpus.sh
# probe matrix: 6 mutated copies pA1..pA4,pC1,pC2 vs base+draftB
```

## Findings
Diff — primary `+75`, independent `+87`, floors `+6`, no new imports. Per file: `FENCE_RE` (`^[ \t]*(`{3,}|~{3,})(.*)$`); `fenced_lines()` (1-based set; closes only on its own delimiter char; **unclosed runs to EOF** = fail-closed); the census **classifies** rather than skips — `index_tokens_fenced` + `_detail` beside the existing `index_tokens_excluded` (the round-33 named-class rule at :329); fence fixture + 11 primary / 7 independent self-test pins.

**Design delta vs draft A (P2):** A patches the primary only, so after landing the two witnesses disagree (P2's defect 2) — B patches **both**, fence helper mirrored; B also bumps the floors in-step (A prints `observed=113 floor=108`).

Proofs, base → draftB, both instruments unless noted: live `tracked=53 index_patterns=69 unindexed=0 stale=0 missing=0` exit 0; primary stdout **byte-identical**; primary `--json` adds exactly 2 keys (`index_tokens_fenced: 0`, `[]`; checked: added=2 changed=0 missing=0); independent stdout **and** json byte-identical. Probes (primary/independent exit): fenced row swap 0→**1/1** (`unindexed=1` naming `frontmatter-trigger-surface.md`); **all** rows fenced 0→**1/1** (`unindexed=52`/51, patterns 0); unclosed fence 0→**1**; `~~~` fence 0→**1/1**; control fenced dead-path row 0→**0/0** (not a promise); control unfenced dead-path 0→**1/1** (`stale=1 missing=1`) — the fence, not the row, is the discriminator. Self-tests 108→**119**, 52→**59**, 0 failures; floors `PASS corpus_integrity observed=119 floor=119` (half-bump → `FAIL registry floor drift` exit 2); corpus/independent/surfaces/harness/pins gates exit 0; fault harness **ALL PASS**.

## Defects
1. **[MEDIUM, confirmed — claim target]** `verify_corpus_integrity.py:300 file_column_tokens` has no fence state; a row quoted in a ``` block satisfies the census. Total, not marginal: fencing **every** row still exits 0. Closed by this patch.
2. **[MEDIUM, NEW]** `verify_corpus_independent.py:213 coverage_cells` — same section-only shape, same probe, exit 0. Closed by B; left open by A.
3. **[LOW, corroborates P1]** P3's "two globs replace all rows and still pass" is false as written: glob-only keeps index green but DRIFTs `report_total` 36→23, `commit_total` 27→16 (exit 1). The fenced-row probe is the real red-before.
4. **[LOW]** the walker reads the whole document, so a fence opened below `## Known gaps` is order-sensitive; no live effect (byte-invariant).

## Limits
Nothing landed, no LOG.md entry, no repo file written but this fragment. The corpus is a /dev/shm copy, so the checklist gate fails there on path reasons only (`name_directory`, host-relative citations); it is exit 0 on the real repo and B touches no checklist input. Tab-indented openers and an unbalanced fence mid-map not swept across all 49 rows.
