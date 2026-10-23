# FalsifyLesson — attack on `corpus/lessons/round-62.md` (round 62 wave 2)

Seat: `L1kotoba62.FalsifyLesson`. Scope: the lesson file only — M93 evidence
pointer, Gate S118 record, rejected-candidate bullets, status-change line, and
per-count command discipline (Q54). Lane tip attacked:
`e6da78bbe420722dd18a13182a7c4b64ce02f005` (`git rev-parse HEAD`). Read-only
posture kept; the only write is this report.

## Verdict

One substantive defect (a false evidentiary claim inside M93's own "shown able
to fail" clause), one minor imprecision. Every other attacked item verified
against committed bytes.

## Findings

### F1 — DEFECT (moderate): M93's "shown able to fail" clause states a diagnostic that its cited receipt does not contain

`corpus/lessons/round-62.md:25` (M93, final clause) claims:

> `.ufo/waves/round-62/controls/absorption-hollow.txt:5-8` records the hollow
> variant exiting 1, but its diagnostic is a missing `check_scoped_rules.py`
> path, not the intended guard-direction rejection

Measured against the cited bytes at tip:

- `grep -c 'check_scoped_rules.py' .ufo/waves/round-62/controls/absorption-hollow.txt` → **0**
- `absorption-hollow.txt:7-8` actual content:

  ```
  $ python3 -B /tmp/r62hollow/hollow.py --self-test
  absorption self-test failed: guard-mutation direction is missing for one or more errata
  ```

  i.e. the recorded diagnostic **is** the intended guard-direction rejection —
  the exact string raised by the instrument's `validate_run` require at
  `verifiers/check_erratum_absorption.py:337`. The receipt file is unchanged
  since its only commit `3e7aed9` (`git log --oneline --
  .ufo/waves/round-62/controls/absorption-hollow.txt` → one entry), so the
  claim was never true of the committed receipt.

- The claim was inherited from the wave-1 scribe draft: committed
  `git show HEAD:.ufo/waves/round-62/w1/ScribeLessonQ57.md:46` asserts the same
  false "missing `/tmp/r62hollow/check_scoped_rules.py` path" diagnostic. The
  working tree carries an uncommitted edit to that file
  (`git status --porcelain` → ` M ScribeLessonQ57.md`) but the edit touches a
  different line (the no-tests-run disclaimer, `:49` in the diff); the false
  sentence stands in both versions.

- Effect of the defect: the lesson understates the control it cites. Per the
  plan's kill rule (`plans/round-62.md:95-96`), the hollow auditor "must fail" —
  and the committed receipt shows it failing *for the intended reason*, not a
  path artifact. The lesson's "shown able to fail" evidence is therefore
  misreported in the conservative direction: the control is stronger than the
  lesson says. The clause's second half is accurate
  (`ExecAbsorbInstrument.md:70-72` does record the hollow shortcut rejected for
  missing run records — verbatim text confirmed).

- Recommended repair: rewrite the clause to state what the receipt shows —
  hollow exits 1 with the guard-direction diagnostic — and drop the
  missing-path characterization (or attribute it to nothing, since no
  committed artifact contains it).

### F2 — IMPRECISION (minor): "the action check contains only support-fraction logic"

`corpus/lessons/round-62.md:25` — inside the cited range,
`verifiers/check_scoped_rules.py:1010-1040` (`action_conjunct`) contains, in
addition to the forward/reverse support fractions (`fwd_need`/`rev_need`,
`:1025-1029`, `:1035-1039`), two non-fraction conjuncts: a minimum distinct
content-word count (`MIN_CONTENT`, `:1021-1023`) and a page-occurrence check
("action word(s) %s do not occur on the committed snapshot", `:1030-1034`).
"Only support-fraction logic" is imprecise; the operative claim (no G7
event-claim conjunct, no G9 compound-purpose conjunct) is verified correct —
the function returns `[]` at `:1040` with no backticked-identifier or
claim-verb arm.

## Verified clean (with evidence)

- **M93 evidence pointer resolves.** `verifiers/check_scoped_rules.py:972-1040`
  covers `content_words` (`:972-977`; `BACKTICK_RE.sub(" ", text)` at `:975` —
  the backticked-span strip, confirmed) and `action_conjunct` (`:1010-1040`).
- **r61 quote.** `.ufo/reports/round-61/kotoba.md:40` contains "five pre-data
  arm amendments each forced by a measured attack (MutA3, MutFixtures, MutA4
  ×3 seams, MutA1, MutA2)" verbatim (the lesson drops only the parenthetical).
- **Draft-text claim.** `plans/round-62.md:19-24` records the r61 attacks as
  measured against draft predicate text; `ScoutPriorReceipts.md:10-18` table
  shows every erratum columned "no" under committed receipt, with `:18` naming
  the r61 report line.
- **Matrix line.** `absorption-hollow.txt:17-28` (command `python3 -B
  verifiers/check_erratum_absorption.py --self-test`, output `errata measured
  5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`, `exit=0`) — and the
  canonical data receipt `.ufo/waves/round-62/C1-absorb-measure.txt` carries
  the identical command/output/exit. The lesson's pointer to the control
  receipt rather than the canonical `C1-absorb-measure.txt` is unusual but
  the quoted bytes are byte-identical in both.
- **v31 pointers.** `check_scoped_rules_v31.py:1046-1088` contains
  `g7_conjunct` and the extended `action_conjunct` calling it; `:2578-2615`
  contains the survivor-verdict block printing `survivors closed %d of 6` and
  the check `"G9 remains a declared surviving bound"` with
  `bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation
  survives per CriticC1Hollow` — "explicitly keeps G9 as a declared surviving
  bound" confirmed.
- **Gate S118 record.** URL, access time `2026-10-23T20:49:56Z`, HTTP 200,
  55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`
  all match the committed snapshot (`sha256sum` → identical; `wc -c` →
  55354) and the seat report `.ufo/waves/round-62/w1/SrcRulesFrontmatter.md:11-25`
  (the cited range holds the `date` description, the curl command block, and
  the output block). Quote: `sed -n '250p' .ufo/waves/round-62/snapshots/S118.page`
  → `| \`paths\` | No | Glob patterns that [scope the rule to matching
  files](#path-specific-rules). …` — the lesson's ≤25-word de-markdowned
  quote is verbatim text on that line; `memory.md:250` and § Rule frontmatter
  reference (`:244-250` span) confirmed.
- **Census command.** `census-before.txt:3` carries the exact recorded command;
  `:4-18` are W04 warnings, `:19` `ok`, `:20` `exit=0` — "exit 0
  (`census-before.txt:3-20`)" verified.
- **Rejected candidates (all four shas spot-verified).**
  - Bullet 1 (lesson `:19`): S047 `.md` URL 404 with 9-byte `Not Found` body —
    `ScoutKeyPagesA.md:145-152`; Cursor `rules.md` 404 and `reference/plugins.md`
    404 with `# Page not found` — `:162-169`; census list `:224-225`. All cited
    ranges accurate.
  - Bullet 2 (lesson `:20`): `cursor.com/docs/context/rules` → `redir=1` to
    `cursor.com/docs/rules`, same sha256 — `ScoutKeyPagesA.md:193`, `:224`. Alias
    characterization accurate.
  - Bullet 3 (lesson `:21`): all four sha256 strings match
    `ScoutKeyPagesA.md:156` verbatim (`6e7964dc…`, `90150f5a…`, `25f43326…`,
    `2d842e6b…`); the source line supports the lesson's summary (enumeration
    probes rejected for lacking the `applyTo`/frontmatter field table).
