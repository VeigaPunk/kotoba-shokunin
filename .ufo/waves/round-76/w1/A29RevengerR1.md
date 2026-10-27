# A29RevengerR1 — does the R1 correction quote the superseded bytes, and does the folded render really read 1022?

VERDICT: R1's two halves hold on the bytes I could measure — the drafted correction quotes both superseded strings byte-for-byte (full 793-char M75-1 row identical, Gate reject sentence identical, base prefix unchanged), and the yaml folded render of the whole block reads **1022** (clip) / **1021** (stripped) at the r75 tip `ac9f29510d3914a6edb97c8dbdb3445cab9141de` and at all three neighbours; but R1 is **not closed at observation time**: neither `verifiers/check_r75_routed_repairs.py` nor `.ufo/waves/round-76/receipts/r1-folded-render.txt` exists yet, and the correction cites both. One design hazard is live and demonstrated below: a whole-file containment check for the superseded text is green at the base commit, so the R1 arm must be scoped to the appended bytes.

Observed at lane `eab64394dba08a47f6797a2e23719be14675b44b`, 2026-10-27T14:06:44-03:00. Report only; no lane file was written by this seat.

## Axes

Consistency (the r75-closure axis R1 repairs), calibration (exactness as a measurable property, not an adjective), coverage (four revisions, both slice conventions, five mutant worlds), operability (a 7-arm red/green conjunct any closure can run), adjacency (the 1021-vs-1022 convention is live in `check_sibling_census.description_of`; C1 conjunct (d) inherits the same off-by-one and a second, unclosed convention for the first sentence).

## 1. The superseded bytes, as committed

Both strings live in `corpus/lessons/round-75.md`, whose bytes are stable at every revision in scope: sha256 `7f260fd517495ffa680f0088f0e1dd17906fe562fe2158dbffa6807e79d57db6`, 2,161 characters / 2,175 bytes, at `ac9f2951`, `b7f13f4b` and `HEAD` (verified by `git show <rev>:corpus/lessons/round-75.md | sha256sum`). The file does not exist at `65a5c7a6` (`git show` empty).

**M75-1 row — line 11, 793 characters, sha256 `884c20c3fd609c32de5f28940902b956336e57dcbd392a9c2f7c9cf884b97dea`:**

```
| stale-premise | `considerthese/2026-10-26.md:17` says description is 1,021/1,024 characters; current committed SKILL frontmatter (master 65a5c7a, lines 3–18) is substantially shorter; direct `awk 'NR>=3&&NR<=8{print NR ":" length($0) ":" $0}'` yields 14,76,78,73,79,72 for frontmatter lines 3–8. | Q67 (read proposal against actual file contract) does not catch stale values; corpus Q54/Q60 require reproducible counts and revision-addressed evidence, but no current criterion catches a proposal's imported observation | Freeze each proposed target from the current committed bytes and rerun its counter before plan freeze; classify historical proposal numbers as historical, not as round baseline. This lesson-only repair is not claimed as a guard until a failing fixture demonstrates it. |
```

Superseded clause inside it (202 chars, sha256 `113f90d8207a5382d6e07f3ae5556487839c51852e43a30aeeb44d9d494d3c7e`):

```
current committed SKILL frontmatter (master 65a5c7a, lines 3–18) is substantially shorter; direct `awk 'NR>=3&&NR<=8{print NR ":" length($0) ":" $0}'` yields 14,76,78,73,79,72 for frontmatter lines 3–8.
```

**## Gate reject candidate — line 5, sha256 `efed322fe5423274345494ce88c4c36feaecb003b4b579b06173ed9568f35f67`; the sentence (170 chars, sha256 `30549f47f63fb6fb5dfa5d1e99cd9cf93d4a7c8be5236d79e5d3ecf76b648acf`):**

```
Candidate reject: any claim that the 1021-character description size reported in `considerthese/2026-10-26.md` remains current; current frontmatter is materially shorter.
```

Drift surface: the row carries one non-ASCII character, U+2013 EN DASH in `lines 3–18` (206 UTF-8 bytes for 202 characters), four ASCII `"` and two backticks; the Gate sentence is pure ASCII with two backticks. A correction that normalizes the dash, curls the quotes, or truncates with `…` is readable but not byte-equal (QUALITY Q56: `byte-exact` is literal).

## 2. The correction draft, tested against those bytes

