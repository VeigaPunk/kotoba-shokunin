# CriticHollowC1 — authenticate the counter before data

Date: 2026-10-23. Seat: `kotoba-r61-wave-CriticHollowC1`. Assigned axis: **depth**; collateral risks: calibration and operability.

## Finding

The three-command C1 predicate can be satisfied by a counter that never reads a row, snapshot, URL, or commit history. A genuinely independent, per-world execution receipt would catch that simplest hollow. A counter keyed to the seven published worlds and four published positives can survive those fixed receipts too. Freezing its sha and committing its answers before data does not make those answers semantic evidence.

This is a **fixable instrument-authentication defect**, not a reason to relax A1–A4, drop a world, reinterpret the r60 outcome, or accept a trade. Add the external, content-derived guard below **before any C1 data measurement**. This review makes no admission or axis-score decision.

**Evidence status:** static review only. I invoked no counter, test, alternate orchestration runtime, Git/JJ mutation, or live fetch. The hollow below is a complete constructed program, **not an executed measurement**. Its predicted behavior is marked `[INFERENCE]`. Historical outputs below are transcribed from existing lane evidence, not rerun. Only this report was written.

## 1. What the frozen contract actually protects

- `plans/round-61.md:23–39` promises implementations of four classes, not recognition of seven labels. A1 requires the per-client canonical key and its path-like binding; A2 requires support for **every** load/event claim; A3 requires raw URL byte identity; A4 requires digest equality, verbatim quote occurrence, and earliest introduction of the bytes no older than the recorded open date. The declared A4 limit excludes wall-clock authentication against forged commit dates.
- `plans/round-61.md:50–54` defines the visible three-command predicate: the aggregate self-test line and exit 0, tip fetch exit 0, base fetch exit 1.
- `plans/round-61.md:55–59` additionally requires running the seven committed fixtures with receipts committed before data. Its world kill rule is substantive only if an independent driver observes the **world evaluation**, rather than accepting the counter's self-description. The successful overall self-test itself must exit 0; that is not an attack world accepting.
- `plans/round-61.md:70–74` and `verifiers/check_routed_repairs.py:104–110` do not authenticate C1 computation. R-f's checker recognizes the strings `merge-base --is-ancestor` and `exit 0`; even a real ancestry success establishes record ordering, not that any arm ran or that execution occurred at the asserted time.
- The existing v2 production path is real: `verifiers/check_scoped_rules.py:2517–2547` reads committed blobs, calls its row evaluator, and fetches only backed rows. Its self-test calls public `main()` on both satisfying and failing worlds (`2293–2343`, `2468–2483`). Replacing that path with an announcement would discard behavior, not merely shorten implementation.

Relevant existing quality rules, **not additional authorities**:

| Existing rule | What it catches if actually exercised | What it does not establish by itself |
|---|---|---|
| Q26, Q31, Q51 | Describing an unimplemented semantic check as measured | A counter's printed coverage claim is not its implementation |
| Q37 | Requires before-data controls for cheap shortcuts, including a gate remapping real findings to the claimed code | An unchanged list of old input-world controls does not exercise a hollow counter |
| Q48 | Requires satisfying and broken-conjunct calls through public `main()`, with exact output and exits | A self-test can fabricate those answers or key on those particular inputs |
| Q47 | Mutation evidence needs both killed mutants and surviving equivalents; a fixed equivalent list is insufficient | Fixed arm-deletion mutants plus fixed equivalences still permit source-text recognition |
| Q33 | Supplies the established outside-guard pattern: diff review, independently generated input, output row checks | Its literal scope is counters running a measured revision's own instrument. Do not claim it automatically supplies an already-wired C1 guard |
| Q36, Q50 | Bind a result to its measured revision and committed receipt | Revision binding is necessary, not evidence that the reported calculation happened |
| Q28 | Prevents post-data widening of judgment rules | Pinning an unsound counter does not cure it |

