# E07SkillPatchVerify — round 77 w1, kotoba (hyaku run 10, attempt 1)

Seat: `E07SkillPatchVerify` (executor, leaf; no subagents, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base (lane HEAD): `6523aced1ee0ebe07dca996213bdc645a6acbd1e` — `SKILL.md` 590 lines, tree clean in
a fresh `git clone --shared`.
Date: 2026-10-27. Host: linux 7.2.11-arch1-1.

Frozen counters are untouched by this seat and still match the plan's pins at lane HEAD:

- `verifiers/check_desc_craft.py` `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`
- `verifiers/check_r75_routed_repairs.py` `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`

## 1. Axes I worked (and the ones I refused to spend)

- **Depth (C1, the lowest owned axis)** — turn conjunct (c) from red to green *with the frozen
  counter's own predicate*: one § Body craft row that cites both the entry and S213 and carries
  quote fragments that occur verbatim, on one line, after the first heading of the
  optimizing-descriptions snapshot.
- **Consistency (C2 registry)** — both r76 counters get a registry row in the existing 8-column
  shape, so `check_gate_registry.py` can compare the lane's description of its gates with the
  files: base `60 of 62` (exit 1) becomes `62 of 62` (exit 0). This is the r76 row that never
  landed; the counters themselves are not edited.
- **Calibration** — every row I add states the *measured* target line of its counter and the
  pre-data base value, so a reader cannot mistake "gate exists" for "claim holds".
- **Operability** — the patch must not leave the lane in a state where a no-harm gate is red
  because of a dangling citation. This drove two concrete changes (below): the registry rows name
  receipt *files* under *existing directory* tokens instead of three not-yet-existing per-file
  paths, and the gate-registry row length was trimmed toward the house maximum.
- **Freshness** — not spent: no source row, no snapshot and no fetch is touched by this seat; the
  three snapshot digests are constants of the frozen counter and were only re-read.

Nothing was widened: no entry, no lesson, no LOG/SCORECARD row, no SOURCES cell, no counter, no
floor registry. Only `SKILL.md`, only in a scratch clone.

## 2. The r76 draft, verified rather than trusted

Source: `.ufo/waves/round-76/build/skill-patch.md` (B13, revised after B15Simplifier's D1–D2).
Each claim was checked against committed/fetched bytes; results:

| draft claim | measured result |
|---|---|
| body row insert after base line 216, before the blank line 217 | **true** (`| confirm discovery before trusting a path \| S224 quickstart \|` is the last Body craft row at 216; 217 blank, 218 `## Trigger-fidelity checklist`) |
| `### Body craft` heading line 205, unique `^#{2,4}\s+Body craft` match | **true** (exactly one heading; the counter's `section()` needs exactly one) |
| registry rows after the `check_sibling_reread.py` row, before the blank line and `## Sources` at 514 | **true** for the rows (base 512 → patch 514–515) |
| "`## Gate registry` stays line 448" | **false** — base **445**, patched **446** (the body row shifts it by one). Off by 3 in the draft. |
| budget box "base 285 → patched 286, text unchanged" | **true** (checklist detail: `593 lines within budget 600 (from box at line 286)`) |
| fragment 1 `Err on the side of being pushy`, page-unique | **true** — snapshot line **27**, after first heading (line 5); `grep -F` 0 hits in evaluating-skills and best-practices |
| fragment 2 `descriptions tend to grow during optimization`, page-unique | **true** — snapshot line **159**, page-unique |
| fragment 3 `Avoid adding specific keywords from failed queries`, "8 words", page-unique | **page-unique true, word count false** — snapshot line **157**, **7 words**, not 8 (the ≥5-word rule still holds) |
| row is 3 cells / 447 chars / 65 words | **true** as written (447 chars, 65 words) |
| the two Pin-2 registry rows are ready to paste | **false — they are truncated**: both end in `…` after the verdict cell and carry **4** cells, not 8 (no Self-test, Pinned values, Write scope, Owner). Pasted as-is, `check_gate_registry.py` pads the row and fails it (`self-test cell names no backticked flag`, empty pinned values, owner `''`), so the registry would stay red. |
| Pin-2 rows cite `.ufo/waves/round-76/receipts/r1-folded-render.txt`, `…/noharm-at-tip.txt`, `.ufo/waves/round-76/w2-registry-note.md` | **all three paths absent at base** (the C2 repairs they describe are exactly what is still open). `verify_skill_checklist.py` `trigger.citation_resolves` resolves every repo-rooted backtick token in `SKILL.md`, so landing those rows before those files is a new red (measured: probe A lists all four tokens). |

Defects I repaired in the delivered rows: the truncation (D-E07-1), the 448 anchor (D-E07-2 — a
reporting error only, nothing depends on it), the 8-vs-7 word count (D-E07-3), and the receipt
coupling (D-E07-4). D-E07-1/4 are the ones that would have cost the wave its operability gate.

## 3. Delivered rows (verbatim, from the patch file)

Body craft (line 217, one row, 3 cells, 447 chars / 65 words — the existing six rows' dense form):

```text
| write the description as an imperative about the goal, not the mechanics, and err pushy | S213 optimizing-descriptions; `corpus/knowledge/description-craft-round76.md` | "Err on the side of being pushy": list the contexts the skill serves, including ones the user never names; "descriptions tend to grow during optimization", so re-check length after each edit; "Avoid adding specific keywords from failed queries" — name the category instead. |
```

Gate registry, C1 row (line 514, 8 cells, 1447 chars):

```text
| `verifiers/check_desc_craft.py` | gate | `python3 -B verifiers/check_desc_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C1 counter (depth): committed bytes only, one verdict line per conjunct; (a) the three pinned pages under `.ufo/waves/round-76/snapshots/` with identical digests in `MANIFEST.sha256`, `fetch-record.json` (HTTP 200) and the in-file table, plus the round-76 lesson `## Gate` access record; (b) the entry `corpus/knowledge/description-craft-round76.md` carries at least four located quotes (at most 25 words), each verbatim on a cited line of the optimizing-descriptions snapshot after its first heading and page-unique against the other two; (c) `SKILL.md` section Body craft carries a row citing the entry and S213 with at least two located quote fragments; (d) the entry's audit table states the rendered `description` (clip 1022, stripped 1021 at the r76 base) and first-sentence (151) lengths the counter recomputes from the measured revision; (e) row S213's `used-by` lists the entry and the old and new values are logged in `corpus/lessons/round-76.md`; (f) the entry opens with `source:`, `verified-at:`, `recheck:`; `description craft backed 6 of 6` at the measured rev, `0 of 6` at the pinned base `2f67554` | `--self-test` | in-file; `.ufo/waves/round-76/snapshots/` | none (reads `git show <rev>:<path>`; a `--self-test` writes isolated fixture repos under `$TMPDIR`, removed) | kotoba |
```

Gate registry, C2 row (line 515, 8 cells, 1158 chars):

```text
| `verifiers/check_r75_routed_repairs.py` | gate | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-76 C2 counter (consistency): the four round-75 routed defects close on committed content — R1's appended correction in `corpus/lessons/round-75.md` plus the `r1-folded-render.txt` receipt under `.ufo/waves/round-76/receipts/` printing the folded render recomputed from the measured `SKILL.md` (clip 1022, stripped 1021); R2's `noharm-at-tip.txt` receipt under `.ufo/waves/round-76/receipts/` naming the r75 final tip `ac9f295` on its first line and recording green integrity/independent stdout and exit codes re-run at that exact revision, cited from LOG section Round 75; R3's `w2-registry-note.md` note in `.ufo/waves/round-76/` reconciling the R75Attack28 phantom with a machine-checkable excerpt, cited from LOG section Round 75; R4's LOG section Round 75 closing line appended after the pending text; `r75 routed repairs closed 4 of 4` at the measured rev and `0 of 4` at the pinned base | `--self-test` | in-file | temporary clone and gate re-run dirs under `$TMPDIR` (removed) | kotoba |
```

Shape checks: 8 cells in file order (`Name | Kind | Entry command | Verdict map | Self-test |
Pinned values | Write scope | Owner`), verdict map declares `0=clean` and `1=failed` once each and
`2=could-not-evaluate` once; `--self-test` is an exact `add_argument` in both counters; pinned
values are `in-file` plus a token that is a directory in the tree; write scope non-empty; owner
`kotoba`. Registry rows are 1447/1158 chars against a house median of 314 and a previous maximum
of 1095 (`check_spec_craft.py`) — 202/154 words. The C1 row was trimmed from 1620 chars in the
first revision; the remaining size is the six-conjunct verdict map, not padding.

## 4. Measurements (each gate's own exit status, never a pipeline)

Harness: `/fast/scratch/hyaku/kotoba-r77/E07SkillPatchVerify/run.sh`, `evidence.sh`; every gate is
run directly and its `$?` captured immediately. Scratch clone per revision, `git clone --shared`
from the lane, `user.name scratch-r77` / `user.email scratch@example.invalid` set before the first
commit, `git rev-parse --show-toplevel` asserted equal to the clone dir before that commit, every
git call `-C`-qualified. The clone sits at `<sandbox>/kotoba-shokunin` inside a fleet-shaped
directory of symlinks to the fleet root (minus `.git`, `.jj`) because
`verify_skill_checklist.py` resolves `../` citations from the parent.

| gate | base `6523ace` | patched `a051f52` (this patch only) |
|---|---|---|
| `check_desc_craft.py --repo … --rev …` | `description craft backed 0 of 6`, **exit 1** — `(c) no Body craft row cites both corpus/knowledge/description-craft-round76.md and S213` | `description craft backed 1 of 6`, **exit 1**, `(c) act-on: pass`; (a)(b)(d)(e)(f) still fail on the entry/lesson absent |
| `check_gate_registry.py --rev …` | `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, **exit 1** | `… conformant 62 of 62 …; phantom 0`, **exit 0** |
| `verify_skill_checklist.py --repo … --json` | **exit 1**, 10 pass / 1 fail: `governance.citation_resolves` | **exit 1**, 9 pass / 2 fail: `trigger.citation_resolves` + `governance.citation_resolves` |
| `check_spec_craft.py --repo … --rev …` | `spec craft pages backed 3 of 3`, exit 0 | `spec craft pages backed 3 of 3`, **exit 0** (no regression from a seventh Body craft row) |
| `wc -l SKILL.md` | 590 | **593** (budget 600; box moves 285 → 286, text unchanged) |

So the patch **turns conjunct (c) green** and **turns the gate registry green (60/62 → 62/62)**,
and it **adds one checklist fail whose fix is a landing order, not a text edit** (§5.1).

## 5. The reds, with the exact fix

### 5.1 Patch-caused, and it is a landing order (measured)

`verify_skill_checklist.py --json` at a revision that holds the patch but not the claim data:

```text
trigger.citation_resolves  FAIL
  line 217: 'corpus/knowledge/description-craft-round76.md' does not resolve …
  line 514: 'corpus/knowledge/description-craft-round76.md' does not resolve …
  line 514: 'corpus/lessons/round-76.md' does not resolve …
```

**Exact fix: land `SKILL.md` in the same commit as (or after) `corpus/knowledge/description-craft-round76.md`
and `corpus/lessons/round-76.md`.** Both files are already required by C1 conjuncts (b)/(f) and
(a)/(e), so this adds no file to the touch list — it only forbids a "SKILL.md first, data later"
commit split. Measured: probe D (patch + those two files, no C2 receipts) gives checklist **exit 0,
11 pass**; probe F (same + the two draft corrections + the S213 `used-by` append) gives
`description craft backed 6 of 6`, **exit 0**, checklist **exit 0**, registry **62 of 62, exit 0**.

The delivered C2 row names its receipts as bare filenames under existing directory tokens
(`.ufo/waves/round-76/receipts/`, `.ufo/waves/round-76/`), so the three C2 repair artifacts are
**not** prerequisites for landing `SKILL.md` — C1 and C2 can still land as two commits. The r76
draft's per-file paths would have forced a single combined commit (probe A measured four dangling
tokens).

### 5.2 Pre-existing at base, not caused by this patch (routed finding)

`governance.citation_resolves` is red at the r77 base, in a pristine clone **and** in the real lane:
`LOG.md:2818` points at `` `.ufo/reports/round-76/kotoba.md` `` (a *fleet-root* report) with the
lane-rooted form. Resolved from the lane root it is dead; the file exists at
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md` (8128 bytes, 15:35 today).

**Exact fix (measured):** write the pointer as `` `../.ufo/reports/round-76/kotoba.md` `` — the
fleet lane-report convention `citation_resolve()` supports (≤3 `..` hops). Probe B shows
`governance.citation_resolves` PASS with that one token changed; probe D/F then reach checklist
exit 0. Alternative if editing an existing LOG line is refused: append a round-77 correction notice
(the `GOVERNANCE_CORRECTIONS` mechanism) — but that means editing `verify_skill_checklist.py`'s
in-file table, a bigger change than a one-token pointer fix. Note the fragility either way: the
lane's older `.ufo/reports/round-NN/` directories are untracked in git, so this check passes only in
a working tree that holds them.

This also contradicts the r76 plan's § Base battery line ("checklist `pass 11` exit 0") for the r77
base — the r76 integration commit `2f67554` added the pointer after that battery was taken. The L1
should record `verify_skill_checklist.py` as red at base in the wave receipt rather than green.

## 6. What this seat does not claim

- Not C1. `description craft backed 1 of 6` at the patched commit, `6 of 6` only in a scratch probe
  built from unverified r76 drafts plus two corrections I made there. The K=6 measurement belongs to
  the lane commit after the L1 integrates the entry, the lesson and the S213 `used-by` append.
- Not C2. Zero of the four repairs is read, written or scored here; the C2 row is documentation of
  the frozen counter, and `check_r75_routed_repairs.py` is untouched.
- No source, snapshot, fetch, census or floor change. No FORECAST/SCORECARD/LOG/QUALITY edit. No
  git or jj write outside the scratch clone.

## 7. Two draft defects surfaced for the seats that own those files

Found while probing the landing (reported, not fixed in the lane — outside my file scope):

1. **`lesson-draft.md`, § Gate located quote.** The quote is written as
   `` "`A few sentences to a short paragraph is usually right`" ``. `check_desc_craft.py` captures
   the span between the double quotes *including the backticks*, then requires it to occur on one
   collapsed snapshot line — it never does, so conjunct (a) fails with
   `the lesson Gate carries no <=25-word quote located in the optimizing-descriptions snapshot`
   (measured: probe D, 4 of 6). Dropping the inner backticks makes
   `"A few sentences to a short paragraph is usually right"` a located, page-unique quote
   (snapshot line 28) and conjunct (a) passes (probe E: 5 of 6).
2. **`plans/round-76.md` § Base battery** claims the checklist was green at base; it is not (§5.2).

Probe F reaches 6 of 6 once (1), the S213 `used-by` append and this patch are all present — so C1's
remaining work is exactly the entry, the lesson and the SOURCES append, with no further `SKILL.md`
change.

## 8. Tooling

No install, upgrade or download of any kind. Nothing under `~/.local/bin` or any other PATH entry
was created or modified; `pacman` was not invoked. Python 3 from the host, `git` from the host.

## 9. Files

Written to the lane (both under `.ufo/waves/round-77/build/`):

- `E07SkillPatchVerify.skill.patch` — unified diff (`git diff 6523ace… a051f52… -- SKILL.md`),
  3 insertions, 0 deletions; `git apply --check` against a pristine base clone: exit 0.
  sha256 `1122809b94aec086a98fedfce5bea85b00f95c35346aaee939c0f570bd1463dd`.
- `E07SkillPatchVerify.gates.txt` — every command, its full stdout and its own exit status for the
  base run, the patched run and the six mechanism probes; 20,173 bytes, sha256
  `8f7316596666fb27daf04ba2e3cadd5ac8d00d7759ec9b8cfef3810252d2683c`.

Scratch (`/fast/scratch/hyaku/kotoba-r77/E07SkillPatchVerify`, six clones/sandboxes) is removed
before yielding; the gates file is self-contained, so no receipt depends on it.

VERDICT: SKILL.md patch verified and delivered — conjunct (c) red→green at the patched commit, gate registry 60/62→62/62 exit 0, SKILL.md 590→593 lines, no axis harmed; the one patch-caused checklist fail is a landing-order requirement (entry + `corpus/lessons/round-76.md` in the same commit) and the one pre-existing red is LOG.md:2818's lane-rooted fleet-report pointer, with the one-token fix measured.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E07SkillPatchVerify.skill.patch /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E07SkillPatchVerify.gates.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E07SkillPatchVerify.md