Draft: `.ufo/waves/round-76/build/B08-r1-round-75-correction.diff` (sha256 `95c96cd4c95a8cfeb0acc87df4bda0a479a08bfc2e6c6bf69ab11d83b5943282`), applied in scratch to the committed base copy (sha256 `7f260fd5…`, `patch -p1` exit 0, dry-run exit 0). Applied result sha256 `703f56126807c84a7edc08fd1b71ca86993a93b75aee7a0228a71b9417b54a6e`; appended tail 4,659 characters / 4,702 bytes, sha256 `c57e41e3d9cb50f4a9798a3e36e13e6dafad8623f0a75fcda3d798687007daae`.

| arm | result |
|---|---|
| append-only: applied file starts with the 2,175 base bytes | PASS (byte-identical prefix, `startswith` on bytes) |
| M75-1 row premise clause appears verbatim in the tail | PASS (202/202 chars) |
| Gate reject sentence appears verbatim in the tail | PASS (170/170 chars) |
| full M75-1 row appears verbatim (4-space-indented copy) | PASS — copy line is 797 chars = 4 spaces + 793; stripped copy `==` committed row with zero `difflib` opcodes |
| correction's own "closed on" fragment `This lesson-only repair is not claimed as a guard until a failing fixture demonstrates it.` | PASS verbatim in the row and in the tail |
| tail names `:11` and `:5` for row and Gate | PASS (both line numbers correct on the committed file) |
| prose row fragment (166 chars, before `; direct \`awk…\``) | PASS verbatim substring of the committed row |
| `plans/round-75.md:15` quote (158 chars) | PASS verbatim against `git show b7f13f4:plans/round-75.md` line 15 |
| `considerthese/2026-10-26.md:17` quotes `still 1,021 of 1,024 chars` (26) and `about 150 chars` (15) | PASS verbatim against committed line 17 |
| commit ids `65a5c7a663249e…`, `ac9f29510d39…`, `4de12b61f75c…`, `b7f13f4b39cb…` | PASS, all `git rev-parse --verify <id>^{commit}` resolve |

No divergence was found between the correction's quotations and the committed bytes. The elision in the first paragraph (row's opening clause, then the row's closing clause, joined by narrative with no `…` inside the quotation marks) is a style point, not a byte defect: the complete row follows 22 lines later under the sentence "The superseded row, verbatim".

## 3. The method fix: the folded render really is 1022 at the r75 tip

My seat's named revision is `ac9f29510d3914a6edb97c8dbdb3445cab9141de`; `git show ac9f295:SKILL.md` in scratch is 590 lines, sha256 `7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a`.

```
$ git show ac9f295:SKILL.md | python3 -c "import sys,yaml;d=yaml.safe_load(sys.stdin.read().split('---')[1])['description'];print(len(d),len(d.strip()))"
1022 1021                     # exit 0
```

Layout and arithmetic at the same revision (recomputed, not quoted):

| assertion in the correction | measured @ `ac9f295` | measured @ `b7f13f4` |
|---|---|---|
| marker line 3 is `description: >` | OK (14 chars, `>` = clip) | OK |
| content lines 4–18, closing fence 19 | OK | OK |
| raw sum of lines 4–18 = 1,037 | OK | OK |
| − 30 indent + 14 join spaces = 1,021 | OK (1,007 + 14) | OK |
| clip render = 1,022; stripped = 1,021 | OK | OK |
| window `NR>=3&&NR<=8` = `14,76,78,73,79,72`, sum 392 | OK | OK |
| first sentence = 151 characters | OK (`.strip()` then `split('. ')[0]+'.'`) | OK |
| description identical at `65a5c7a6`, `ac9f2951`, `b7f13f4b`, `4de12b61` | OK (all four: 1022/1021, fence 19) | OK |

Slice conventions the correction claims, tested directly (not inferred):

```
split("---")[1]        -> clip 1022, stripped 1021     # the correction's command
split("\n---")[0]      -> clip 1021, stripped 1021     # drops the clip newline
'\n'.join(lines 1..18)+'\n' -> clip 1022, stripped 1021
```

So "the method fix (yaml folded render, whole block) produces 1022" is true at the tip under clip chomping, and the off-by-one is exactly the clip newline — matching the pre-data addendum, and matching the lane's live second convention: `check_sibling_census.description_of` on the same bytes returns **1021** (`len` 1021, equal to the clip render minus its trailing newline). The two numbers coexist in the lane by design, not by error, but every receipt must name which one it prints (addendum 1 requirement).

## 4. Cross-references the correction leans on