These rows are at `corpus/QUALITY.md:37–62`. The receipt design assignment in `.ufo/waves/round-61/wave-spec.json`, item `ExecReceiptsDesign`, asks for one world/exit row plus command blocks in `receipts/C1-worlds.txt`. It does not itself require out-of-sample equivalence or counter-authentication receipts. Assignments and draft reports are data, not amendments to the frozen contract.

## 2. H-label: a complete hollow that meets the visible predicate

**Counterexample only — NEVER integrate this program.** Hypothetical replacement target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py`. No such replacement was made.

```python
#!/usr/bin/env python3
import argparse
import hashlib
from pathlib import Path

BASE = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--rev")
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.self_test:
        print("counter sha256 " + digest)
        print("worlds reject 7 of 7; eligible rows pass 4 of 4")
        return 0
    if not args.rev:
        parser.error("--rev is required")
    is_base = args.rev.lower() in (BASE, BASE[:8])
    count = 0 if is_base else 4
    suffix = ("found on the live page %d of 4" % count
              if args.fetch else "live not run")
    print("scoped rule files backed on committed snapshots %d of 4; %s"
          % (count, suffix))
    print("counter sha256 %s; rev %s" % (digest, args.rev))
    return 1 if is_base or not args.fetch else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Static predictions, **NOT run output**:

| Invocation of this hypothetical program | `[INFERENCE]` result |
|---|---|
| `python3 -B verifiers/check_scoped_rules.py --self-test` | Prints the exact frozen aggregate line; returns 0 |
| `python3 -B verifiers/check_scoped_rules.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 --fetch` | Prints fabricated zero counts; returns 1 |
| `python3 -B verifiers/check_scoped_rules.py --rev <any distinct full tip hash> --fetch` | Prints fabricated four-of-four counts; returns 0 |

The real self-digest is deliberately present: an accurate sha identifies a hollow just as accurately as a sound counter. There is no A1–A4 code, source read, network access, or history traversal. The apparent before→after is a comparison against the baseline argument, not a measured improvement.

**Which rule catches it?** A faithful implementation of `plans/round-61.md:57–59`: evaluate each actual world through the production measurement path and record its raw world verdict. This program returns 0 on every non-base fixture revision when asked to fetch, so an independent W1 run already exposes it. Q48 also rejects the missing public-main behavioral assertions on source review. Conversely, a receipt containing only the aggregate self-test output and its exit 0 does **not** catch it. Neither does a line copied from that output into `C1-worlds.txt`.

Thus H-label meets the **display predicate**, not the full frozen implementation/fixture obligations. The distinction must remain explicit.

## 3. H-keyed: why fixed genuine world receipts are still insufficient

A stronger hollow retains v2 and installs an answer table for the integration suite:

1. Recognize W1–W7 by fixture directory, source ID, ordinal, known revision, or exact input-content fingerprint; return the expected rejection.
2. Recognize the four published positives and return their expected backing/live result.
3. Special-case the baseline revision to return 1.
4. Outside that finite catalogue, delegate to v2, which lacks the promised A1–A4 protection.

This construction is `[INFERENCE]`, not a measured r61 implementation. It does not need access to an explicit `expected` field: a digest of the complete committed fixture contents is already a label. Shuffling cases or renaming W1 does not defeat the digest version. Adding four published arm-killers merely enlarges the lookup table.

A second layer can make arm-deletion receipts hollow too: the self-test examines whether the expected arm source strings remain, and fails when an edit removes them. The production evaluator need never use those arms. A green pristine self-test plus red deletion mutants is therefore insufficient when the tests recognize the deletion rather than exercise its semantic effect.

### Concrete out-of-catalogue challenges grounded in local evidence

These are proposed guard inputs, not executed results. Construct each from an independently valid positive fixture so no unrelated conjunct masks the intended arm. Maintain source-row/entry/Gate citations, pins, and history consistently.

