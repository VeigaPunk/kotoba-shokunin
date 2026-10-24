# Round 67 wave 1 — SOURCES append-only review

## Scope and measured identities

Axes reviewed: existing-row preservation, actual verifier CLI/range behavior, census
E03/E04 refusal, and reproducibility of the measured bytes.

- Pinned base: `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. Both `HEAD` and `master`
  still resolved to this revision at the last check; there was no committed append tip to measure.
- The assigned draft was absent on the first read. I screened the 164 staged rows while it was
  absent. It subsequently appeared; the primary results below are for the actual three-row draft,
  not a reviewer-written substitute.
- Reviewed draft: `.ufo/waves/round-67/w1/drafts/SOURCES.append.r67.md`, three rows
  S123/S124/S129, uncommitted sha256
  `4294646dd727a9b25c5b0632a092d5d0318e7bc721fb50923862c3ef7584a953`.
- Sandbox: `/tmp/kotoba-r67-ReviewAppendOnly.GPnkdk`. The before bytes for the pinned run came
  from `git show 2a8eba56b3f9321b70c569fa2816d42237ca49a2:corpus/SOURCES.md`, not from the
  changing working tree. The combined draft-world sha256 was
  `642f911c5c2cf13fe145f00c5e648d7b88d8d0b689523e43295975582ca0d387`.
- Tooling installs: none. No git/jj write command was run; sandbox mutations were under `/tmp`.

## Findings by severity

### Medium — the requested `--tip` invocation cannot supply Q34 evidence

The seat item's literal command is not accepted by the verifier. Observed at the pinned base:

```text
$ python3 -B verifiers/check_sources_append_only.py --base 2a8eba56b3f9321b70c569fa2816d42237ca49a2 --tip 2a8eba56b3f9321b70c569fa2816d42237ca49a2
usage: check_sources_append_only.py [-h] [--rev REV] [--base BASE]
                                    [--repo REPO] [--self-test] [--quiet-log]
check_sources_append_only.py: error: unrecognized arguments: --tip 2a8eba56b3f9321b70c569fa2816d42237ca49a2
exit 2
```

`verifiers/check_sources_append_only.py:162-170` defines `--rev`, not `--tip`; its docstring
also declares usage/environment exit 2 (`:22`). Use `--rev <tip>`. A base-to-base invocation was
run only as a CLI control and printed `0 commits scanned`; that empty range is **not** append
evidence. Q34 (`corpus/QUALITY.md:45`) still requires the real claimed range and pasted output.

### Low — the assigned draft and the live working-tree append have different identities

While this review ran, `corpus/SOURCES.md` became modified with a different three-row append.
The live snapshot had sha256
`ce2decba97bda64ed6cfb6529e52c5ced1f16c15a8dc51f0d6adb886ce0737ff`.
Across S123/S124/S129 it differed from the assigned draft in 16 cells, including S129
`tier: B -> A`, `recheck: 180d -> 90d`, and all three `used-by` cells. Both snapshots independently
compared clean against the committed base (120 -> 123 rows, zero breaches and zero permitted-cell
notes), so this is an evidence-identity issue, not an observed append-only breach.

Do not transfer this draft's census result or a future gate result on the live bytes from one
identity to the other. Materialize the chosen bytes, re-run census on those bytes, and run Q34 on
the commit that actually contains them.

No high-severity finding and no append-only/E03/E04 defect was found in the assigned draft itself.

## Contract results for the assigned draft

### (a) Existing protected cells are preserved in the pure-append world

I inserted the three exact draft rows immediately before `## Paths` in the committed base blob and
called the verifier's own `parse`/`compare` functions. Observed:

```text
draft-world: base-rows=120 rows=123 breaches=0 permitted-notes=0
```

`verifiers/check_sources_append_only.py:64-81` checks every existing row and every cell; only
`status`, `recheck`, and `used-by` are permitted in-place changes, and a removed row is a breach.
Thus the zero breaches answer the protected-cell question, and zero notes also shows that this
world makes no permitted-cell edits. The live working-tree snapshot separately produced the same
`breaches=0 permitted-notes=0` comparator result against the pinned base.

### (b) The real gate is conditionally clean, but has not been run on an append commit

For a commit range whose SOURCES changes are exactly this pure append, the supported command is
expected to exit 0 and print `0 protected-cell changes`. That is a code-and-comparator-backed
conditional result, **not** a claimed tip receipt: no commit containing the block existed at review
time, and the literal `--tip` command exits 2 as shown above.