- **Status change.** `corpus/SOURCES.md:129` used-by names
  `corpus/lessons/round-62.md` and `corpus/knowledge/erratum-absorption-round62.md`
  (file exists). The `queued`→`mined` line: S118's row was committed `mined`
  from first appearance (status cell extracted from every `-S`-hitting commit
  `3e7aed9`, `89bdaf4`, `de7f01c`, `68af5b1` → all `| mined |`); `queued` was
  the seat-draft status (`SrcRulesFrontmatter.md:45` drafts `| queued`). This
  matches the lane's own convention — round-61 recorded S117 `queued`→`mined`
  identically (`corpus/lessons/round-61.md:31`) and S117 likewise was never
  committed queued — so the line is convention-consistent, not a defect.
  S103 (the row S118 re-opens) remains `mined` at `SOURCES.md:115`; the Gate's
  "admitted, not rejected; no reject/flip recorded" is consistent with the
  registry.
- **Q54 (no count without a command).** Every count in the lesson carries its
  command or a receipt pointer: the matrix line names
  `check_erratum_absorption.py --self-test` + receipt; census names the script
  invocation + receipt; `55,354 B`/sha256 come from the recorded
  `curl`/`sha256sum` output at `SrcRulesFrontmatter.md:11-25`. No orphan count
  found.
- **Cross-references.** Q57 row exists (`corpus/QUALITY.md:68`) citing M93 and
  the same control receipt; README index rows for the lesson and the
  erratum-absorption entry exist (`corpus/README.md:109-110`); SKILL.md
  registry rows for the three new gates exist (`SKILL.md:488-490`).

## Residual risk / gaps

- I did not re-run `check_erratum_absorption.py --self-test` in the lane
  (assignment scoped to the lesson file; the instrument's committed receipts
  were verified for internal consistency — `C1-absorb-measure.txt` and
  `absorption-hollow.txt` carry identical output lines — but the bytes were
  not re-executed under this seat). Other wave-2 seats own execution attacks.
- Uncommitted sibling edits in the working tree (` M ScribeEntry62.md`,
  ` M ScribeLessonQ57.md`; untracked `census-after.txt`, `w2/` artifacts) are
  the L1 integrator's in-flight work; flagged only because the scribe draft's
  false F1 sentence exists in committed form and the uncommitted edit does
  not fix it.
- The `## Falsify corrections` section (`round-62.md:32`) remains the
  placeholder "(to be filled by wave 2)" — expected pre-integration state;
  F1/F2 above are the corrections to record there.

## Installs

None. Tools used: `git` (read-only log/show/diff/status/rev-parse), `sha256sum`,
`sed`, `grep`, `wc` — all preinstalled host binaries. No lane file was modified
other than this report.