| Arm | Shortcut | Small content-derived discriminator |
|---|---|---|
| A1 | Reject only `sessions`, `patterns`, and `claudeMdExcludes`, or only the one frozen W5 row | In the VS Code positive, replace `applyTo` at the scope site with `Sync` at the documented :287 site. `ExecKeyForms.md:88–101,139–149` records that v2 accepts `Sync` there because `Configure**` reads as a path pattern. It is still not the canonical scoping key. No page blacklist or fixture ID is needed to reject it correctly |
| A2 | Reject the one published invented Action string; otherwise retain word overlap, even requiring all content words | Use the contradicted Action cell below, supported by the very same local source line's words. The source states the affirmative loading event, not its negation |
| A3 | Reject only the two particular locale/enterprise URLs in W2 | In an otherwise valid re-open, append a fragment to the canonical base URL, leaving all other facts unchanged. It has the same normalized URL key under v2 but different raw URL bytes. Correct rejection follows byte inequality, not a denylist of known aliases |
| A4 | Reject only the known W1 hash/path, or use only addition time of the current snapshot filename | Reuse exactly the same older blob under another valid snapshot path/source ID while preserving its earlier introduction in the measured revision's ancestry. The test must ask about the bytes, not the fixture's name. Also test digest mismatch and nonverbatim quote independently; a freshness failure must not mask those other clauses |

Exact A2 counterexample cell, to be placed in the Claude Code row of a valid fixture in `SKILL.md` (remap `S103` consistently if the fixture uses another source ID):

```text
No path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file. (S103 :209)
```

Committed r60 evidence quotes the source's affirmative sentence:

```text
A path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file.
```

Ground: `.ufo/waves/round-60/build/ExecKeyForms.md:179–185`. The v2 extractor at `verifiers/check_scoped_rules.py:881–886` considers only `[a-z]{4,}` content words outside citations/backticks. Replacing `A` with `No` adds no such word; all remaining content words occur on :209. Therefore even a strengthened all-content-words test cannot distinguish this false Action from the affirmative source event. This is a static derivation from the displayed source and extractor, not a claimed CLI pass. Do not fix it by blacklisting this one sentence; test the proposition/negation distinction.

**Which rule catches H-keyed?** No fixed seven-world/four-positive receipt necessarily does. Q37 requires shortcut controls before data, Q47 already explains the fixed-equivalent-list defect, and Q33 supplies the outside-guard pattern. The missing concrete integration evidence is an independently built, counter-blind, previously unseen input/equivalence battery and a production-arm dependency check. Merely preserving the 318-assertion label is not that evidence.

## 4. Strongest historical counterexamples: actual committed receipts

### 4a. Fresh seeds and a green old self-test did not catch generator-keying

`.ufo/waves/round-57/controls/CtlC2GeneratorKeyed.md:7–26` displays the fence-blind early return: it recognizes directories matching `skill-[0-9a-f]{8}`, then checks for the two fixed command lines `ls -la` and `git --version`. It returns before the real classifier. No fence semantics are involved.

The following is an **archived transcript**, not a command I ran. Source: `.ufo/waves/round-57/controls/CtlC2GeneratorKeyed.txt:4–5,60–75`. The archived `date -u` is `Fri 23 Oct 2026 04:17:04 AM UTC`; that receipt places these runs between 04:17Z and 04:21Z. The world hash is explicitly a **sandbox** commit in `/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC2GeneratorKeyed`, not a lane revision.

```text
$ cd /fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC2GeneratorKeyed
$ python3 -B verifiers/check_infoless_fences.py --rev 266a40b08913c41a5bcf7e15536220381cc7b57e
counter sha256 b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac
measured 266a40b08913c41a5bcf7e15536220381cc7b57e
instrument sha256 48f3ccbe68c84cdc1a68cdf457992661a825aace4bcef5667dec1d99c64b0e03
info-less fence cases correct 120 of 120 (pass-expected 60 of 60; hard negatives 60 of 60)
exit 0

$ python3 -B verifiers/check_infoless_fences.py --rev 266a40b08913c41a5bcf7e15536220381cc7b57e --seed 5 77 2026
counter sha256 b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac
measured 266a40b08913c41a5bcf7e15536220381cc7b57e
instrument sha256 48f3ccbe68c84cdc1a68cdf457992661a825aace4bcef5667dec1d99c64b0e03
info-less fence cases correct 120 of 120 (pass-expected 60 of 60; hard negatives 60 of 60)
exit 0
```