- `corpus/lessons/round-75-verifier-spotcheck.md:63` is the DISAGREE row (Gate reject re-check) and `:72` is `| quality | **harmed** |` — the correction's citations resolve to the intended lines.
- `plans/round-75.md:7` names `Surface: SKILL.md:193`, and the row at that line contains the equality wording (`…equality; the reference run_eval…`): the correction's "round 75's C1 is the equality-threshold claim on `SKILL.md:193`" is grounded.
- `corpus/QUALITY.md` has no `Q74` row at base (`grep -n Q74` empty), and the drafted row `B08-q74-quality-row.diff` states the same rule the correction summarises ("measure a folded block scalar by its render at a named revision, never on a line window"), grounded in M76-1. The number is free.
- No verifier pins `corpus/lessons/round-75.md` bytes (`grep -rn 'round-75' verifiers/*.py` empty), so the append does not break a frozen counter. The append adds no `commit \`<hex>\`` citation (`COMMIT_RE` from `verify_corpus_integrity.py` finds none in base or applied file) and no `.ufo/reports/round-N/*.md` pointer, so the corpus pointer/commit_total equalities are unmoved by this edit — the correction's own internal citation `.ufo/waves/round-76/receipts/r1-folded-render.txt` is outside both counted families.

## 5. The hazard: a whole-file containment check for R1 is green at base

At the base commit the superseded row and the Gate sentence are already in the file, so "does the lesson contain the superseded M75-1 text / the Gate reject candidate" is **true with no correction written at all**. Any R1 arm implemented as containment over the whole lesson therefore cannot fail its own must-fail world ("correction paragraph naming no superseded text") — the Q25/Q48 defect this lane has caught before. The build seat's own verification transcript shows the shape: `grep -cF any\ claim\ that\ the\ 1021-character… out/corpus/lessons/round-75.md` → `1`, `exit=0`, in a world where the patch had **failed to apply** (`patch: **** Can't open patch file r1.diff`, exit 2) — the 1 came from the base row, not from the correction.

The fix is one line: scope the search to bytes appended after the base, or to the `## Correction (appended` section. The conjunct below does that and is shown able to fail. It is 60 lines, dependency-free, and reads no git (the caller supplies the file):

```python
#!/usr/bin/env python3
"""R1 exactness conjunct, scoped to the appended correction section."""
import hashlib, json, sys
FIX = json.load(open("fixtures.json"))          # row, clause_row, clause_gate (+sha256)
HEADING = "## Correction (appended"

def section(text):
    i = text.find(HEADING)
    return "" if i < 0 else text[i:]

def main():
    root = sys.argv[1]; rel = sys.argv[2] if len(sys.argv) > 2 else "corpus/lessons/round-75.md"
    text = open(f"{root}/{rel}", encoding="utf-8").read(); sec = section(text)
    arms = {
        "correction-section present": bool(sec),
        "row clause exact": FIX["clause_row"] in sec,
        "gate clause exact": FIX["clause_gate"] in sec,
        "full M75-1 row exact (793 chars)": FIX["row"] in sec,
        "renders 1022 asserted": "1,022" in sec,
        "content lines 4-18 asserted": "lines 4\u201318" in sec,
        "spot-check cited": "corpus/lessons/round-75-verifier-spotcheck.md" in sec,
    }
    for k, v in arms.items(): print(("PASS " if v else "FAIL ") + k)
    print(f"\nr1 exactness: {sum(arms.values())} of {len(arms)}")
    return 0 if all(arms.values()) else 1

if __name__ == "__main__":
    sys.exit(main())
```

Results (each world built in scratch from the committed base + the draft, the file named on the command line):

| world | score | exit | failing arms |
|---|---|---|---|
| committed base `b7f13f4` bytes, no correction | `0 of 7` | 1 | all seven |
| draft applied (appended tail `c57e41e3…`) | `7 of 7` | 0 | — |
| mutant: row clause truncated with `…` (ellipsis), row abridged | `5 of 7` | 1 | row clause exact; full row exact |
| mutant: en dash → hyphen in `lines 3–18` / `lines 4–18` | `4 of 7` | 1 | row clause; full row; lines 4–18 |
| mutant: Gate sentence wrapped in curly quotes `“…”` | `6 of 7` | 1 | gate clause exact |
| mutant: token dump (heading + `1,022` + `lines 4–18` + spot-check name, no quoted bytes) | `4 of 7` | 1 | row clause; gate clause; full row |