The verifier scans each commit touching `corpus/SOURCES.md` in `base..rev`
(`verifiers/check_sources_append_only.py:99-118`). It does not grade an uncommitted append. The
reviewer must therefore use a nonempty range, inspect the diff, and paste the actual summary.

The comparator self-test was also run:

```text
$ python3 -B verifiers/check_sources_append_only.py --self-test
self-test: 0 failure(s) over 21 assertions
```

### (c) Census E03/E04 result and refusal behavior

The exact draft-world registry was validated with:

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-24 --file /tmp/kotoba-r67-ReviewAppendOnly.GPnkdk/pinned-draft/corpus/SOURCES.md
exit 0
```

Output was the 16 pre-existing W04 cross-scope warnings (S018, S019, S021, S054, S055, S056,
S065, S086, S103, S104, S106, S110, S111, S114, S115, S118), then:

```text
file	ok	/tmp/kotoba-r67-ReviewAppendOnly.GPnkdk/pinned-draft/corpus/SOURCES.md
```

There was no E03 or E04 and no new W04. S123/S124/S129 are distinct, unused ids relative to the
base, and their normalized URLs do not repeat a base `(URL, exact scope)` pair.

The refusal paths are real, not inferred from the clean run:

- **E03 duplicate id:** changing the sandbox S124 id to S123 produced
  `file E03 S123 duplicate id`, exit 1. E03 has no supersession exemption. Refuse the append until
  every id is unused; renumber in scratch and re-point every adopted citation by document, as the
  plan requires. Do not rewrite an existing row to make room.
- **E04 duplicate normalized URL within the exact same scope:** cloning S123 as otherwise-unused
  S125 with the same URL and scope produced the following, exit 1:

  ```text
  file E04 S125 duplicate url model-spec.openai.com/2026-08-18 within scope The normative authority ladder OpenAI trains against, tier=A for the ladder and the override rule only; this row makes no claim that the spec governs non-OpenAI clients, nor that any skill client implements it
  ```

  Refuse a redundant row. A genuine correction instead follows the contract's new-row
  `supersedes S0NN —` discipline; merely rewording `scope` to evade E04 is not a repair. A real
  different-scope reuse is W04, a warning rather than E04. The validator's exact conditions and
  non-rejected/supersedes exemptions are at `scripts/sources-census.sh:600-605,635-654`.

Fallback coverage from the initially absent draft: appending all 164 staged rows to the clean base
produced 284 parsed rows, zero comparator breaches/notes, and no E03/E04 in the canonical census
output. That as-is package nevertheless exited 1 on other census findings, so this is not an
adoption pass; the three transformed rows above are the reviewed candidate.

## Exact commands for the post-integration reviewer

Run from the lane root after the chosen block and its real `used-by` targets are committed:

```bash
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
base=2a8eba56b3f9321b70c569fa2816d42237ca49a2
tip="$(git rev-parse HEAD)"

# Prevent a vacuous base..base receipt and require the pinned base to be ancestral.
test "$tip" != "$base" &&
  git merge-base --is-ancestor "$base" "$tip" &&
  python3 -B verifiers/check_sources_append_only.py --base "$base" --rev "$tip"

# Inspect exactly what the range changes; do not hide permitted-cell notes.
git diff --unified=3 "$base" "$tip" -- corpus/SOURCES.md

# Census the real tree, so used-by paths are checked against real files.
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
  --root /home/vgpnk/Projects/shokunin kotoba

# Instrument control.
python3 -B verifiers/check_sources_append_only.py --self-test
```

For the append-only command, require exit 0, `0 protected-cell changes`, and a nonzero scanned
commit count; paste the observed line beside the full `tip`. For census, require exit 0 and inspect
that no `E03`/`E04` line appears; W04 alone does not fail validation. If the working tree is being
cited as tip evidence, also record `git status --short` and ensure the measured files match `$tip`.

## Residual risk and verification gaps

- No committed tip containing either candidate block existed, so Q34 compliance remains unclaimed.
- The sandbox copied the base corpus and `SKILL.md` and created an existence-only fixture at
  `corpus/knowledge/instruction-authority-ladder-round67.md` to isolate registry/schema behavior
  from unrelated E11s. Its exit 0 is not evidence of the knowledge entry's contents or admission;
  the production census command above remains necessary.
- This review covers append-only structure, registry parsing, and E03/E04 identity behavior. It
  does not re-open the three external sources or judge the prose, tier choice, quote fidelity, or
  the differing live row's S129 tier/recheck choices.