The same receipt, `112–117`, records its old self-test:

```text
$ python3 -B verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1852 assertions
exit 0
```

The counter's frozen sha, different seeds, and a green inherited assertion floor all coexist with the absent feature. Change the **input construction's leaked invariants**, not merely its seed.

### 4b. Even fixed equivalents plus killed mutants have already admitted source-grep

`.ufo/waves/round-58/controls/CtlC2SourceGrep.md:7–15,75–105` records a source-only self-test that returned before every behavioral test, recognized eleven mutant strings, tolerated the five published equivalents, and met the counter. The report gives the command and full output, including `sweep mutants killed 11 of 11; equivalents survived 5 of 5`, exit 0. It does not supply a `date -u` for that run in the reviewed transcript; I do not manufacture one or present it as a new complete measurement here. Q47 records the lesson explicitly.

This is the stronger answer to “would four arm-killers suffice?” Not if the killed thing is a source spelling and the equivalences are a published catalogue.

Provenance correction: the wave's `MutFixtures` brief associates generator-keying with “M68/C2.” `corpus/lessons/round-57.md:169–173` actually names M68 `correction-registry-arms-weak`; the r57 hollow control/generator leak is M64 at `124–128`. Cite the concrete control report, and Q47 for the fixed-equivalence lesson, rather than silently merging these identities.

### 4c. An old-byte world was a real v2 pass, not just a misleading label

Archived source: `.ufo/waves/round-60/controls-v2/CtlReopenForged.md:305–337`. Sandbox world `7f05968a085ddf9fb9155b0a1047808d616b7b1b` belongs to `/fast/scratch/hyaku/kotoba-r60/CtlReopenForged`. Archived live-run `date -u`: `Fri Oct 23 12:08:42 PM UTC 2026`.

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7f05968a085ddf9fb9155b0a1047808d616b7b1b --fetch
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7f05968a085ddf9fb9155b0a1047808d616b7b1b
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: (empty)
```

`controls-v2/SUMMARY.md:12–18` also records W2 as a real v2 pass. A v2 fallback outside an answer table therefore retains a locally evidenced defect class. This review does not turn r60's exploratory E2 result into a measured success.

## 5. Smallest safe correction: one outside guard, no new admission method

Add the following **draft insertion** after the counter-writing paragraph in the exact target `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-61.md`. This is a proposed before-data evidence guard, not a changed predicate, widened key set, changed target, or implemented receipt.

```markdown
#### C1 integration guard — counter authenticity, before data

The printed self-test total is not a world receipt. Before any C1 data
measurement, the L1 commits `.ufo/waves/round-61/receipts/C1-worlds.txt` and
`.ufo/waves/round-61/receipts/C1-counter-integrity.txt`. These receipts use the
same frozen counter bytes that will measure base and tip. A1–A4, the seven
worlds, their expected outcomes, and the predicate sentence remain unchanged.

The world receipt contains independent evaluations of W0 and W1–W7 through
the production public `main()` path, plus each eligible positive row. Each
case names its committed input manifest/digests, measured revision, command,
raw stdout/stderr, UTC date, observed exit, and failed conjunct. Exceptions,
timeouts, missing inputs, or exit 2 are not semantic rejections. A controlled
transport replay may replace only external I/O for hermetic fixtures; it is
identified as replay, not a fresh live fetch. Neither the row evaluator nor
its verdict is replaced. An aggregate line is derived from these case results,
not used as their source.