The token-dump world is the one the plan's C2 control `C2-W1` asks for ("repair files with forged values → fails"); it fails here on the quoted-bytes arms while passing the number and citation arms, which is the discrimination the frozen counter needs.

## 6. What is not verifiable yet (blocking R1's closure, not this seat's verdict)

1. `verifiers/check_r75_routed_repairs.py` — absent at 14:06:44. Its R1 arm must (a) scope to appended bytes per §5, (b) require both clause strings exactly (not fragments; Q32), and (c) carry the red-before receipt. Its self-test must-fail arm "correction paragraph naming no superseded text" is exactly the mutant row above; if the arm is written as whole-file containment it will pass silently.
2. `.ufo/waves/round-76/receipts/r1-folded-render.txt` — absent. Per addendum 1 it must name the measured revision and print **both** variants with the convention named (`1022` clip / `1021` stripped); a receipt that prints only `1022` does not meet the addendum, and a receipt that prints only `1021` cannot satisfy the frozen predicate. The correction's citation of both artifacts is forward-looking at draft time, which is normal pre-freeze, but the closure should re-run this section's §2/§3 arms against the committed tip bytes rather than against the build draft.
3. The correction is a build artifact (`build/B08-r1-round-75-correction.diff`), not committed bytes. Everything in §2 is "draft applied to base bytes", not "committed tip". My verdict is therefore about the draft's fidelity, which is what a pre-landing review can settle; the tip check is one `git show <tip>:corpus/lessons/round-75.md | python3 check_r1_exact.py` away once it lands.

## 7. Adjacency notes (recorded, not fixed here)

- **First-sentence convention is unclosed.** The correction prints 151 (strip, then `split('. ')[0]+'.'`); a regex ending at the first `.`-plus-whitespace prints **152** (it keeps the trailing space). The addendum fixed the clip/strip convention for the render but not this one; C1 conjunct (d) measures "first-sentence length", so the two seats can disagree by one and both be defensible. Fix the convention (with or without the separator space) before the counter freezes.
- **The lane's own guard prints the other number.** `check_sibling_census.description_of` returns 1021 for the same bytes; a future reader comparing the correction's 1022 with that guard's 1021 will see a one-character contradiction unless the convention sentence travels with both numbers — which the correction and addendum do, and Q74 is drafted to require.
- **Q29's sweep scope excludes lessons.** `check_correction_sweep.py`'s registry covers README/SCORECARD/SKILL/PROVINCE/knowledge entries, not `corpus/lessons/*.md`, so nothing regresses this correction if the appended section is later edited. The correction's own guard is the round-76 counter; a sweep row is not owed, but the exposure is real and should be named in the round-76 lesson rather than left implicit.
- **The "withdraws the plan's base note" phrasing.** The plan file stays as filed (it is not in the touch list and is not edited by the draft); the withdrawal exists only as this appended correction. That is the correct append-only discipline, but the sentence could read as an in-place plan edit; naming the plan line as "superseded by this appended correction" removes the ambiguity.
- **B08's verify transcript contains two false-green arms** (`grep -cF … out/…` = 1 on texts that exist in the base file, §5) and two red arms caused by its own missing patch file. The artifact it produced is correct; its self-verification did not prove that, and the closure should not cite that transcript as evidence for R1.

## 8. Confidence

- Exactness of the two quoted strings and the full row copy against committed `corpus/lessons/round-75.md` (sha `7f260fd5…`): **high** — byte containment plus zero-opcode diff plus hash.
- Folded render 1022 at `ac9f295` and the arithmetic table: **high** — recomputed by an independent script and by the correction's own command, both exit 0.
- Slice-convention claim (1022 vs 1021): **high** — both slices executed.
- First-sentence 151: **high for the stated convention**, and the convention is stated; the 152 variant is an inference about what another seat's counter may implement.
- `plans/round-75.md:15` and `SKILL.md:193` referents: **high** (verbatim substring; the plan line names the surface).
- R1 closure at tip: **not established** — counter and receipt absent at observation; §6 lists the exact arms to re-run.
- Whole-file containment hazard being reachable in the eventual counter: **inference** from the shape of B08's transcript and from the base file containing both strings; not observed in `check_r75_routed_repairs.py`, which does not exist yet.

Housekeeping: no tool installed, no git/jj mutation, no lane file written except this report; all fixture work was done in `/fast/scratch/hyaku/kotoba-r76/A29RevengerR1/`, removed before this report was handed off (the conjunct source and every fixture hash needed to rebuild it are inline above).

Report: .ufo/waves/round-76/w1/A29RevengerR1.md
