# RevRcRd — audit of repairs R-c / R-d against r60 closure defects 2 / 4

Seat: `kotoba-r61-wave-RevRcRd` (reviewer, round-61 v2 wave, attempt 1, hyaku run 5).
Date of all measurements: 2026-10-23. All reads are of committed bytes; the five audited
files were verified byte-identical to their committed blobs (path-scoped
`git status --porcelain` empty, see §5). Read-only audit: no lane/fleet write except this
report; no git/jj mutation (only `git log`/`git status` reads); no dispatch; no ask tool.
No pacman (paused); no installs.

Scope: R-c ↔ r60 spotcheck defect 2 (evidence pointer), R-d ↔ r60 spotcheck defect 4
(census-after file), both as frozen in `verifiers/check_routed_repairs.py` (freeze commit
`7827628a939b0333c89892dfcedc72e390ccfb60`, 2026-10-23T16:07:09-03:00 = 19:07:09Z,
"round-61: plan freeze …, C2 routed-repairs counter + base control, census-before, v2 wave
spec+dispatch"). Verdict up front: **both repair requirements are factually well-formed and
the required direction of R-c is the true direction of the committed r60 bytes.** R-c/R-d
are "missing" at base (counter 0 of 6, exit 1 — independently reproduced); both land at
integration. Findings below are wording/verification requirements the landed bytes must
meet, plus two low-severity hardening notes.

---

## 1. R-c — the base-measurement pointer (defect 2)

### 1.1 What the closure defect says (committed bytes)

`corpus/lessons/round-60-verifier-spotcheck.md` (frontmatter: `lane_tip: 79cf2638…`,
`base: 31092dc6f875370bddd6eb1e4da4ca0d210c56af`), defect 2:

```
117|2. **Evidence pointer.** The base measurement (`31092dc6`, exit 1) is committed in
118|   `receipts/freeze2-selftest.txt`, not in `C1-measure.txt` as the report's joint
119|   citation implies. Evidence exists; the pointer is imprecise.
```

Same file's spot-check table rows 44–46 already state the true mapping:

```
44|| base measurement | `.ufo/waves/round-60/receipts/freeze2-selftest.txt` | `scoped rule files backed on committed snapshots 0 of 0; live not run`, exit 1 @ `31092dc6` | PASS |
45|| after measurement | `.ufo/waves/round-60/C1-measure.txt` | `4 of 4 backed; 4 of 4 live`, `--fetch` exit 0 @ `7b80ae80`; non-fetch run exit 1; L1 sandbox re-run 2026-10-23T12:28:23Z | PASS (supporting evidence, per E2) |
46|| gate self-test | `freeze2-selftest.txt` | `self-test: 0 failure(s) over 318 assertions`, exit 0 | PASS |
```

The original sloppy citation — fleet report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md:34`:

```
34|- Base `31092dc6` (measured at the freeze and re-run by this L1): `scoped rule files backed on committed snapshots 0 of 0; live not run`, exit 1 (`.ufo/waves/round-60/receipts/freeze2-selftest.txt`, `C1-measure.txt`).
```

The parenthetical joint citation puts `C1-measure.txt` beside the base measurement; the
file does not contain it (below). That is exactly the imprecision R-c must name.

### 1.2 Verifying read #1 — the committed r60 BASE receipt

`.ufo/waves/round-60/receipts/freeze2-selftest.txt`, read in full 2026-10-23 (working tree,
verified == committed blob):

```
# freeze-2 receipt: sandbox clone /fast/scratch/hyaku/kotoba-r60/L1freeze2 at b1cd64bb45eee744c4ec93be8631f1eddb28fddd; 2026-10-23T11:39:30Z
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
$ timeout 600 python3 -B verifiers/check_scoped_rules.py --self-test
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions
exit 0
$ timeout 300 python3 -B verifiers/check_scoped_rules.py --rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af
exit 1
scoped rule files backed on committed snapshots 0 of 0; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af
```

### 1.3 Verifying read #2 — the committed r60 AFTER receipt

`.ufo/waves/round-60/C1-measure.txt` (note: lane-round-60 top level, **not** under
`receipts/`), read in full 2026-10-23 (working tree, verified == committed blob):

```
# C1 measurement (supporting evidence; C1 is exploratory per plan § Erratum E2): sandbox clone /fast/scratch/hyaku/kotoba-r60/L1measure at 7b80ae80cda69a95b6fc90879395113a99a57912; 2026-10-23T12:28:23Z
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7b80ae80cda69a95b6fc90879395113a99a57912
exit 1
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7b80ae80cda69a95b6fc90879395113a99a57912
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7b80ae80cda69a95b6fc90879395113a99a57912 --fetch
exit 0
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7b80ae80cda69a95b6fc90879395113a99a57912
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
C1 predicate: --fetch exit 0 (F>=TARGET) — MET (supporting evidence only)
$ timeout 300 python3 -B verifiers/check_gate_registry.py --rev 7b80ae80cda69a95b6fc90879395113a99a57912
verifiers/verify_skill_checklist.py          OK
verifiers/verify_surfaces.py                 OK
gate registry rows conformant 34 of 34 lane verifiers; phantom 0
```

### 1.4 R-c fact verdict

- `freeze2-selftest.txt` holds the **base run**: `--rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af`
  → `scoped rule files backed on committed snapshots 0 of 0; live not run`, **exit 1**
  (31092dc6 is the r60 base per the spotcheck frontmatter). It holds no `--fetch` run and
  no `7b80ae80` occurrence.
- `C1-measure.txt` is **after-only**: every measured run is at rev
  `7b80ae80cda69a95b6fc90879395113a99a57912` (plain run exit 1; `--fetch` exit 0 = the MET
  predicate). The string `31092dc6` occurs nowhere in it.
- So the assignment's required direction — `receipts/freeze2-selftest.txt` = base
  measurement, `C1-measure.txt` = after-only — **matches the committed r60 files' actual
  contents**. Confirmed, not assumed.

### 1.5 The frozen R-c arm and what a landed line must say

`verifiers/check_routed_repairs.py` (freeze commit `7827628`), R-c arm:

```python
    rc = any(
        "receipts/freeze2-selftest.txt" in line and "C1-measure.txt" in line
        for line in log.splitlines()
    )
    why.append(f"R-c base-measure pointer: {'ok' if rc else 'missing'}")
```

Self-test fixture line (correct direction, from `self_test()`):

```
erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt
```

The arm requires both literals on **one LOG.md line** and cannot check direction: an
inverted line ("base is C1-measure.txt, not freeze2…") would also count. The checker
docstring assigns that judgment to reviewers ("it does not judge whether a repair text is
substantively honest — reviewers remain responsible for that (Q31)").

**RC-1 (must-hold direction, reviewer requirement).** The landed R-c erratum line must
state, with the full committed paths and revs, exactly:

> base measurement = `.ufo/waves/round-60/receipts/freeze2-selftest.txt`
> (`--rev 31092dc6…` exit 1, `0 of 0; live not run`); `.ufo/waves/round-60/C1-measure.txt`
> is after-only (runs only at `7b80ae80…`; plain exit 1, `--fetch` exit 0) and holds no
> base-rev run.

A line naming both files with the direction inverted satisfies the counter and must fail
review. The self-test fixture's own wording is in the correct direction; keep it that way
in LOG.md.

**RC-2 (LOW, wording).** The bare string `receipts/freeze2-selftest.txt` becomes ambiguous
this round: R-f creates a second receipts dir (`.ufo/waves/round-61/receipts/
controls-ancestry.txt`). The landed line should use the full r60 path
`.ufo/waves/round-60/receipts/freeze2-selftest.txt` (still contains the checker's literal,
so the arm is unaffected).

---

## 2. R-d — the standalone committed census-after (defect 4)

### 2.1 What the closure defect says (committed bytes)

`corpus/lessons/round-60-verifier-spotcheck.md:125-128`:

```
125|4. **Census-after file.** No standalone committed census-after output file; the after
126|   census is recorded in `residual/ReviewMeasure.md:84` (exit 0, 13 W04) and was
127|   re-run live by this closure (exit 0, `kotoba ok`). Round-end exit-0 conformance
128|   is satisfied; commit the output file next round.
```

### 2.2 The frozen census command

Named in the round driver, `/home/vgpnk/Projects/shokunin/.ufo/prompts/kotoba-round-61.md:64-66`:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
```

Same command family as r49/r51/r52/r53 plans and the r60 spotcheck row 51
(`scripts/sources-census.sh validate --root … kotoba`). The script header declares the
validate mode read-only ("writes only stdout or --out"); W04 = same URL across scopes
(warning class; exit 0 with warnings).

### 2.3 Verifying read #3 — the committed census-before

`.ufo/waves/round-61/census-before.txt`, committed with the plan in freeze commit
`7827628` (`git log -n1 -- <path>` →
`7827628a939b0333c89892dfcedc72e390ccfb60 2026-10-23T16:07:09-03:00 round-61: plan freeze …`),
13 W04 rows (grep -c W04 → 13), last non-empty line `exit=0`. Full content:

```
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

Note: census-before.txt does **not** embed the command that produced it — it is bare
command stdout + the `exit=0` tail.

### 2.4 Rerunning the frozen census command (read-only)

Command, 2026-10-23 (paste of run at 2026-10-23 07:13:45 PM UTC), exit code shown:

```
Fri 23 Oct 2026 07:13:45 PM UTC
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

Byte-diff of (rerun stdout + `exit=0`) against the committed census-before.txt:

```
IDENTICAL-TO-COMMITTED-CENSUS-BEFORE
```

(diff exit 0 → zero differing lines). So the frozen census command today reproduces the
committed census-before byte-for-byte, and a census-after of the same shape ending
`exit=0` is producible at integration.

### 2.5 The frozen R-d arm

`verifiers/check_routed_repairs.py` (freeze commit `7827628`), R-d arm:

```python
    census = blobs.get(".ufo/waves/round-61/census-after.txt")
    rd = (
        census is not None
        and [ln for ln in census.splitlines() if ln.strip()][-1].strip() == "exit=0"
        if census is not None
        else False
    )
    why.append(f"R-d census-after file: {'ok' if rd else 'missing'}")
```

Self-test arms cover it from both sides: the all-repairs world uses
`census_after = "kotoba ok\nexit=0\n"` (→ 6 of 6) and the damaged variant
`".ufo/waves/round-61/census-after.txt": "exit=1\n"` drops to 5 (must-fail arm present).

- "Standalone committed file" is structurally enforced: the arm reads the blob only via
  `git show <rev>:<path>`; an uncommitted working-tree file cannot satisfy it.
- `exit=0` as the last non-empty line is enforced, case/spacing-exact after `.strip()`.

### 2.6 R-d fact verdict and findings

- census-after does not exist yet (absent from `.ufo/waves/round-61/` at audit time) —
  correct per plan § Frontier step ("committed at integration"). Nothing to judge on its
  bytes; the requirement is well-formed and reproducible (§2.4).

**RD-1 (reviewer requirement at integration).** The R-d arm reads only the **last
non-empty line**; a body-less file containing just `exit=0` passes the counter. The honest
census-after must carry the full frozen-command output — same shape as census-before (13
W04 rows today, `kotoba ok`, `exit=0`) — with any W04 delta explained by real SOURCES.md
rows landed this round, not silently grown. The r60 defect was precisely an after-census
that existed only inside a seat report; do not re-create that shape in a new wrapper.

**RD-2 (LOW, instrument pinning).** The census instrument is a fleet-repo script
(`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`), not pinned by any lane
commit, and census-before.txt does not embed the command or a script hash. When R-d is
cited, record beside it (LOG.md line, or header lines above the output inside
census-after.txt — both compatible with the last-line arm): the command, `date -u`, and
`sha256sum` of the script (Q24/Q13 receipt practice).

---

## 3. Base control (the fix shown able to fail) — independently reproduced

The committed receipt `.ufo/waves/round-61/controls/C2-base.txt` (freeze commit `7827628`,
working tree == committed blob):

```
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
base-exit=1
```

My independent rerun at the frozen base (read-only; counter reads committed blobs via
`git show`), paste:

```
Fri 23 Oct 2026 07:13:45 PM UTC
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

(command: `python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326`;
exit 1.) R-c and R-d both read `missing` at base — both repairs are shown able to fail,
matching plan § C2 ("at base `f3246d14`: `0 of 6`, exit 1").

**OBS-1 (LOW, adjacent — the control receipt for both audited repairs).**
`C2-base.txt` does not record the rev, command, or date it measured; the binding to
`f3246d14` lives only in the plan text and the freeze commit message. This rerun closes
that gap (same output at the named rev). Recommend the L1 keep future control receipts
self-describing. Non-blocking.

---

## 4. Findings summary (severity order)

1. **RC-1 (reviewer must-hold, medium weight):** the R-c arm cannot check direction; the
   landed LOG.md erratum must name `.ufo/waves/round-60/receipts/freeze2-selftest.txt` as
   the base measurement (exit 1 @ `31092dc6`) and `.ufo/waves/round-60/C1-measure.txt` as
   after-only (runs only @ `7b80ae80`). Verified true direction of the committed bytes in
   §1.2–1.4; an inverted line would still count 6 of 6 and must fail review.
2. **RD-1 (reviewer must-hold at integration):** census-after must be the full
   frozen-command output ending `exit=0`, not a bare last-line file; the counter reads
   only the last non-empty line (§2.5–2.6).
3. **RC-2 (low):** use the full r60 path for the freeze2 receipt — round-61 now also has a
   `receipts/` dir (R-f), so the bare `receipts/…` name is ambiguous in prose.
4. **RD-2 (low):** pin the census instrument (command + script sha256 + date) beside the
   R-d citation; the script is fleet-repo bytes a lane commit does not freeze.
5. **OBS-1 (low, adjacent):** C2-base receipt lacks self-describing provenance (rev/
   command/date); independently reproduced at `f3246d14` this audit.

No counter-defect found in the frozen checker: both arms are implemented as documented,
both have must-fail self-test coverage (`exit=1` damaged census arm; base world 0 of 6),
and the committed docstring correctly scopes what the counter does not judge (Q31).

## 5. Verification method, residues, gaps

- All quoted file contents were read from the working tree and confirmed identical to
  committed blobs: path-scoped `git status --porcelain -- .ufo/waves/round-60/receipts/freeze2-selftest.txt .ufo/waves/round-60/C1-measure.txt verifiers/check_routed_repairs.py .ufo/waves/round-61/census-before.txt .ufo/waves/round-61/controls/C2-base.txt`
  → empty (exit 0). The lane working tree has other in-flight dirty lines (19 at audit
  time, wave/L1 work, not touched by me); none overlap the audited paths.
- The checker base rerun reads committed blobs only (`git show rev:path`), so the dirty
  tree cannot affect it. The census rerun reads the working-tree `corpus/SOURCES.md`; its
  byte-identity to census-before shows the census-relevant rows are unchanged.
- Not verified (does not exist yet, lands at integration): the LOG.md R-c/R-d lines, the
  census-after bytes, R-f's controls-ancestry receipt. This audit pins the facts those
  bytes must match and the exact arms that will count them.
- No jj/git mutation, no lane write besides this report, no scratch cited as evidence.
  Scratch used: `/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-RevRcRd/` (empty of
  evidence-bearing content; the diff/rerun outputs are pasted above).

---

Installs: no installs (no tools installed or upgraded; pacman untouched, host-wide pause respected).
Blockers: none.
One line: attacked R-c/R-d — verified against the committed r60 receipts that
`freeze2-selftest.txt` holds the base run (exit 1 @ 31092dc6) and `C1-measure.txt` is
after-only (7b80ae80), reproduced the C2 base control (0 of 6, exit 1 @ f3246d14), and
byte-reproduced the committed census-before from the frozen fleet census command (exit 0,
13 W04).