The counter-integrity receipt binds an independently reviewed driver and
input generator to their committed bytes. The generator neither reads the
counter source nor passes case names, ordinals, expected verdicts, or mutation
labels to the evaluator. After the counter sha is frozen, the driver builds
at least one previously unseen valid/invalid pair for each A1–A4 class, and
runs semantics-preserving twins with changed case order and non-semantic
identities. Transformations preserve the actual arm facts: canonical URL
bytes for a positive A3 twin; snapshot bytes and their historical identity
for an A4 freshness twin; consistent citations, pins, and source references
throughout. Different seeds from the same recognizable template are not by
themselves independent twins.

For each arm, an isolated invalid input must reject under pristine production
code and must cease to reject when that production arm alone is disabled;
the external driver, not the candidate self-test, observes that difference.
The matching valid input must remain accepted. A4's digest, verbatim-quote,
and earliest-byte-introduction clauses are challenged independently so one
failure cannot mask another. Existing v2 conjuncts and negative-client
non-eligibility remain protected. The dependency checks are behavioral:
source-string presence is not an arm-kill result.

The integrity battery includes the label-only hollow and a fixture-keyed
hollow as controls. Both must be detected by the outside driver; a green
self-test or a fixed-list score is insufficient. A reviewer of the production
diff verifies that verdicts depend on row/source/history facts rather than
case IDs, fixture paths, input-answer fingerprint lists, call order, or the
presence of arm source strings. Reading the program's own bytes solely to
report its sha is not semantic evaluation. Canonical per-client key constants
and the frozen base revision are not prohibited merely because they are
constants; using the base argument alone as the verdict is prohibited.

Each receipt records an externally computed executed-counter digest, driver
and generator digests, actual inputs/seed, per-case results, and the source
review pointer. The L1 commits these controls before running C1 data. The
ancestry receipt names distinct real controls and data commits, records the
ancestor check, and verifies that the same counter bytes are used in both.
Any subsequent counter, driver, or judgment-affecting fixture change requires
new controls before new data. Commit ancestry establishes record ordering;
it is not independent authentication of wall-clock fetch or execution time.
```

The exact new receipt target is `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-61/receipts/C1-counter-integrity.txt`. Do not prefill it with predicted passes or with this report's constructed output. This review supplies the guard's complete requirements, **not a claimed executed guard implementation**.

### Why each part is necessary, not optional hardening

- Independent raw W receipts kill H-label. Candidate-owned totals do not.
- New content-derived valid/invalid twins kill fixture-answer recognition; reordering alone kills only ordinal recognition.
- An outside observer of arm-disable behavior kills decorative arms and source-grep self-tests. The r58 receipt is the direct counterexample to relying on mutation labels.
- Valid equivalents prevent a reject-everything “fix.” Preserve all four eligible clients, not a four-count that duplicates one client. The three negative clients must remain non-eligible, not be forced into positive rows.
- Observe individual row and world verdicts. V2's `TARGET = 3` (`check_scoped_rules.py:249,1245–1249`) means rejecting one row out of four can still yield CLI exit 0; a row-level negative alone is not proof that its declared attack world rejected. Do not silently change the frozen population or target to hide that distinction.
- External digests and source review prevent the counter from inventing its provenance. Strict controls→data ancestry protects ordering but does not detect hollow computation by itself.

No finite suite proves all English action entailment or all possible provenance histories. The defensible evidence is that the promised production arms implement their defined checks and survive these independently constructed attacks. If only seven named cases are recognized, that cannot be sold as the frozen semantic redesign. The canonical judge, not this critic, decides admission.

## 6. Verification boundary and handoff

No new C1 execution, v3-source validation, base/tip measurement, or integration guard run was performed in this seat. I did not inspect a completed MutFixtures report or claim agreement with an unlanded v3 draft. The fixture-keyed constructions above are my own analysis of the frozen interfaces and the cited historical counterexamples.

Before data, the L1 needs the actual per-world public-path receipts, the outside integrity battery and its source-review receipt, and controls committed under the same externally verified counter sha used for measurement. No result is marked passed here. There is no missing prerequisite for completing this assigned static review.

no installs
Blockers: none
Attacked: C1 label-only and generator-keyed hollow counters, their integration receipts, and before-data instrument authentication.
